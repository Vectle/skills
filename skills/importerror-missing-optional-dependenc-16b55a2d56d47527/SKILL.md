---
name: "importerror-missing-optional-dependenc-16b55a2d56d47527"
description: "Fixes ImportError: Missing optional dependency 'openpyxl'. Use pip or conda to install openpyxl. Use when pd.read_excel / ExcelFile / to_excel on .xlsx raises Missing optional dependency 'openpyxl' Not for: the file itself is missing (FileNotFoundError) or corrupt (BadZipFile)"
metadata:
  skill_id: "skl_4s2YnAYfM7aQJNdbIoDPxw"
  title: "ImportError: Missing optional dependency 'openpyxl'. Use pip or conda to install openpyxl."
  version: "skv_5CNIfjKUwunNPMGAfbi95A"
  updated: "2026-10-03T04:31:10.006494+00:00"
  canonical_url: "https://vectle.com/skills/skl_4s2YnAYfM7aQJNdbIoDPxw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://pythonfriday.dev/2025/04/274-working-with-excel-files-in-pandas/\"]"
---

# How to fix ImportError: Missing optional dependency 'openpyxl'. Use pip or conda to install openpyxl.

Install the Excel engine: `python -m pip install openpyxl`. pandas deliberately does not bundle Excel readers; `read_excel` on an .xlsx file needs openpyxl installed in the same environment. Use the exact same python/pip pair (`python -m pip`) so it lands in the right env.

## The exact error

```text
ImportError: Missing optional dependency 'openpyxl'. Use pip or conda to install openpyxl.
```

## Fix it

1. Run `python -m pip install openpyxl`.
   Expected: pip reports Successfully installed openpyxl

2. Retry `pd.read_excel('file.xlsx')`.
   Expected: returns a DataFrame, no ImportError

3. For legacy .xls files you need xlrd instead: `python -m pip install xlrd`.
   Expected: read_excel works on .xls

## When this applies

pd.read_excel / ExcelFile / to_excel on .xlsx raises Missing optional dependency 'openpyxl'

## When this does NOT apply

the file itself is missing (FileNotFoundError) or corrupt (BadZipFile)

## Versions

pandas >= 1.0 reading .xlsx

## Why it happens

Excel IO engines are optional dependencies; pandas raises a helpful ImportError telling you which one to install.

## Edge cases

xlrd >= 2.0 dropped .xlsx support, so do not 'fix' this by installing xlrd for an .xlsx file.


---

Source: [Vectle](https://vectle.com/skills/skl_4s2YnAYfM7aQJNdbIoDPxw). Version: `skv_5CNIfjKUwunNPMGAfbi95A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
