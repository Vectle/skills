---
name: "dotnet-error-in-4-11-0-when-using-chro-0f402bcc2f77a490"
description: "Shows how to fix dotnet Error in 4.11.0 when using ChromeDriverService.CreateDefaultService(). Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_ymQDUKEIRPDYG4QMBjjpcQ"
  title: "Dotnet Error in 4.11.0 when using ChromeDriverService.CreateDefaultService()"
  version: "skv_pMD8gkG8tzHVReSjjyR6OA"
  updated: "2026-10-03T14:38:20.158763+00:00"
  canonical_url: "https://vectle.com/skills/skl_ymQDUKEIRPDYG4QMBjjpcQ"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

For "Unable to obtain chrome using Selenium Manager": what works: Upgrade to Selenium 4.12 or newer. In 4.11 the.NET Service constructor treated a path without a trailing slash as a file instead of a directory, which broke ChromeDriverService.CreateDefaultService(); that was fixed for 4.12.

```text
Unable to obtain chrome using Selenium Manager
```

## Steps

1. What works:
Upgrade to Selenium 4.12 or newer. In 4.11 the .NET `Service` constructor treated a path without a trailing slash as a file instead of a directory, which broke `ChromeDriverService.CreateDefaultService()`; that was fixed for 4.12. From 4.11 on, you also do not need to manage drivers yourself: drop the manual service creation and let Selenium Manager download the driver.

2. If you unpack the NuGet by hand for PowerShell use, keep the layout intact: `selenium-manager.exe` goes in `selenium-manager/windows/` next to `Selenium.WebDriver.dll`, and dependency DLLs like `Newtonsoft.Json` must sit beside the WebDriver DLL. A user confirmed the exact failing script worked after these fixes.

## When to use

You are seeing this: What was reported: Issue SeleniumHQ/selenium#12564 (closed, 46 comments): ### What happened? Use this skill when you run into "Dotnet Error in 4.11.0 when using ChromeDriverService.CreateDefaultService()".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 4.11.0, 4.10.0. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://www.nuget.org/packages/Selenium.Support/

- https://www.nuget.org/packages/Selenium.WebDriver


---

Source: [Vectle](https://vectle.com/skills/skl_ymQDUKEIRPDYG4QMBjjpcQ). Version: `skv_pMD8gkG8tzHVReSjjyR6OA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
