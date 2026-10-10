---
name: "firefox-and-edge-browser-not-launching-ddb59cdaba8f66a6"
description: "Fixes Selenium being unable to launch Firefox or Edge in a Linux container (Jenkins). Check how the browser binary is installed: the maintainer found Selenium Manager was resolving the /snap/bin/firefox symlink to /usr/bin/snap, which can't report a Firefox version. The fix was to stop resolving symlinks for browsers found in PATH, shipped in the next Selenium version. If your container installs browsers via snap, make sure Selenium Manager finds the real binary, or upgrade Selenium past that fi"
metadata:
  skill_id: "skl_22rwzjbQnLCbotpfjpRm_Q"
  title: "Firefox and Edge Browser not launching on a Jenkins Linux Container"
  version: "skv_3szpH08BQeZ4wmQgfotghw"
  updated: "2026-10-03T05:55:50.952314+00:00"
  canonical_url: "https://vectle.com/skills/skl_22rwzjbQnLCbotpfjpRm_Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

If Selenium can't launch Firefox or Edge in a Linux container, check how the browser binary is installed: the maintainer found Selenium Manager was resolving the /snap/bin/firefox symlink to /usr/bin/snap, which can't report a Firefox version.

1. If your container installs browsers via snap, make sure Selenium Manager finds the real binary.
2. Or upgrade Selenium past the fix (it stopped resolving symlinks for browsers found in PATH).
3. Expected: the browsers launch.

When to use: Firefox and Edge wont launch in a Jenkins Linux container (works on local Windows).

When not to use: local launches (different cause).

Compatibility: Selenium (fix shipped in the next version). Reported in SeleniumHQ/selenium#12495.

Variants:
- "selenium firefox container"
- "selenium manager snap"
- "selenium 12495"

Root cause: symlink resolution pointed Selenium Manager at /usr/bin/snap instead of Firefox.

Edge cases: the container not having the browsers pre-installed is a separate check; do that first.

---

Source: [Vectle](https://vectle.com/skills/skl_22rwzjbQnLCbotpfjpRm_Q). Version: `skv_3szpH08BQeZ4wmQgfotghw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
