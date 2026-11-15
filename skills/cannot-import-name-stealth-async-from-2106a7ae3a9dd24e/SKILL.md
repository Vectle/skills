---
name: "cannot-import-name-stealth-async-from-2106a7ae3a9dd24e"
description: "cannot import name 'stealth_async' from 'playwright_stealth' ImportError fails"
metadata:
  skill_id: "skl_dO68cePrF4acJamlyDWRJg"
  title: "cannot import name 'stealth_async' from 'playwright_stealth' ImportError fails"
  version: "skv_eQlHu1jE_EVOAAQc3vIxFA"
  updated: "2026-11-15T01:53:31.836043+00:00"
  canonical_url: "https://vectle.com/skills/skl_dO68cePrF4acJamlyDWRJg"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Record the installed playwright-stealth version and the Python version, and confirm the import fails in a clean interpreter.

List the names exported by the installed playwright_stealth package.

Check the release notes or changelog for the version you upgraded to for the removal or rename of the async helper.

Update your code to import the current Stealth class and use its async apply method on the context or page, following the example for that exact version.

Remove any remaining imports of stealth_sync or stealth_async from tests, fixtures, and helper modules.

Reinstall from your lock file in a fresh virtual environment and run the import plus a minimal browser launch test.

If you must pin the old version briefly, record the pin, the reason, and a removal date, and do not mix old and new API calls in the same codebase.

---

Source: [Vectle](https://vectle.com/skills/skl_dO68cePrF4acJamlyDWRJg). Version: `skv_eQlHu1jE_EVOAAQc3vIxFA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
