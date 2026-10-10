---
name: "importerror-cannot-import-name-beautif-d646541a2d796004"
description: "Fixes the BeautifulSoup import failure where Python finds something called bs4 but the BeautifulSoup class is not inside it. Use when `from bs4 import BeautifulSoup` raises ImportError even though a bs4 package seems installed. Not for `No module named 'bs4'` (nothing installed) or FeatureNotFound parser errors."
metadata:
  skill_id: "skl_dRPHCrGBWWEcwy5bYYvk_Q"
  title: "ImportError: cannot import name 'BeautifulSoup' from 'bs4'"
  version: "skv_Z2P0fZVq-u-8WAGw-yD35Q"
  updated: "2026-10-03T05:59:57.100166+00:00"
  canonical_url: "https://vectle.com/skills/skl_dRPHCrGBWWEcwy5bYYvk_Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

This almost always means the thing Python found under the name bs4 is not really BeautifulSoup. Either you installed the stub `bs4` 0.0.1 package from PyPI (`pip install bs4` installs a dummy, not the library), or a file named `bs4.py` in your working directory is shadowing the real package. Run `pip uninstall bs4 -y` then `pip install beautifulsoup4`, and rename any `bs4.py` sitting next to your script. The import works right after.

## The error

```text
ImportError: cannot import name 'BeautifulSoup' from 'bs4'
```

## Fix it

1. **See what Python actually imported as bs4**

```
python -c "import bs4; print(bs4.__file__)"
```
Expected: a path inside site-packages ending in `bs4/__init__.py`. If it points at a `bs4.py` in your project folder, that file is shadowing the library and step 2 fixes it.

2. **Remove a shadowing bs4.py if there is one**

Check your script's folder for a file named `bs4.py` (and a `__pycache__` next to it) and rename it to anything else. Then re-run:
```
python -c "from bs4 import BeautifulSoup; print('ok')"
```
Expected: it prints `ok`. Python checks your script's directory before site-packages, so a stray file wins.

3. **Uninstall the stub, install the real library**

```
pip uninstall bs4 -y
pip install beautifulsoup4
```
Expected: `pip show beautifulsoup4` reports version 4.x, and `pip show bs4` reports nothing. The PyPI package literally named `bs4` is a 0.0.1 placeholder with no code in it.

4. **Confirm the import**

```
python -c "from bs4 import BeautifulSoup; print(BeautifulSoup('hi', 'html.parser').get_text())"
```
Expected: it prints `hi`.

## When this applies

- `from bs4 import BeautifulSoup` raises ImportError naming BeautifulSoup
- you (or a requirements file) once ran `pip install bs4` instead of `pip install beautifulsoup4`
- the import works in one folder but fails in another

## When it does NOT apply

- `ModuleNotFoundError: No module named 'bs4'` means nothing is installed at all, different fix
- `bs4.FeatureNotFound` means a parser like lxml is missing, not the class
- the ImportError names something other than BeautifulSoup

## Compatibility

beautifulsoup4 4.x on Python 3.6 and newer. The `pip install bs4` stub trap applies on every Python version because the dummy `bs4` 0.0.1 package is still published on PyPI.

## Variant phrasings

### `ImportError: cannot import name BeautifulSoup` (no quotes, no from-clause)

The same failure on Python 2 and early Python 3, which printed the old-style message without quotes. Same causes, same fix. Seen in the wild through `import mechanicalsoup`, whose own import chain runs `from bs4 import BeautifulSoup`.

## Why it happens

Two different things can answer to the name bs4. PyPI hosts a placeholder package literally named `bs4` (version 0.0.1) whose only purpose is telling you to install beautifulsoup4 instead, so `pip install bs4` gives you an empty package with no BeautifulSoup class in it. Separately, any `bs4.py` file in your working directory shadows the installed package, because Python looks in the script's directory before site-packages.

## Edge cases

- If `pip show bs4` prints version 0.0.1, that is the stub. Uninstall it.
- Jupyter users: restart the kernel after reinstalling. The old module object stays cached in a running kernel.
- A half-finished install can leave a broken `__init__.py` behind. `pip install --force-reinstall beautifulsoup4` clears that up.
- Check `pip list` inside the right environment. A venv that never got beautifulsoup4 installed fails the same way one folder over.


---

Source: [Vectle](https://vectle.com/skills/skl_dRPHCrGBWWEcwy5bYYvk_Q). Version: `skv_Z2P0fZVq-u-8WAGw-yD35Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
