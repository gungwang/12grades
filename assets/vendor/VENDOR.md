# Third-party graph libraries (bundled with the repository; pages do not access external CDNs)

The browser builds and licenses were copied unchanged from the official npm packages. Versions:

| File | Package | Version | License |
| --- | --- | --- | --- |
| `cytoscape.min.js` | [cytoscape](https://www.npmjs.com/package/cytoscape) | 3.30.4 | MIT; see `LICENSE-cytoscape.txt` |
| `dagre.min.js` | [dagre](https://www.npmjs.com/package/dagre) | 0.8.5 | MIT; see `LICENSE-dagre.txt` |
| `cytoscape-dagre.js` | [cytoscape-dagre](https://www.npmjs.com/package/cytoscape-dagre) | 2.5.0 | MIT; see `LICENSE-cytoscape-dagre.txt` |
| `qrcode.js` | [qrcode-generator](https://www.npmjs.com/package/qrcode-generator) | 2.0.4 | MIT; see `LICENSE-qrcode-generator.txt` |

`dagre.min.js` is the browser build published with dagre 0.8.5 (`dist/dagre.min.js`), and already bundles graphlib and lodash. graphlib and dagre are both licensed under MIT by Chris Pettitt; lodash is also MIT-licensed. These three libraries and `qrcode.js` (Kazuhiko Arase, MIT) are excluded from this repository's CC BY-NC license and retain their respective licenses. The diagnostic results page uses `qrcode.js` to draw the share-image QR code on a canvas; it does not request a generation API at runtime. jsQR 1.4.0 (Apache-2.0), used to decode QR codes in smoke tests, is in `scripts/vendor/` and is not loaded by the pages.

Pages reference these files only by relative paths. They do not fetch scripts, stylesheets, or fonts from npm, a CDN, or any other external domain at runtime.
