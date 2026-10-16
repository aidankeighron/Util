---
layout: script
language: Tools
---

# Zero-Database User-Scoped Storage Architecture

A blueprint for building private, client-side web tools that require **zero backend servers**, **zero database hosting fees**, and **zero maintenance**, while keeping each user's data completely private, secure, and scoped to their own Google account or browser.

---

## 1. Problem & Architecture Goals

When building quick micro-tools (such as a CSV games library analyzer, personal budget tracker, or log viewer):
- **Hosting a backend database is cumbersome**: Servers require maintenance, environment secrets, database migrations, security patches, and hosting bills.
- **Data privacy is non-negotiable**: If users upload personal data (e.g., game history, finances, notes), that data must **never** be stored on a shared public server or leaked to other users.
- **Tools should be shareable & free to host**: The frontend can be hosted as static files on GitHub Pages, Cloudflare Pages, or Vercel for free.
- **Cross-device persistence vs. instant local speed**: Users want the speed of local computing combined with the optional convenience of cloud backup across devices.

---

## 2. Storage Comparison

| Storage Mechanism | Setup Difficulty | Persistence | Storage Limit | Privacy | Best For |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **IndexedDB (Local)** | None (Browser built-in) | Device local | Up to 60-80% of free disk space | 100% private to device | Instant local queries, large CSV/JSON parsing, offline use |
| **Google Drive `appDataFolder`** | One-time Google OAuth Client ID | Cloud (Any device with Google login) | 15 GB free (User's Drive quota) | Completely hidden; app can only access its own files | Cross-device sync, cloud backup, user-scoped persistence |
| **Hybrid (Recommended)** | Low (GIS + IndexedDB) | Local-first + Cloud backup | 15 GB+ | Maximum privacy & performance | Production-grade serverless micro-tools |

---

## 3. Google Drive `appDataFolder` Deep Dive

The Google Drive API provides a dedicated hidden folder known as the **Application Data folder** (`appDataFolder`).

### Key Properties
1. **Hidden from User Drive UI**: Files stored in `appDataFolder` do not show up in the user's regular Google Drive file list, preventing accidental deletion or clutter.
2. **Strict App Isolation**: Your web application can **only** read and write files that it created. It has zero access to the user's personal Google Drive documents, photos, or sheets.
3. **User Isolation**: User A can never see or touch User B's files. Data isolation is enforced natively by Google's authentication infrastructure.
4. **OAuth Scope**: Requires only `https://www.googleapis.com/auth/drive.appdata` — a restricted, non-sensitive scope that grants access solely to the application data directory.
5. **Storage Quota**: Files count against the user's standard 15 GB free Google Drive quota. For CSVs, JSON data, and SQLite databases, 15 GB is virtually limitless.
6. **Zero Operational Costs**: Storage and egress are handled entirely by Google Drive; you pay \$0 in infrastructure costs.

---

## 4. The Recommended Hybrid Pattern: Local-First + Cloud Backup

```
[User Browser]
      │
      ├─► (1) Upload CSV / Input Data
      │         │
      │         ▼
      ├─► (2) Parse locally (Web Worker / PapaParse)
      │         │
      │         ▼
      ├─► (3) Save to IndexedDB (Instant, zero latency, offline ready)
      │         │
      │         ▼
      └─► (4) Optional "Sync with Google Drive"
                │
                ▼
          [Google Drive appDataFolder]
          (Encrypted / Serialized JSON backup)
```

1. **Immediate Local Access**: User uploads their file (e.g., CSV). It is parsed in-browser and indexed into IndexedDB. Querying and visualizations run at native hardware speeds.
2. **Cloud Sync on Demand**: When the user clicks **"Sign in with Google"** and **"Sync"**, the app uploads the serialized data blob directly to their `appDataFolder`.
3. **Restore on New Devices**: When visiting the tool from a new phone or laptop, the user signs in with Google, and the app detects and restores their database from `appDataFolder`.

---

## 5. Ready-to-Use Implementation Code

### A. Google Drive `appDataFolder` Client (JavaScript)

```javascript
/**
 * Client for managing user-scoped storage in Google Drive's appDataFolder.
 */
class GoogleDriveStorage {
  /**
   * Initializes the Google Drive storage client.
   * @param {string} clientId - The Google OAuth 2.0 Client ID.
   */
  constructor(clientId) {
    this.clientId = clientId;
    this.accessToken = null;
    this.tokenClient = null;
  }

  /**
   * Initializes the Google Identity Services token client.
   * @param {Function} onTokenReceived - Callback when access token is acquired.
   */
  init(onTokenReceived) {
    if (typeof google === 'undefined') {
      throw new Error('Google Identity Services SDK not loaded.');
    }

    this.tokenClient = google.accounts.oauth2.initTokenClient({
      client_id: this.clientId,
      scope: 'https://www.googleapis.com/auth/drive.appdata',
      callback: (tokenResponse) => {
        if (tokenResponse.error !== undefined) {
          throw tokenResponse;
        }

        this.accessToken = tokenResponse.access_token;
        if (onTokenReceived) {
          onTokenReceived(this.accessToken);
        }
      }
    });
  }

  /**
   * Triggers the Google Sign-in OAuth flow.
   */
  signIn() {
    if (!this.tokenClient) {
      throw new Error('Client not initialized. Call init() first.');
    }

    this.tokenClient.requestAccessToken({ prompt: 'consent' });
  }

  /**
   * Searches for a file by name inside appDataFolder.
   * @param {string} filename - The name of the file to search for.
   * @returns {Promise<string|null>} The file ID or null if not found.
   */
  async findFile(filename) {
    const query = encodeURIComponent(
      `name = '${filename}' and 'appDataFolder' in parents and trashed = false`
    );
    const url = `https://www.googleapis.com/drive/v3/files?spaces=appDataFolder&q=${query}&fields=files(id,name)`;

    const response = await fetch(url, {
      headers: { Authorization: `Bearer ${this.accessToken}` }
    });
    const data = await response.json();

    if (data.files && data.files.length > 0) {
      return data.files[0].id;
    }
    else {
      return null;
    }
  }

  /**
   * Saves or updates a JSON file inside appDataFolder.
   * @param {string} filename - Name of the file.
   * @param {object} payload - JavaScript object to store as JSON.
   * @returns {Promise<string>} The file ID.
   */
  async saveFile(filename, payload) {
    const existingId = await this.findFile(filename);
    const boundary = '-------314159265358979323846';
    const delimiter = `\r\n--${boundary}\r\n`;
    const closeDelim = `\r\n--${boundary}--`;

    const metadata = {
      name: filename,
      mimeType: 'application/json',
      parents: existingId ? undefined : ['appDataFolder']
    };

    const multipartRequestBody =
      delimiter +
      'Content-Type: application/json; charset=UTF-8\r\n\r\n' +
      JSON.stringify(metadata) +
      delimiter +
      'Content-Type: application/json\r\n\r\n' +
      JSON.stringify(payload) +
      closeDelim;

    let endpoint = 'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart';
    let method = 'POST';

    if (existingId) {
      endpoint = `https://www.googleapis.com/upload/drive/v3/files/${existingId}?uploadType=multipart`;
      method = 'PATCH';
    }

    const response = await fetch(endpoint, {
      method: method,
      headers: {
        Authorization: `Bearer ${this.accessToken}`,
        'Content-Type': `multipart/related; boundary=${boundary}`
      },
      body: multipartRequestBody
    });

    const result = await response.json();
    return result.id;
  }

  /**
   * Loads a JSON file's content by filename from appDataFolder.
   * @param {string} filename - The name of the file to load.
   * @returns {Promise<object|null>} The parsed JSON payload or null.
   */
  async loadFile(filename) {
    const fileId = await this.findFile(filename);
    if (!fileId) {
      return null;
    }

    const response = await fetch(
      `https://www.googleapis.com/drive/v3/files/${fileId}?alt=media`,
      {
        headers: { Authorization: `Bearer ${this.accessToken}` }
      }
    );

    return await response.json();
  }
}
```

---

### B. IndexedDB Local Storage Wrapper (JavaScript)

```javascript
/**
 * Lightweight IndexedDB wrapper for local-first persistence.
 */
