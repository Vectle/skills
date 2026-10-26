---
name: "modulenotfounderror-no-module-named-ya-cc083d0fbcba917e"
description: "Fixes ModuleNotFoundError: No module named 'yaml' when importing PyYAML. Covers the pip name vs import name mismatch and the wrong-interpreter trap. Use when python cant find the yaml module after what looked like a good install. Not for yaml parse errors or Loader TypeErrors."
metadata:
  skill_id: "skl_nicWch2DE4YMGHyq7l694g"
  title: "ModuleNotFoundError: No module named 'yaml'"
  version: "skv_d4AQH0w7QYo7NcAlfeDOtQ"
  updated: "2026-10-03T05:57:53.374142+00:00"
  canonical_url: "https://vectle.com/skills/skl_nicWch2DE4YMGHyq7l694g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://pytutorial.com/how-to-solve-modulenotfounderror-no-module-named-yaml/\"]"
---

## TL;DR

The pip package is called PyYAML but you import it as yaml. Run pip install pyyaml, then import yaml works. If it still fails, youre installing into a different python than the one running your code, which is the cause nine times out of ten.

## The error

```text
ModuleNotFoundError: No module named 'yaml'
```

## Fix it

1. Run `pip install pyyaml` in the same environment that runs your code.
   Expected: pip prints Successfully installed PyYAML-x.y.z

2. Verify with `python -c "import yaml; print(yaml.__version__)"`.
   Expected: prints a version like 6.0.2 with no error

3. If it still fails, compare `which python` with `pip -V` (or `python -m pip install pyyaml` to force the right one).
   Expected: both point at the same environment; the import then works

## When this applies

- python raises ModuleNotFoundError: No module named 'yaml' on import yaml
- you ran pip install yaml or pip install PyYAML and it still fails

## When it does NOT apply

- yaml parses but throws errors (thats a content problem, not an install problem)
- TypeError about Loader (different skill, see the yaml.load Loader fix)

## Tool and version notes

PyYAML 5.x and 6.x, Python 3.8+. The import name has been yaml forever; the PyPI name is PyYAML (pip install is case-insensitive, pyyaml works).

## Other ways this shows up

### ModuleNotFoundError: No module named 'yaml' inside a virtualenv

The venv was created without system packages and PyYAML was installed globally. Activate the venv first, then pip install pyyaml inside it.

### ImportError: No module named yaml (older python wording)

Same fix. Python 3.6+ says ModuleNotFoundError, older versions say ImportError.

## Why it happens

PyPI distribution names and import names dont have to match, and here they dont: the project is PyYAML, the top-level module is yaml. pip install yaml installs a totally different stub package, which is why guessing the name fails.

## Edge cases

- On Debian/Ubuntu, apt install python3-yaml also works but gives you an older version.
- If youre on conda, conda install pyyaml avoids compiler hassles for the optional C loader.

---

Source: [Vectle](https://vectle.com/skills/skl_nicWch2DE4YMGHyq7l694g). Version: `skv_d4AQH0w7QYo7NcAlfeDOtQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
