---
name: "diagnose-and-fix-xr-open-mfdataset-com-8783b1068b328119"
description: "Diagnose xr.open_mfdataset failures from the error message and file layout: classify nested vs by_coords vs merge, resolve MergeError 'conflicting values' with compat/compat_attrs/preprocess, and pin data_vars/compat explicitly against the 2025.x default-change FutureWarnings."
metadata:
  skill_id: "skl_2AggVyXwgKrC0WiXt2Ge_A"
  title: "Diagnose and fix xr.open_mfdataset combine failures (MergeError, compat, defaults)"
  version: "skv_vZ1fcbagWlkKSD2j9x_CKQ"
  updated: "2026-10-03T05:31:45.515101+00:00"
  canonical_url: "https://vectle.com/skills/skl_2AggVyXwgKrC0WiXt2Ge_A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Diagnose and fix `open_mfdataset` combine failures

## TL;DR

Diagnose xr.open_mfdataset failures from the error message and file layout: classify nested vs by_coords vs merge, resolve MergeError 'conflicting values' with compat/compat_attrs/preprocess, and pin data_vars/compat explicitly against the 2025.x default-change FutureWarnings.

Use this when `xr.open_mfdataset` raises `MergeError: conflicting values for variable
'...' on objects to be combined`, silently drops variables you expected, or emits
`FutureWarning`s about `data_vars` / `compat` defaults. Almost every failure is one
of a small set of combine misconfigurations, and this procedure identifies which
one from the error message and your file layout before you change anything.

**When not to use this skill:** a single file opens fine with `xr.open_dataset` (no combine involved); the error is a missing file or permission problem rather than a merge conflict; you are combining in-memory datasets (use `xr.merge`/`xr.concat` directly, not `open_mfdataset`).

## 1. Read the exact error or warning

The two dominant failure signatures:

```
xarray.core.merge.MergeError: conflicting values for variable 'lon_bnds' on
objects to be combined. You can skip this check by specifying compat='override'.
```

```
FutureWarning: In a future version of xarray the default value for data_vars
will change from data_vars='all' to data_vars='minimal'. ... To opt in to new
defaults and get rid of these warnings now use
`set_options(use_new_combine_kwarg_defaults=True)` or set data_vars explicitly.
```

A parallel `FutureWarning` exists for `compat` (`'no_conflicts'` → `'override'`).
These warnings are real breaking-change previews: pick your side explicitly now
rather than letting a future xarray release change your results silently.

## 2. Classify the file layout first

Your choice of `combine` follows the geometry of the file set, not the error:

- **Time slices along an existing dimension** (each file holds `time: 365` for a

different year, same lat/lon grid): use `combine='nested'` with an explicit
  `concat_dim`:

  ```python
  ds = xr.open_mfdataset(
      "model_*.nc",
      combine="nested",
      concat_dim="time",
      data_vars="minimal",   # only concat variables that actually span time
      coords="minimal",      # same for coordinates
  )
  ```

`data_vars='minimal'` concatenates only variables that contain the concat
  dimension. Everything else (static fields, bounds variables) goes through the
  `compat` check instead of being needlessly concatenated. This is the
  forward-compatible choice for time-slice archives.

