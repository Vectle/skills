---
name: "cannot-import-name-mutablemapping-from-9e99b8269fe65315"
description: "cannot import name 'mutablemapping' from 'collections' ImportError fails"
metadata:
  skill_id: "skl_rFDOebxOgzxZFxRplRzvcw"
  title: "cannot import name 'mutablemapping' from 'collections' ImportError fails"
  version: "skv_-pz2Y26byuLk7-Us1sSVfA"
  updated: "2026-11-07T01:53:59.783393+00:00"
  canonical_url: "https://vectle.com/skills/skl_rFDOebxOgzxZFxRplRzvcw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Find who does the old import.** Read the traceback to its last application or library frame and note the file and line doing the import from collections. Expected: you know if the code is yours or a dependencies.

**Fix your own code directly.** Change the import line to import the name from collections.abc instead of collections. Success check: that module imports cleanly on Python 3.10 or later.

**Upgrade a library that does it.** If the frame is inside site-packages, upgrade that package to a release that supports Python 3.10 or later, and pin the new minimum in your requirements. Expected: a fresh install in a clean virtualenv imports without the error.

**Use a shim only as a stopgap.** If an upgrade is blocked, assign the collections.abc names onto collections at the very start of your entry point, before the broken library imports. Success check: the app starts, and a ticket or comment records removing the shim after the upgrade.

**Search for the other moved names.** Search the codebase for imports of Mapping, Sequence, Iterable, Callable, Iterator, Hashable and MutableSequence from collections. Expected: all of them come from collections.abc.

**Verify in CI on the new Python.** Run the test suite on the target Python version, not just locally. Success check: collection and import of every test module pass with no ImportError.

---

Source: [Vectle](https://vectle.com/skills/skl_rFDOebxOgzxZFxRplRzvcw). Version: `skv_-pz2Y26byuLk7-Us1sSVfA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
