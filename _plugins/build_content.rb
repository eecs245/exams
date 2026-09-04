# Run scripts/build.sh before Jekyll reads the source tree, so that
# `jekyll serve` and `jekyll build` compose the exam pages and worksheets
# (and re-extract any exam whose LaTeX changed) without anyone running a
# script by hand. This is the LOCAL convenience only:
#
#   - CI runs build.sh as an explicit workflow step and sets
#     SKIP_CONTENT_BUILD=1 for its Jekyll step, so this hook is inert there.
#   - GitHub Pages' own Jekyll builder loads no _plugins/ at all (safe mode).
#     This site deploys from its own Actions run, which is why a plugin works.
#
# :after_reset is the right stage: it fires before Jekyll reads files -- our
# output is Jekyll's input -- and again on every --watch regeneration. Every
# write build.sh makes is compare-first, so a rebuild that changes nothing
# writes nothing and the watch loop settles.
Jekyll::Hooks.register :site, :after_reset do |site|
  next if ENV["SKIP_CONTENT_BUILD"]

  script = File.join(site.source, "scripts", "build.sh")
  Jekyll.logger.info "Content:", "running scripts/build.sh"
  ok = system("bash", script, chdir: site.source)
  raise "scripts/build.sh failed; fix the error above or set SKIP_CONTENT_BUILD=1 to bypass" unless ok
end
