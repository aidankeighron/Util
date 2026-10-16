# Zero-Database User-Scoped Storage Architecture Guide

This guide details how to build and expand private, client-side web tools that can be hosted statically on GitHub Pages with **zero backend databases**, **zero hosting costs**, and **complete user data privacy**.

---

## Architecture Summary

When building utility tools where users upload data (like game libraries, finance logs, or personal notes):
- **Traditional Approach**: Rent a VPS/Serverless DB (PostgreSQL, MongoDB, Supabase). You incur hosting costs, maintenance overhead, security surface, and liability for holding user data.
- **The Util Zero-DB Approach**:
  1. The tool is a **pure client-side static web application** (HTML/JS/CSS or React/Vue) hosted for free on GitHub Pages.
  2. Data is parsed and analyzed locally in the user's browser using **IndexedDB / OPFS** for speed and offline availability.
  3. For multi-device persistence and cloud backup, data is synced directly to the user's **Google Drive `appDataFolder`** via the Google Drive REST API.
  4. The developer pays **\$0**, stores **no user data**, and needs **no database servers**.

---

## Storage Layer Comparison

### 1. IndexedDB (Browser Sandbox)
- **Speed**: In-memory speeds, instantaneous queries, native hardware execution.
- **Capacity**: Browser allocates up to 60-80% of available disk space (gigabytes).
- **Security**: Bound by browser origin policy; inaccessible to third-party domains.
- **Trade-off**: Data stays on that specific device and browser profile; clearing browser history/cache can wipe data unless persistent storage permission is requested (`navigator.storage.persist()`).

### 2. Google Drive `appDataFolder` (User Cloud Storage)
- **Privacy & Security**:
  - Hidden from the user's regular Google Drive UI — users will not accidentally delete or modify the files.
  - The application can **only see the files it created**; it has zero access to the user's personal documents, photos, or emails.
  - Isolated per user: User A cannot access User B's files.
- **Capacity**: Backed by the user's 15 GB free Google account storage.
- **API Scope**: `https://www.googleapis.com/auth/drive.appdata` (Restricted app data scope).
- **Cost**: \$0 to the application developer.

---

## Recommended Hybrid Architecture

For every new tool you or an AI agent create:
1. **Load & Query**: Read uploaded files (e.g. CSVs) directly into IndexedDB.
2. **Visualize**: Render charts, search tables, and aggregations directly from the local IndexedDB.
3. **Backup / Sync**: Provide a "Sync with Google Drive" button that pushes a snapshot JSON payload to the user's `appDataFolder`.
4. **Restore**: On initial visit or login on a new machine, query `appDataFolder` to restore existing data.

---

## AI Agent Prompt Blueprint

To prompt an AI coding assistant to create a new tool adhering to this architecture:

```markdown
Build a static web application for [Tool Name / Purpose].

Architecture Constraints:
- Pure client-side static HTML/CSS/JavaScript (runs on GitHub Pages).
- Zero external database or backend server.
- Store primary data in IndexedDB for instant querying and offline work.
- Provide Google Drive appDataFolder sync using OAuth scope `https://www.googleapis.com/auth/drive.appdata` and Google Identity Services.
- All user inputs must be validated and sanitized.
- Ensure responsive UI with dark mode styling matching the Util palette:
  --gray-6: #111111;
  --gray-5: #151618;
  --gray-3: #22252a;
  --accent: #50dfb3;
  --white-1: #f3f4f6;
```

---

## Reference Implementation

See [`docs/assets/Tools/Storage Architecture.md`](docs/assets/Tools/Storage%20Architecture.md) for complete copy-pasteable JavaScript classes for `GoogleDriveStorage` and `LocalDB`.
