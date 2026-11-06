# Platform constraints checked against current documentation

**Verified source retrieval:** official Tauri repository and MDN documentation fetched through the configured HTTPS proxy on 2026-11-06. URLs and SHA-256 contents in [source manifest](../research/results/platform_sources.json). This verifies what those retrieved documents say, not this game's platform operation. Branch URLs are mutable; hashes identify the retrieved versions.

|Source|Supported finding|Implementation consequence|
|---|---|---|
|[Tauri prerequisites](https://raw.githubusercontent.com/tauri-apps/tauri-docs/v2/src/content/docs/start/prerequisites.mdx)|Windows development needs Microsoft C++ Build Tools, WebView2 and Rust; MSI tooling has additional requirements|Build on Windows with explicit prerequisites; player must not install developer tools. Test installer WebView runtime provisioning including offline path|
|[MDN PWA installability](https://raw.githubusercontent.com/mdn/content/main/files/en-us/web/progressive_web_apps/guides/making_pwas_installable/index.md)|Installation needs HTTPS or local development origin; iOS installation uses Share menu; beforeinstallprompt custom prompt is not supported on iOS|Do not ship a Chromium-only install button as the iPhone install flow. First installation/download needs network; cache assets for subsequent offline play|
|[MDN quotas and eviction](https://raw.githubusercontent.com/mdn/content/main/files/en-us/web/api/storage_api/storage_quotas_and_eviction_criteria/index.md)|IndexedDB/Cache storage is best-effort by default; persist requests can be denied; quota writes can fail; browser/embedded WebKit policies differ|Handle QuotaExceededError, estimate usage, request persistence where supported, keep export/import and last known-good generation. Do not promise permanent local browser saves|

The retrieved MDN documents distinguish iOS versions and browser engines; avoid a universal storage-size promise or treating a quota fraction as available free disk. No iPhone or Windows machine is attached for runtime/package validation here. Linux Python performance does not establish WebView, browser or phone performance.

**Plausible but unverified recommendation:** TypeScript/Vite shared core with workers and accessible UI, then compare Tauri and Electron through measured Windows spikes. A PWA uses browser installation, not Tauri's native iOS build pipeline. App Store packaging is out of initial scope and unnecessary for the requested installable PWA.

**Required next tests:** actual Windows install on clean VM and offline launch; actual iPhone Share-menu installation, airplane-mode play/relaunch, suspension, service-worker update boundary, quota error, backup export/import and recovery after force-close. Record OS/browser/model and all observed failures. These are outstanding, not passed checks.
