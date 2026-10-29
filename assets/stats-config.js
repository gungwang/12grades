/* Analytics configuration. If both values are empty, the site loads no analytics scripts and sends no analytics requests.
 * See the "Analytics" section of docs/pwa.md for configuration details. */
window.CNM_STATS = {
  // Cloudflare Web Analytics token. The beacon script loads only when this value is set.
  cloudflareToken: '',
  // Custom event collection endpoint (https://…). When set, events are sent as JSON POST requests with sendBeacon.
  endpoint: 'https://math-pansgo-stats.xiaokunfeng310.workers.dev/collect',
  // Optional callback, invoked once per event with { event, source, path, ts, ... }.
  onEvent: null
};
