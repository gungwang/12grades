# App Phase 1: PWA, child profiles, and analytics hooks

## PWA

- `manifest.webmanifest`: app name, `display: standalone`, theme color `#0f6e62`, icons, and three shortcuts (diagnostics, knowledge graph, and child profiles). All paths are relative, so the site works at a domain root or in a subdirectory. `start_url` includes `?source=pwa`.
- Icons are in `assets/icons/`. `python3 scripts/make_pwa_icons.py` generates them from the site logo and colors (`#0f6e62`, `#dff3ef`): `icon-192.png`, `icon-512.png` (rounded corners), `icon-maskable-512.png` (with a safe zone), and `apple-touch-icon.png` (180 px, opaque, for iOS).
- `sw.js` (must be in the site root to control the entire site):
  - During installation, it precaches pages, scripts, stylesheets, icons, and `data/*.json` (about 6 MB, including a 3.7 MB question bank). Installation succeeds only when the app shell is complete; a data-cache failure does not block installation.
  - Pages and scripts use a network-first strategy (5-second timeout) and fall back to the cache offline, so online users receive the new version after deployment.
  - Data, icons, and the manifest use the cache first and update in the background; the next visit gets the new data.
  - When the cache list changes or an incompatible data-structure change is made, increment `VERSION` in `sw.js`. The old cache is deleted when the service worker activates.
  - Add every new page or script to the `SHELL` list in `sw.js` to make it available offline.
- Each page's `<head>` includes the manifest, apple-touch-icon, and theme-color. The page footer loads `assets/stats-config.js`, `assets/stats.js`, and `assets/pwa.js`. The service worker registers only over HTTPS or on localhost.
- Deployment: `scripts/deploy-cf.sh` already includes `sw.js`, `manifest.webmanifest`, and `children/` in the deployment package.

### Add-to-home-screen prompt (`assets/pwa.js`)

| Environment | Behavior |
|---|---|
| Android / desktop Chrome or Edge | Captures `beforeinstallprompt`; after about 1 second, a prompt appears at the bottom of the page. Select “Add” to open the system install dialog. |
| iOS Safari (including iPad) | There is no install API. The prompt button says “How to add” and opens an illustrated guide: Share → Add to Home Screen → Add. The prompt is not shown in Chrome, WeChat, or other in-app browsers on iOS because their steps differ. |
| Opened from a home-screen icon (`display-mode: standalone`, `navigator.standalone`) | No prompt is shown. |

After selecting “Not now,” selecting “Got it” after the guide, or selecting “Add,” the timestamp is saved in `localStorage` under `cnmPwa.dismissed.v1`, and the prompt no longer appears automatically. A footer link labeled “Add to Home Screen” remains available. When `appinstalled` fires, `cnmPwa.installed.v1` is written and the entry point is also hidden. Clear both keys to show the prompt again.

## Child profiles

- All data stays in the browser's `localStorage`; it is not uploaded. There are no accounts or cloud sync. Clearing browser data or switching devices removes access to the data.
- `cnmChildren.v1`: `{ current, children: [{ id, name, grade, textbook, createdAt }] }`; supports up to 8 profiles, and nicknames must be unique.
- `cnmChildren.records.v1`: `{ [childId]: [records] }`. A normal profile keeps its 40 most recent records. After merging a backup, profiles with more than 40 records retain their full history; later saves or moved records are not truncated to 40. Each record represents one diagnostic session; its fixed key format `学科|seed|目标` means `subject|seed|target`. A record includes the subject, scope name, number of questions answered, counts of weak / shaky / mastered / untested topics, their topic IDs, and root-cause IDs. Reopening the results page or correcting answers for the same session updates this record rather than adding another.
- Textbook edition is a note in the profile. The graph's topics and chapters follow the PEP edition; content is not filtered by edition.
- Diagnostic pages: the start, question, and results pages all let you switch the current child (or choose “Do not save to a profile”). The results page saves automatically to the current child's profile. Switching to another child moves the record as well. Demo mode (`demo=1`) does not save.
- `children/history.html`: filter by subject. “Topics that are still weak” combines all of a child's records, uses the latest result for each topic, lists root causes first, links each item to the knowledge graph, and offers a “Test again” action. Individual diagnostic records appear below; you can expand or delete them.

### Profile backup and restore across browsers

“Export all profiles” on the profile-management page downloads a `children-backup-*.json` file that includes the export time, all child profiles, the current-child selection, and all saved diagnostic records for every subject. The button is disabled when there are no profiles. Read or parse errors are shown, and no empty backup is created. Exporting does not modify local data or send profile data to a server.

Backup format:

```json
{
  "format": "12grades.children",
  "version": 1,
  "exportedAt": "2026-10-28T00:00:00.000Z",
  "profiles": {
    "v": 1,
    "current": "child-id",
    "children": [{ "id": "child-id", "name": "Xiaoman", "grade": "Grade 3", "textbook": "PEP Edition", "createdAt": "2026-10-01T00:00:00.000Z" }]
  },
  "records": { "child-id": [] }
}
```

