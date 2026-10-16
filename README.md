# Util

A hub of quick-reference cheat sheets, programming concepts, and micro-tools.

## Viewing the Site
- **Live GitHub Pages Site**: [https://aidankeighron.github.io/Util/](https://aidankeighron.github.io/Util/)
- **UI Layout**: Uses a two-panel interface with a compact selector panel on the left (featuring real-time search filtering, collapsible categories, and item counters) and the active tool or cheat sheet displayed on the right.

---

## Adding Concepts, Languages, or Tools

### Adding a New Language or Category
1. Create a folder in `docs/assets/` named after your category or language (e.g., `docs/assets/Rust/`).
2. Add `{CategoryName}.md` to `docs/assets/Languages/`:
   ```markdown
   ---
   layout: language
   ---
   ```
3. Add concept or tool `.md` files into `docs/assets/{CategoryName}/` using the `script` layout.

### Adding a Concept or Tool Script
Create a `.md` file in `docs/assets/{CategoryName}/{ToolName}.md`:
```markdown
---
layout: script
language: {CategoryName}
---

## Tool or Concept Description

Your content, code snippets, or tool markup here.
```
Any added file is automatically discovered and listed in the left selector panel.

---

## Local Development & Testing

### Running Jekyll Locally
```bash
cd docs
bundle install
bundle exec jekyll serve
```
Open `http://localhost:4000/Util/` in your browser.

### Running Automated Tests
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```
Verifies front-matter schema integrity, category consistency, and layout structures.