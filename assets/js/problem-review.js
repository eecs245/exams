(() => {
  "use strict";

  // Store each problem separately so changes to different flags in other tabs
  // never overwrite one another.
  const prefix = "eecs245:review:";
  const idPattern = /^([\p{L}\p{N}_-]+)\/(q[0-9]+)$/u;
  const homepage = document.getElementById("flagged-problems");
  const controls = [...document.querySelectorAll("h2[data-review-id]")].map(addControl);

  function addControl(heading) {
    const { reviewId, reviewLabel } = heading.dataset;
    const key = prefix + reviewId;
    const button = document.createElement("button");
    button.type = "button";
    button.className = "problem-review-toggle";
    button.setAttribute("aria-label", "Flag " + reviewLabel + " for review");

    const icon = document.createElement("span");
    icon.setAttribute("aria-hidden", "true");
    const label = document.createElement("span");
    button.append(icon, label);
    heading.append(button);

    const error = document.createElement("span");
    error.className = "problem-review-error";
    error.setAttribute("role", "alert");
    heading.after(error);

    function updateButton() {
      let flagged = false;
      try {
        flagged = localStorage.getItem(key) !== null;
      } catch {
        // The user gets feedback if they try to flag with storage blocked.
      }
      button.setAttribute("aria-pressed", String(flagged));
      icon.textContent = flagged ? "⚑" : "⚐";
      label.textContent = flagged ? "Flagged" : "Flag";
    }

    button.addEventListener("click", () => {
      try {
        if (localStorage.getItem(key) === null) {
          localStorage.setItem(key, JSON.stringify({ label: reviewLabel, time: Date.now() }));
        } else {
          localStorage.removeItem(key);
        }
        error.textContent = "";
      } catch {
        error.textContent = "Couldn’t update this flag. Check your browser’s site storage settings.";
      }
      refresh();
    });
    return updateButton;
  }

  function getFlags() {
    const flags = [];
    for (let index = 0; index < localStorage.length; index++) {
      const key = localStorage.key(index);
      if (!key?.startsWith(prefix)) continue;
      const problem = idPattern.exec(key.slice(prefix.length));
      if (!problem) continue;

      let entry;
      try {
        entry = JSON.parse(localStorage.getItem(key));
      } catch {
        continue;
      }
      if (typeof entry?.label !== "string" || !Number.isFinite(entry.time)) continue;

      const [, exam, question] = problem;
      const path = encodeURIComponent(exam) + "/#review-" + encodeURIComponent(exam + "-" + question);
      flags.push({ label: entry.label, time: entry.time, path });
    }
    return flags.sort((a, b) => b.time - a.time);
  }

  function renderHomepage() {
    const list = homepage.querySelector(".problem-review-list");
    const message = homepage.querySelector(".problem-review-message");
    const emptyMessage = "Flag a problem on any exam or worksheet to find it here.";
    list.replaceChildren();

    try {
      for (const flag of getFlags()) {
        const item = document.createElement("li");
        const link = document.createElement("a");
        link.href = homepage.dataset.examsUrl + flag.path;
        link.textContent = flag.label;
        item.append(link);
        list.append(item);
      }
      message.textContent = emptyMessage;
    } catch {
      message.textContent = "Flagged problems are unavailable because browser storage is blocked.";
    }

    list.hidden = list.childElementCount === 0;
    message.hidden = !list.hidden;
    homepage.hidden = false;
  }

  function refresh() {
    controls.forEach((updateButton) => updateButton());
    if (homepage) renderHomepage();
  }

  refresh();
  window.addEventListener("pageshow", (event) => {
    if (event.persisted) refresh();
  });
  window.addEventListener("storage", (event) => {
    if (event.key === null || event.key.startsWith(prefix)) refresh();
  });
})();
