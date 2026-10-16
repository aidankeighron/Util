# Util

A hub of quick-reference cheat sheets, programming concepts, and zero-database client-side micro-tools.

## Viewing the Site
- **Live GitHub Pages Site**: [https://aidankeighron.github.io/Util/](https://aidankeighron.github.io/Util/)
- **UI Layout**: Uses a two-panel interface with a compact selector panel on the left (featuring real-time search filtering, collapsible categories, and item counters) and the active tool or cheat sheet displayed on the right.

---

## Zero-Database User-Scoped Storage Architecture

When building new tools (such as uploading and analyzing game library CSVs, personal finance trackers, or log analyzers), **you do not need a backend database**:
- **IndexedDB (Local-First)**: Parses and queries data directly in the user's browser sandbox for instant, zero-latency visualizations and offline use.
- **Google Drive `appDataFolder` (Cloud Persistence)**: Uses the restricted OAuth scope `https://www.googleapis.com/auth/drive.appdata` to save private data directly inside the user's hidden Google Drive application data folder.
  - Zero server hosting fees (\$0 backend cost).
  - Data is 100% private to the user; invisible in their regular Drive UI; the app can only see files it created; users cannot access each other's data.
  - Generous quota backed by the user's free 15 GB Google Drive storage.

For full architectural blueprints, copy-pasteable JavaScript classes (`GoogleDriveStorage`, `LocalDB`), and AI agent prompt templates:
- **Site Guide**: [Storage Architecture Page](docs/assets/Tools/Storage%20Architecture.md)
- **Standalone Document**: [docs/STORAGE_ARCHITECTURE.md](docs/STORAGE_ARCHITECTURE.md)

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

Your content, code snippets, or interactive tool markup here.
```
Any added file is automatically discovered and listed in the left selector panel and on category cards.

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
Verifies front-matter schema integrity, category consistency, documentation links, and layout structures.