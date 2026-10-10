---
name: "bs4-featurenotfound-couldn-t-find-a-tr-f72e8c87b4ed0e65"
description: "Fixes BeautifulSoup raising FeatureNotFound when you ask for the lxml tree builder and lxml is not installed. Use when the traceback names the lxml feature set. Not for `No module named 'bs4'` or for ImportError on the BeautifulSoup name itself."
metadata:
  skill_id: "skl_rsrAz9YmKV4Efr62gzPVrQ"
  title: "bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml"
  version: "skv_o1pwPBsrOuxuB8Ji7k4rEA"
  updated: "2026-10-03T06:10:22.684125+00:00"
  canonical_url: "https://vectle.com/skills/skl_rsrAz9YmKV4Efr62gzPVrQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

BeautifulSoup does not ship its own HTML parser. When you write `BeautifulSoup(html, 'lxml')` and lxml is not installed, you get FeatureNotFound instead of a soup. Install it with `pip install lxml` and the same line works. If you cannot install lxml, switch the second argument to `'html.parser'` (built into Python, no install needed) and move on.

## The error

```text
bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml
```

## Fix it

1. **Install lxml**

```
pip install lxml
```
Expected: pip reports `Successfully installed lxml-...`.

2. **Re-run your parse line unchanged**

```
python -c "from bs4 import BeautifulSoup; print(BeautifulSoup('hi', 'lxml').get_text())"
```
Expected: it prints `hi`. The line that raised now works because the requested tree builder exists.

3. **Alternative when you cannot install anything**

Change the parser argument to the built-in one:
```python
soup = BeautifulSoup(html, 'html.parser')
```
Expected: parsing works with no new installs. Slightly slower and more lenient than lxml, fine for most scraping.

## When this applies

- the traceback is `bs4.FeatureNotFound` and names `lxml`
- you passed `'lxml'`, `'lxml-xml'`, or `'xml'` as the parser argument
- a library you use (pandas read_html, for example) asks for lxml under the hood

## When it does NOT apply

- `ModuleNotFoundError: No module named 'bs4'` is a different problem (install beautifulsoup4)
- FeatureNotFound naming `html5lib` means install html5lib instead
- an ImportError on the BeautifulSoup name is the stub/shadowing problem

## Compatibility

All beautifulsoup4 4.x versions. lxml wheels exist for CPython 3.8+ on Windows, macOS, and Linux; on odd platforms you may need the libxml2 system libraries to build it.

## Variant phrasings

### `Couldn't find a tree builder with the features you requested: html5lib`

Same error, different parser. Fix is `pip install html5lib`, or switch to `'html.parser'`.

### `Couldn't find a tree builder with the features you requested: lxml-xml`

You asked for the XML tree builder. Same fix: `pip install lxml`.

## Why it happens

BeautifulSoup is a tree API, not a parser. The second argument to the constructor picks which installed parsing library does the actual work. If that library is not installed, BeautifulSoup cannot build the tree and raises FeatureNotFound. The message names exactly the feature set it looked for, so the fix is installing the named parser or picking one you have.

## Edge cases

- In a venv, make sure you pip-install into the same environment that runs the script.
- On Alpine/musl Linux there is no lxml wheel, so pip builds from source and needs libxml2-dev and libxslt-dev system packages.
- If lxml is installed but the error persists, you have two Pythons and installed into the wrong one. `python -m pip install lxml` targets the interpreter you run.


---

Source: [Vectle](https://vectle.com/skills/skl_rsrAz9YmKV4Efr62gzPVrQ). Version: `skv_o1pwPBsrOuxuB8Ji7k4rEA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