`profiles` and `records` preserve the complete contents of `cnmChildren.v1` and `cnmChildren.records.v1`, respectively, including child IDs, creation times, record timestamps, subjects, scopes, and mastery-status fields. Topic names in history and weak-topic summaries can be recalculated from topic IDs and records, so they are not stored separately. Incomplete diagnostic sessions, diagnostic settings, seen questions, and visit analytics are not included in profile backups.

To switch browsers, select “Export all profiles” in the original browser, then choose “Import backup file” on the profile page in the new browser. The file is read in the browser and is not uploaded. Version 1 JSON backups are supported, up to 10 MB (UTF-8 BOM is supported). A preview appears after you choose a file. Data is saved only after you select “Confirm merge and import”; canceling writes nothing.

Merge rules:

- Same child ID: merge diagnostic histories, keeping the local nickname, grade, textbook edition, and creation time. Keep the existing current-child selection. If the browser has no profiles, restore the current-child selection from the backup.
- Same name but different IDs: keep both profiles and rename the imported one to something like “Nickname (imported),” while retaining its original ID. Reimporting matches by ID and does not create duplicates.
- Deduplicate diagnostic records by `key`. Use the later of `savedAt` and `updatedAt` to choose the newer result; if timestamps match, keep the local record. Keep records that exist on only one side, and do not truncate them if the merge exceeds 40 records.
- Stop importing if the merged set would exceed eight children; do not delete existing profiles. Malformed files, unknown versions, duplicate IDs or record keys, orphan records, invalid fields, and corrupted local data are not treated as empty data. Keep unknown topic IDs; the history page can fall back to displaying the ID.
- If local profiles change after the preview, preview again before confirming. On confirmation, write records first and profiles second. If the second write fails, restore the original records; if restoration also fails, show a separate error and do not report success. Resolve browser storage quota or permission problems before trying again.

The JSON file contains nicknames and learning records; keep it secure. Incomplete diagnostic progress and diagnostic settings are still excluded from backups.

Test the backup and restore logic with `node tests/test_children.js` (no third-party dependencies).

Browser migration test: `node tests/test_children_browser.js` (Node 22+, local Chrome/Chromium; set `CHROME` to specify its path). It uses isolated browser storage to download and import a backup, then checks restored history and weak topics, duplicate imports, conflict merging, stale previews, quota-failure rollback, and mobile layout. It does not access real user profiles; test files and screenshots are written to the system temporary directory.

## Analytics

**The repository previously had no analytics implementation** (the pages did not load analytics scripts or collect data). No account details are fabricated; this section documents configurable hooks that are empty by default, so pages send no analytics requests.

Configure them in `assets/stats-config.js`:

```js
window.CNM_STATS = {
  cloudflareToken: '',  // Cloudflare Web Analytics token; its beacon script loads only when this is set
  endpoint: '',         // Custom collection endpoint; when set, sendBeacon POSTs events to it
  onEvent: null         // Optional callback, called once per event
};
```

`assets/stats.js` provides `window.cnmTrack(name, props)`. Each event has this format:

```json
{ "event": "pageview", "source": "pwa", "path": "/diagnose/", "ts": "2026-10-22T12:00:00.000Z" }
```

- `source`: `pwa` means the app was opened from a home-screen icon (`display-mode: standalone` or iOS `navigator.standalone`); `web` means a normal web visit. The `start_url` in `manifest.webmanifest` also includes `?source=pwa`, so entry points can be distinguished from the URL parameter.
- Events: `pageview`, `pwa_launch` (the first open in a standalone session), `appinstalled`, `return_visit` (the local date differs from the previous visit; includes `days_since_first` and `visit_days`), `install_hint_shown`, `install_prompt_accepted` / `install_prompt_dismissed`, `ios_guide_opened`, `install_hint_closed`, and `child_added`.
- No personal information is collected, including child nicknames, grades, or answers. Events contain only the event name, source, page path (without query parameters), and timestamp. Return visits are determined from the first and most recent visit dates in local `localStorage` under `cnmStats.v1`; there is no user identifier.
- A `cnm:track` event is also dispatched on the same `window`, so other code can listen without modification.

How to connect analytics:
1. **For page views only**: Create a Web Analytics site in the Cloudflare dashboard and put its token in `cloudflareToken`. It tracks page views only and does not support custom events, so events such as `appinstalled` will not appear there.
2. **To distinguish PWA installs and return visits**: Set up a receiver (for example, a Cloudflare Worker that writes to D1 or Analytics Engine) and put its URL in `endpoint`. The request body is the JSON shown above, sent as `text/plain` to avoid a CORS preflight. The receiver can aggregate events by `event` and `source`.
3. **For another analytics service**: Forward events from `onEvent` or listen for `cnm:track`.

When `cloudflareToken` is set, pages request `static.cloudflareinsights.com`. In that configuration, the “no external requests” check in `scripts/screenshot.js` will fail; this is expected.

## Local verification

```bash
python3 -m http.server 8000   # The service worker can also register on localhost.
```

Open http://localhost:8000/ and inspect Manifest and Service Workers under DevTools → Application. Enable Offline and refresh; the knowledge graph, diagnostics, and profiles should all still open. The Android prompt appears only over HTTPS (or localhost) and when Chrome's installability criteria are met. To see the iOS guide, use Safari or an iPhone user agent.