class LocalDB {
  /**
   * @param {string} dbName - Name of the database.
   * @param {string} storeName - Name of the object store.
   */
  constructor(dbName = 'UtilAppDB', storeName = 'datasets') {
    this.dbName = dbName;
    this.storeName = storeName;
    this.db = null;
  }

  /**
   * Opens the IndexedDB database.
   * @returns {Promise<IDBDatabase>}
   */
  async open() {
    if (this.db) {
      return this.db;
    }

    return new Promise((resolve, reject) => {
      const request = indexedDB.open(this.dbName, 1);

      request.onupgradeneeded = (event) => {
        const db = event.target.result;
        if (!db.objectStoreNames.contains(this.storeName)) {
          db.createObjectStore(this.storeName, { keyPath: 'key' });
        }
      };

      request.onsuccess = (event) => {
        this.db = event.target.result;
        resolve(this.db);
      };

      request.onerror = (event) => {
        reject(event.target.error);
      };
    });
  }

  /**
   * Stores an item by key.
   * @param {string} key - Unique key.
   * @param {*} value - Serializable value.
   * @returns {Promise<void>}
   */
  async set(key, value) {
    const db = await this.open();
    return new Promise((resolve, reject) => {
      const tx = db.transaction([this.storeName], 'readwrite');
      const store = tx.objectStore(this.storeName);
      const req = store.put({ key, value, updatedAt: new Date().toISOString() });

      req.onsuccess = () => {
        resolve();
      };

      req.onerror = () => {
        reject(req.error);
      };
    });
  }