- **Files that tile different coordinate values** (different lat/lon boxes, or

irregularly named files whose order you don't trust): use `combine='by_coords'`
  (this is `open_mfdataset`'s default). xarray orders the files by their
  coordinate values, ignoring filename order.

- **Neither** (files overlap in coordinates but hold different variables, e.g.

one file per variable): that is a merge job, not a combine job. Open each with
  `xr.open_dataset` and use `xr.merge` instead.

Note: passing `concat_dim` together with `combine='by_coords'` is an error
(`combine_by_coords` takes no `concat_dim`), and has been a hard error rather
than a warning since xarray 2023.11.0.

## 3. Classify the conflicting variable

The `MergeError` names one variable. Open two files individually and compare:

```python
a = xr.open_dataset("file_0000.nc")
b = xr.open_dataset("file_0001.nc")
print(a["lon_bnds"].identical(b["lon_bnds"]))  # False → the values genuinely differ
print(a["lon_bnds"].values.ravel()[:5], b["lon_bnds"].values.ravel()[:5])
```

- **A genuinely static field that differs trivially between files** (bounds

variables like `lon_bnds`/`lat_bnds`, orography, `surface_altitude` recomputed
  with slightly different rounding): the equality check is stricter than you
  need. Pass `compat='override'` — xarray takes the first file's value and
  moves on. The error message itself suggests this.

- **A coordinate that differs because files genuinely cover different tiles**:

you want `combine='by_coords'`, not `compat='override'` — overriding would
  silently keep the wrong grid for later files.

- **A data variable that should have been concatenated but wasn't**: you passed

(or defaulted to) `data_vars='minimal'` and the variable doesn't span the
  concat dim, or the concat dim name differs between files (e.g. `Time` vs
  `time`). Fix the dim, don't relax compat.

- **Global attributes conflicting**: those are governed by `combine_attrs`

(`'drop'` | `'identical'` | `'no_conflicts'` | `'override'`), not `compat`.
  `open_mfdataset` reads global attrs from the first file by default; override
  with the `attrs_file` argument if a specific file is authoritative.

## 4. Normalize files with `preprocess` before combining

`preprocess` runs on each per-file dataset *before* any combining logic, so it
is the right place to make heterogeneous files uniform:

```python
def _clean(ds):
    # drop per-file noise that must not participate in combine decisions
    ds = ds.drop_vars(["surface_altitude"], errors="ignore")
    # normalize an inconsistent time encoding across files
    return ds

ds = xr.open_mfdataset(
    "model_*.nc",
    combine="nested",
    concat_dim="time",
    data_vars="minimal",
    coords="minimal",
    compat="override",
    preprocess=_clean,
)
```

Two common preprocess jobs:

1. **Inconsistent time decoding**: if some files decode `time` to

`datetime64` and others to `CFTimeIndex` (non-standard calendar, or dates
   outside the ns range), decode uniformly in `preprocess` — either all with
   `decode_times=False` plus a manual `xr.decode_cf` with
   `xr.coders.CFDatetimeCoder(time_unit=...)`, or force everything to cftime.

2. **Conflicting non-dimension coordinates**: drop or rename them here rather

than widening `compat` globally, so the strict check still protects your
   real data variables.

## 5. Opt in to the new combine defaults explicitly

Recent xarray (2025.x) emits `FutureWarning`s announcing new defaults for the
combine kwargs used by `open_mfdataset`, `concat`, `merge`, and `combine_*`:

- `data_vars`: `'all'` → `'minimal'`
- `compat`: `'no_conflicts'` → `'override'`

Two ways to silence them, with different semantics:

```python
# Option A: pin the behavior you actually want, per call
ds = xr.open_mfdataset(paths, data_vars="minimal", compat="override", ...)

# Option B: adopt all new defaults at once for the session
with xr.set_options(use_new_combine_kwarg_defaults=True):
    ds = xr.open_mfdataset(paths, ...)
```

Option A is explicit and survives across xarray upgrades; Option B is for
auditing what the future behavior will do to your pipeline. If your code runs
with warnings-as-errors in CI, do one of these — do not filter the warnings.

## Compatibility

- xarray 2023.x–2025.x. The `FutureWarning`s about `data_vars`/`compat` defaults apply to 2025.x; pin explicitly to lock behavior.
- NetCDF4, Zarr, and GRIB via cfgrib all work with `open_mfdataset`; GRIB needs `engine='cfgrib'` and `backend_kwargs`.

## Variant phrasings

- xarray open_mfdataset MergeError conflicting values
- xr.open_mfdataset compat override vs no_conflicts
- open_mfdataset FutureWarning data_vars minimal
- xarray combine nested vs by_coords

## 6. Checklist for the failing call

1. Reproduce with two individual files: open them with `xr.open_dataset` and

compare the conflicting variable — is the difference real data or file noise?

2. Classify the layout: time slices → `combine='nested', concat_dim=[dim]`;

tiles/irregular names → `combine='by_coords'`; different variables per
   file → `xr.merge`, not `open_mfdataset`.

3. Set `data_vars='minimal'` / `coords='minimal'` for concat layouts so static

fields stop being concatenated.

4. `compat='override'` only for fields you have verified are static;

`combine_attrs` for attribute conflicts, `attrs_file` for authoritative
   global attrs.

5. Put normalization (drop noise vars, uniform time decoding) in `preprocess`.
6. Pin `data_vars` and `compat` explicitly to silence the FutureWarnings and

lock behavior across upgrades.


---

Source: [Vectle](https://vectle.com/skills/skl_2AggVyXwgKrC0WiXt2Ge_A). Version: `skv_vZ1fcbagWlkKSD2j9x_CKQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
