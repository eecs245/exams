# Publish .build/ -- the composed exam pages and topic worksheets -- into the
# site without those files ever existing in the source tree.
#
# scripts/build.sh composes every page from the questions in src/ into .build/
# (gitignored, and excluded in _config.yml). This generator mirrors that
# directory into the site: each .md becomes a virtual page, rendered exactly as
# if it sat at the same path in the source, and every other file (the images a
# page references) becomes a static file. So /exams/fa25-mt1/ and
# /worksheets/chapter-3/ are served, but there is no exams/ or worksheets/ at
# the repo root to edit by mistake -- they are rebuilt on every build anyway.
module ExamsSite
  class ComposedPages < Jekyll::Generator
    safe true
    priority :highest

    BUILD_DIR = ".build"
    # "w_r_axes 2.png": iCloud conflict copies. This repo lives in ~/Documents.
    SYNC_CONFLICT = %r!\s\d+\.[^./]+\z!.freeze

    def generate(site)
      root = File.join(site.source, BUILD_DIR)
      unless File.directory?(root)
        raise "#{BUILD_DIR}/ is missing: run scripts/build.sh (jekyll does this itself " \
              "unless SKIP_CONTENT_BUILD is set)"
      end

      pages = []
      Dir.glob("**/*", base: root).sort.each do |relative|
        path = File.join(root, relative)
        next unless File.file?(path)
        next if relative.match?(SYNC_CONFLICT)

        dir = File.join("/", File.dirname(relative))
        name = File.basename(relative)
        if name.end_with?(".md")
          pages << composed_page(site, path, dir, name)
        else
          site.static_files << Jekyll::StaticFile.new(site, root, dir, name)
        end
      end

      # Prepended, not appended: Jekyll renders pages in this order, and the
      # theme builds its search index from each page's RENDERED content -- it
      # names that file zzzz-search-data.json precisely so it sorts last. Pages
      # added after it would be indexed as raw Markdown, losing every "#"
      # heading and showing escapes in titles.
      site.pages.unshift(*pages)
    end

    private

    def composed_page(site, path, dir, name)
      # Explicitly UTF-8: the pages hold emoji and math, and the default external
      # encoding is US-ASCII wherever LANG is unset (cron, some CI shells).
      source = File.read(path, encoding: "UTF-8")
      match = source.match(Jekyll::Document::YAML_FRONT_MATTER_REGEXP)
      raise "#{path}: composed page has no front matter" unless match

      page = Jekyll::PageWithoutAFile.new(site, site.source, dir, name)
      page.data.merge!(SafeYAML.load(match[1]) || {})
      page.content = match.post_match
      page
    end
  end
end
