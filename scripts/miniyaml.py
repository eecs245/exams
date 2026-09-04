"""A reader for the YAML subset this repo's _data files use.

CI and the machines that preview the site have bare Python -- no PyYAML -- and
the two data files are simple enough not to need it. Supported:

  - block mappings         key: value          nested by 2-space indentation
  - block sequences        - item              of scalars or of mappings
  - scalars                plain, "double-quoted", 'single-quoted'; integers
                           made of digits only become int
  - comments               # to end of line, blank lines anywhere

Not supported, deliberately: flow collections ({a: b}, [x, y]), anchors, multi-
line scalars, tabs. Jekyll reads the same files with a full parser, so anything
outside this subset would work on the site and silently misparse here; the
reader raises on shapes it does not understand rather than guess.
"""
from __future__ import annotations

import re
from pathlib import Path

_KEY = re.compile(r"^([A-Za-z0-9_.\-]+):(?:\s+(.*))?$")


class MiniYamlError(ValueError):
    pass


def load(text: str, source: str = "<string>") -> object:
    lines = _significant_lines(text, source)
    if not lines:
        return None
    value, index = _parse_block(lines, 0, lines[0][0], source)
    if index != len(lines):
        raise MiniYamlError(f"{source}:{lines[index][2]}: unexpected content after document")
    return value


def load_file(path: Path) -> object:
    return load(path.read_text(), str(path))


def _significant_lines(text: str, source: str) -> list[tuple[int, str, int]]:
    """(indent, content, line_number) for every line that carries data."""
    out: list[tuple[int, str, int]] = []
    for number, raw in enumerate(text.splitlines(), start=1):
        if "\t" in raw[: len(raw) - len(raw.lstrip())]:
            raise MiniYamlError(f"{source}:{number}: tabs are not allowed for indentation")
        stripped = _strip_comment(raw).rstrip()
        if not stripped.strip():
            continue
        indent = len(stripped) - len(stripped.lstrip(" "))
        out.append((indent, stripped.strip(), number))
    return out


def _strip_comment(line: str) -> str:
    """Drop a trailing comment, leaving # inside quotes alone."""
    quote = None
    for position, char in enumerate(line):
        if quote:
            if char == quote:
                quote = None
        elif char in ("'", '"'):
            quote = char
        elif char == "#" and (position == 0 or line[position - 1] in " \t"):
            return line[:position]
    return line


def _parse_block(lines, index, indent, source):
    if lines[index][1].startswith("- ") or lines[index][1] == "-":
        return _parse_sequence(lines, index, indent, source)
    return _parse_mapping(lines, index, indent, source)


def _parse_sequence(lines, index, indent, source):
    items: list[object] = []
    while index < len(lines) and lines[index][0] == indent and (
        lines[index][1].startswith("- ") or lines[index][1] == "-"
    ):
        _, content, number = lines[index]
        item = content[2:].strip() if content != "-" else ""
        if not item:
            # "-" alone: the item is the nested block on the following lines.
            value, index = _parse_block(lines, index + 1, lines[index + 1][0], source)
            items.append(value)
        elif _KEY.match(item):
            # "- key: value": a mapping whose first key sits after the dash.
            # Re-express that first line at the item's content column so the
            # mapping parser sees it as an ordinary key line.
            patched = lines[:index] + [(indent + 2, item, number)] + lines[index + 1 :]
            value, index = _parse_mapping(patched, index, indent + 2, source)
            lines[:] = patched
        else:
            items.append(_scalar(item))
            index += 1
            continue
        if _KEY.match(item):
            items.append(value)
    return items, index


def _parse_mapping(lines, index, indent, source):
    mapping: dict[str, object] = {}
    while index < len(lines) and lines[index][0] == indent:
        _, content, number = lines[index]
        if content.startswith("- "):
            break
        match = _KEY.match(content)
        if not match:
            raise MiniYamlError(f"{source}:{number}: expected 'key: value', got {content!r}")
        key, rest = match.group(1), match.group(2)
        if key in mapping:
            raise MiniYamlError(f"{source}:{number}: duplicate key {key!r}")
        if rest is None or rest == "":
            if index + 1 < len(lines) and lines[index + 1][0] > indent:
                mapping[key], index = _parse_block(lines, index + 1, lines[index + 1][0], source)
            else:
                mapping[key] = None
                index += 1
        else:
            mapping[key] = _scalar(rest)
            index += 1
    return mapping, index


def _scalar(text: str) -> object:
    text = text.strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in ("'", '"'):
        return text[1:-1]
    if text.startswith(("{", "[")):
        raise MiniYamlError(f"flow collections are not supported: {text!r}")
    if text.isdigit():
        return int(text)
    return text
