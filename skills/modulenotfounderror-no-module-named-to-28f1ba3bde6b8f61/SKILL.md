---
name: "modulenotfounderror-no-module-named-to-28f1ba3bde6b8f61"
description: "Fixes ModuleNotFoundError: No module named 'tokenizers' Use when transformers raises `No module named 'tokenizers'` or 'requires the Tokenizers library but it was not found' Not for: `No module named 'transformers'` (install transformers itself first)"
metadata:
  skill_id: "skl_j4GrDEsYFfVy5Oh3CwMY3A"
  title: "ModuleNotFoundError: No module named 'tokenizers'"
  version: "skv_4G9xbtLz1ehX8NZjDw2apg"
  updated: "2026-10-03T04:36:52.700429+00:00"
  canonical_url: "https://vectle.com/skills/skl_j4GrDEsYFfVy5Oh3CwMY3A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix ModuleNotFoundError: No module named 'tokenizers'

Install the missing Rust tokenizer backend: `python -m pip install tokenizers`. transformers needs it for every *Fast tokenizer (BertTokenizerFast etc.). Make sure you install into the same environment that runs the code: `python -m pip` with the python you actually use.

## The exact error

```text
ModuleNotFoundError: No module named 'tokenizers'
```

## Fix it

1. `python -m pip install tokenizers`
   Expected: Successfully installed tokenizers

2. `python -c "import tokenizers; print(tokenizers.__version__)"`
   Expected: prints a version

3. Retry your transformers import.
   Expected: works

## When this applies

transformers raises `No module named 'tokenizers'` or 'requires the Tokenizers library but it was not found'

## When this does NOT apply

`No module named 'transformers'` (install transformers itself first)

## Versions

any transformers with fast tokenizers

## Why it happens

Fast tokenizers are implemented in Rust in the separate `tokenizers` package; minimal installs skip it.

## Edge cases

conda users: `conda install -c conda-forge tokenizers` avoids Rust-toolchain build issues.


---

Source: [Vectle](https://vectle.com/skills/skl_j4GrDEsYFfVy5Oh3CwMY3A). Version: `skv_4G9xbtLz1ehX8NZjDw2apg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
