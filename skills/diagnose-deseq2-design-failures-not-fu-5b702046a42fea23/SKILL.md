---
name: "diagnose-deseq2-design-failures-not-fu-5b702046a42fea23"
description: "Diagnose DESeq2 design failures: classify not-full-rank model matrices into linear-combination vs missing factor-level combinations using model.matrix and rankMatrix, fix constant variables and perfectly confounded covariates, set reference levels with relevel() before DESeq(), and resolve results()/lfcShrink() contrast errors via resultsNames()."
metadata:
  skill_id: "skl_XcK4fWsk8jrJB9aocjc_9A"
  title: "Diagnose DESeq2 design failures: not-full-rank model matrices and contrast errors"
  version: "skv_OZk9o5vBCwKVmRGmtE67uQ"
  updated: "2026-10-03T04:09:07.473167+00:00"
  canonical_url: "https://vectle.com/skills/skl_XcK4fWsk8jrJB9aocjc_9A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"http://bioconductor.org/packages/devel/bioc/vignettes/DESeq2/inst/doc/DESeq2.html\",\"https://support.bioconductor.org/p/9154407/\",\"https://support.bioconductor.org/p/87478/\"]"
---

# Diagnose DESeq2 design failures: not-full-rank model matrices and contrast errors

## TL;DR

When `DESeq()` fails with a not-full-rank model matrix, diagnose the cause from the matrix itself before changing the design: drop constant variables, drop or combine factor levels with empty cells, and remove perfectly confounded terms (no statistical fix exists for those). Set reference levels with `relevel()` before running `DESeq()`, and copy coefficient names verbatim from `resultsNames(dds)` for `results()` and `lfcShrink()`.

Use this when `DESeq(dds)` errors with a model-matrix complaint, or when
`results()` / `lfcShrink()` fail with contrast or coefficient errors. The
vignette section "Model matrix not full rank" names two distinct causes for the
fit error — diagnose which one applies from the model matrix itself before
changing the design.

**When not to use this skill:** the error is about dispersion estimation or outlier handling rather than the design matrix; you are using a different DE framework (edgeR, limma) with its own design diagnostics; the design fits but results look biologically wrong (that is a modeling question, not a rank problem).

## 1. Read the exact error

**Fit error (current DESeq2, from `checkFullRank`):**

```
Error in checkFullRank(modelMatrix) :
  the model matrix is not full rank, so the model cannot be fit as specified.
  One or more variables or interaction terms in the design formula are linear
  combinations of the others and must be removed.

  Please read the vignette section 'Model matrix not full rank':
  vignette('DESeq2')
```

**Fit error (older DESeq2, from `designAndArgChecker`):**

```
Error in designAndArgChecker(object, betaPrior) :
  full model matrix is less than full rank
```

**Constant design variable:**

```
Error: design contains one or more variables with all samples having the same value
```

All three mean the model matrix cannot be inverted. The vignette gives two
main reasons: (1) one or more columns are linear combinations of other columns,
or (2) levels of factors, or combinations of levels of multiple factors, have
no samples.

## 2. Build the model matrix and check its rank

Do not guess which cause applies — compute it:

```r
mm <- model.matrix(design(dds), as.data.frame(colData(dds)))
Matrix::rankMatrix(mm)[1]   # must equal ncol(mm); if lower, the matrix is rank-deficient
colnames(mm)                # inspect what the formula actually expanded to
```

A common source of confusion is that `colData(dds)` can silently contain NA or
wrong values: if the rownames of colData do not match the colnames of the count
matrix, `DESeqDataSetFromMatrix` can produce an object whose colData columns
are NA while the original data frame looks fine. Verify alignment first:

```r
stopifnot(identical(rownames(colData(dds)), colnames(counts(dds))))
```

## 3. Classify the cause from the colData cross-tabulation

**Cause A — constant variable.** A design column where every sample has the
same value contributes nothing. Check each design variable's levels:

```r
table(colData(dds)$condition)   # any variable with a single level is the culprit
```

Fix: drop the constant variable from the design.