  /**
   * Retrieves an item by key.
   * @param {string} key - Unique key.
   * @returns {Promise<*|null>}
   */
  async get(key) {
    const db = await this.open();
    return new Promise((resolve, reject) => {
      const tx = db.transaction([this.storeName], 'readonly');
      const store = tx.objectStore(this.storeName);
      const req = store.get(key);

      req.onsuccess = () => {
        if (req.result) {
          resolve(req.result.value);
        }
        else {
          resolve(null);
        }
      };

      req.onerror = () => {
        reject(req.error);
      };
    });
  }
}
```

---

## 6. How to Have an AI Agent Spin Up a New Tool

When you want an AI agent to build a new tool for you (e.g., a "Games CSV Insights Analyzer"), use this prompt template:

### AI Agent Prompt Template
```markdown
Create a single-page client-side web application for analyzing CSV files of my game collection.

Requirements:
1. Pure static frontend (HTML, CSS, JavaScript) suitable for GitHub Pages or local browser execution.
2. Zero backend servers or databases.
3. Storage Architecture:
   - Use IndexedDB locally to cache parsed data for fast instant filtering, aggregation, and chart rendering.
   - Include an optional "Sync with Google Drive" button using Google Identity Services and the https://www.googleapis.com/auth/drive.appdata scope to save a backup to the user's hidden appDataFolder.
4. Input validation: Validate CSV headers, sanitize string fields, and handle malformed rows gracefully.
5. Provide actionable insights: Total games played, genres breakdown chart, completion rate, top-rated games, and search/filter table.
```

---

## 7. Setup in Google Cloud Console

1. Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a project named `Util-Tools` (or your preferred name).
3. Under **APIs & Services > Library**, enable the **Google Drive API**.
4. Under **APIs & Services > Credentials**, create an **OAuth 2.0 Client ID**:
   - Application type: **Web application**.
   - Name: `Util Static Client`.
   - Authorized JavaScript origins:
     - `http://localhost:4000` (for local development)
     - `https://<your-username>.github.io` (for GitHub Pages)
5. Copy your Client ID into your tool's configuration or prompt your AI agent to reference it safely.
