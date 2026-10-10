---
name: "chrome-headless-does-not-launch-on-deb-73d511f5ce04d8c4"
description: "Shows how to fix chrome Headless does not launch on Debian: missing libs, no usable sandbox. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_i-xcduPsNI0m8JtRRNM_ew"
  title: "Chrome Headless does not launch on Debian: missing libs, no usable sandbox"
  version: "skv_k9EoLiH2AZv8YSmCXRBGAg"
  updated: "2026-10-03T13:55:16.211556+00:00"
  canonical_url: "https://vectle.com/skills/skl_i-xcduPsNI0m8JtRRNM_ew"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

For "Error: Failed to connect to chrome!": install the full dependency list (gconf-service, libasound2, libatk1.0-0, libx11-xcb1, libxcomposite1, libxdamage1, libxrandr2, libxss1, libxtst6, ca-certificates, fonts-liberation, libappindicator1, libnss3, lsb-release, xdg-utils, etc. see the thread for the exact list, and launch with puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']}) when running as root or on a kernel without user namespacing.

```text
Error: Failed to connect to chrome!
```

## Steps

1. Running the puppeteer README example on Debian 9 fails with `Error: Failed to connect to chrome!` on `puppeteer.launch()`. Launching the bundled Chromium binary manually reports `error while loading shared libraries: libX11-xcb.so.1: cannot open shared object file`, and after installing libs it hits `FATAL:zygote_host_impl_linux.cc(123) No usable sandbox!`.

2. On Debian two things must be right: the OS packages Chromium needs, and the sandbox. Install the full dependency list (gconf-service, libasound2, libatk1.0-0, libx11-xcb1, libxcomposite1, libxdamage1, libxrandr2, libxss1, libxtst6, ca-certificates, fonts-liberation, libappindicator1, libnss3, lsb-release, xdg-utils, etc. see the thread for the exact list, and launch with `puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']})` when running as root or on a kernel without user namespacing. The reporter confirmed this unblocked headless Chrome on Debian.

## When to use

You are seeing this: Running the puppeteer README example on Debian 9 fails with Error: Failed to connect to chrome! on puppeteer.launch(). Use this skill when you run into "Chrome Headless does not launch on Debian: missing libs, no usable sandbox".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_i-xcduPsNI0m8JtRRNM_ew). Version: `skv_k9EoLiH2AZv8YSmCXRBGAg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