**Cause B — empty cells in the cross-tabulation.** With multi-factor designs,
tabulate factor combinations:

```r
table(colData(dds)$batch, colData(dds)$condition)
```

A zero cell means a combination of levels has no samples — the corresponding
model-matrix column is all zeros. Fix options: drop the unpopulated levels with
`droplevels()`, or collapse to a single combined factor, e.g. replace
`~ batch + group` with `~ group` when all groups are unique per batch.

**Cause C — perfect confounding (linear combination).** The classic case:
`~ batch + condition` where every sample in batch 1 is condition A and every
sample in batch 2 is condition B. The batch columns are linear combinations of
the condition columns — e.g. groups nested in batches so that all samples of
groups 1-2 are in batch DMSO2 and all of groups 3-4 in batch DMSO1. Find the
aliased terms:

```r
alias(lm(rep(1, nrow(mm)) ~ mm - 1))$Complete   # or inspect alias(design)$Complete
```

When confounding is perfect, no analysis can separate the condition effect
from the batch effect — DESeq2's own guidance is to assume there is no batch
effect (which it deems unlikely) or rerun the experiment with conditions
balanced across batches. Practically, drop the confounded term (e.g. fit
`~ group` alone) and document the limitation.

**Cause D — interaction terms with missing combinations.** `~ genotype +
treatment + genotype:treatment` requires every genotype-by-treatment cell to
have samples. Same diagnosis as Cause B via the cross-tabulation; same fix.

## 4. After the fix: mind the reference level

`results()` uses the LAST variable in the design formula by default, and the
contrast direction follows the factor's reference level (alphabetical unless
changed). Set the reference BEFORE running `DESeq()` — changing levels
afterward does not rebuild the results tables:

```r
dds$condition <- relevel(dds$condition, ref = "untreated")
dds <- DESeq(dds)
res <- results(dds)   # tests treated vs untreated, the last design variable
```

## 5. Diagnose results() and lfcShrink() contrast errors

A separate failure class: the fit succeeded but coefficient extraction fails.
The names must match exactly. List the available coefficients:

```r
resultsNames(dds)
```

Then use the exact name:

```r
res <- results(dds, contrast = c("condition", "treated", "untreated"))
res <- lfcShrink(dds, coef = "condition_treated_vs_untreated", type = "apeglm")
```

The `coef` argument to `lfcShrink` must be an exact string from
`resultsNames(dds)` — a renamed or hand-typed coefficient errors. Note that
older tutorials mention `betaPrior=TRUE` in `DESeq()`; modern DESeq2 handles
log-fold-change shrinkage through `lfcShrink()` instead.

## Compatibility

- DESeq2 1.34+ (Bioconductor 3.14+). The `checkFullRank` error message is current; older versions report via `designAndArgChecker`.
- R 4.1+. `apeglm` needed for `lfcShrink(type="apeglm")`.

## Variant phrasings

- DESeq2 model matrix not full rank
- DESeq2 design matrix less than full rank
- DESeq2 contrast error resultsNames
- lfcShrink coef must be exact string

## 6. Checklist for the failing design

1. Reproduce the exact error text; note whether it is the fit error or a
   coefficient/contrast error.
2. Verify sample alignment: `rownames(colData(dds))` identical to
   `colnames(counts(dds))` — NA-filled colData is a silent variant of this bug.
3. Build `model.matrix(design(dds), colData(dds))`; check `rankMatrix` against
   `ncol`.
4. Classify: constant variable (drop it), empty cells in the cross-tabulation
   (drop levels / combine factors), perfect confounding (drop the confounded
   term; no statistical fix exists), missing interaction cells.
5. Set reference levels with `relevel()` before `DESeq()`, not after.
6. For `results()`/`lfcShrink()`, copy coefficient names from
   `resultsNames(dds)` verbatim.


---

Source: [Vectle](https://vectle.com/skills/skl_XcK4fWsk8jrJB9aocjc_9A). Version: `skv_OZk9o5vBCwKVmRGmtE67uQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
