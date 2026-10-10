---
name: "modulenotfounderror-when-simultaneousl-2789aabdb8ea85ac"
description: "Fixes ModuleNotFoundError when deployed Prefect flows run concurrently from a custom image by upgrading to Prefect 3.2.14 or newer, where flow loading is thread-safe. Use when simultaneous flow runs clash on imports. Not for missing dependencies in the image itself."
metadata:
  skill_id: "skl__J2_ZrmMkiuu6DS9QQERfg"
  title: "ModuleNotFoundError when simultaneously running deployed flows using custom image"
  version: "skv_ek5cP7GboQ9UTFbsL4Xgsg"
  updated: "2026-10-03T04:38:52.369273+00:00"
  canonical_url: "https://vectle.com/skills/skl__J2_ZrmMkiuu6DS9QQERfg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

Fix first: upgrade to Prefect >= 3.2.14. The flow loader was not thread-safe in older versions; PR #16458 (v3.1.9) added a threading lock and unique module names, and PR #17524 (v3.2.14) uses real script filenames as module names and keeps modules in sys.modules.

```text
ModuleNotFoundError when simultaneously running deployed flows using custom image
```

1. Upgrade with `pip install "prefect>=3.2.14"`.
2. Rebuild your custom image with the new Prefect version and redeploy. Expected: simultaneous flow runs each resolve their own imports, no more ModuleNotFoundError.

When to use: deployed Prefect flows crash with ModuleNotFoundError only when several run at the same time.

When not to use: a single flow run fails with ModuleNotFoundError (that is a missing package in your image, not this bug), or flows running on stock images.

Compatibility: Prefect >= 3.2.14 (partial fix in 3.1.9). Custom deployment images.

Variants:
- "prefect concurrent flows ModuleNotFoundError"
- "prefect custom image simultaneous runs import error"
- "prefect load_script_as_module thread safe"

Root cause: load_script_as_module was not thread-safe. It shared the '__prefect_loader__' module name, modified sys.path without locking, and evicted modules from sys.modules after loading, so concurrently loading flows interfered with each other's imports.

Edge cases: if you pinned an older Prefect for other reasons, 3.1.9 has the lock and unique names but not the real-filename module names. 3.2.14 is the fully fixed version.

---

Source: [Vectle](https://vectle.com/skills/skl__J2_ZrmMkiuu6DS9QQERfg). Version: `skv_ek5cP7GboQ9UTFbsL4Xgsg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
