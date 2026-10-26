# AGENTS.md

## What this repo is

A collection of standalone HTML/CSS course exercises (《高级网页设计》homework), not an application. Each `*.html` file is an independent lesson artifact; open them directly in a browser. There is no package manager, build step, linter, test suite, or dev server — do not add tooling, frameworks, or `package.json` unless explicitly asked.

## Conventions

- Filenames mix Chinese characters and spaces (e.g. `5-1 层叠与继承.html`, `4-1 css2.html`). Always quote paths in shell commands.
- Images live in `image/` (`1.jpg`–`5.jpg`). New exercises should reference them relatively as `image/N.jpg`; note `7-1 上图下文.html` currently omits the `image/` prefix — do not "fix" existing files unless asked.
- CSS is embedded in `<style>` inside each file; lessons build on prior lessons (later files keep earlier rules marked `上节课CSS（保留）`).
- Content and comments are in Chinese; keep new content consistent with that.
- Some files intentionally contain leftover comments, incomplete tags, or stray characters (e.g. trailing `s` in `4-1`/`5-1`, empty `5-2 盒模型.html`) — these are learning artifacts, not bugs to clean up unprompted.
- Student identity (学号 412 / 万逸泽) appears in titles and body text as part of the exercises.
- All CSS class names, id names, and JS variables/function names must start with `wan_` (e.g. `wan_box`, `wan_vwVal`, `wan_update`). CSS custom properties (`--brand`) and element selectors are not covered.
- **Newly created HTML files must include a hyperlink to the homepage `index.html`** (e.g. `<a href="index.html">首页</a>` in the header/footer). Note: `index.html` does not exist yet — it must be created before these links resolve; add the link anyway and create the homepage if asked.

## Workflow

- **Before executing any user prompt, append an entry to `wan prompt.md`** (append mode, never overwrite): timestamp, model used (currently `opencode/mimo-v2.6-flash-free`), and the full prompt text. Entry format:
  ```
  ## YYYY-MM-DD HH:MM:SS
  - 模型: <model id>
  - 提示词:
  <prompt text>
  ```
- When batch-editing HTML in PowerShell, note that `.ps1` files without a BOM are read as GBK by PowerShell 5.1 — keep scripts ASCII-only (glob for Chinese filenames) or write them with a UTF-8 BOM.
- Verify work by opening the HTML file in a browser; there is nothing to compile or run.
- Preserve each file's self-contained structure; do not extract shared CSS/JS or reorganize into folders unless asked.
