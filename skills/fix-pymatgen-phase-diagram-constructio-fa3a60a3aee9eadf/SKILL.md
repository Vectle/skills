---
name: "fix-pymatgen-phase-diagram-constructio-fa3a60a3aee9eadf"
description: "Shows how to fix pymatgen phase diagram construction errors. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_gkMAcOhJOSFPfyacgqWyJA"
  title: "Fix pymatgen phase diagram construction errors"
  version: "skv_SVOjfsPP_kOTysi7xIjI5g"
  updated: "2026-10-03T04:47:24.104056+00:00"
  canonical_url: "https://vectle.com/skills/skl_gkMAcOhJOSFPfyacgqWyJA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://matsci.org/t/constructing-convex-hull-and-pourbaix-diagrams-with-newly-calculated-data/46648\",\"https://matsci.org/t/fractions-of-decomposition-products/47047\",\"https://matsci.org/t/to-solve-the-error-typeerror-compoundphasediagram-object-is-not-iterable/40469\"]"
---

## TL;DR

For "TypeError: 'PhaseDiagram' object is not iterable": run every entry set through MaterialsProjectCompatibility().process\_entries() before PhaseDiagram. 0.60 BS2 + 0.40 BS instead of 0.50 BS2 + 0.50 BS for B2S3, this is by design. get\_decomp\_and\_e\_above\_hull returns coefficients on normalized compositions (one atom total): B2S3 is B0.4S0.6, and it decomposes to 0.60 of B0.333S0.667 (BS2) plus 0.40 of B0.5S0.5 (BS).

```text
TypeError: 'PhaseDiagram' object is not iterable
```

## When to use

You are seeing this: PhaseDiagram takes entries, not another diagram. Use this skill when you run into "Fix pymatgen phase diagram construction errors".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## 1. Classify the failure from the observable symptom

- **`TypeError: 'PhaseDiagram' object is not iterable`** (or the same for
 `CompoundPhaseDiagram`), you passed a phase diagram object where a list
 of entries belongs. `PhaseDiagram` takes entries, not another diagram.
 Typical cause: wrapping an existing `pd` in `PhaseDiagram(pd)`, or passing
 the output of a `CompoundPhaseDiagram` build into `ChempotDiagram` /
 `PhaseDiagram`. Fix the call site, not the data.
- **Hull missing phases you know exist, or all energies above hull are 0**
 , the entries were not compatibility-processed. Entries from
 `mpr.get_entries_in_chemsys` carry raw DFT energies plus the metadata
 (run type, Hubbard U, oxide/peroxide corrections) needed for the MP
 correction scheme; `PhaseDiagram` applies none of them itself.
- **`get_e_above_hull(entry)` disagrees with the website for one phase** 
 the entry under test and the hull entries come from different correction
 schemes (e.g. a website energy mixed with locally computed entries), or
 the hull was built from formation energies read off the site and re-fed
 as `PDEntry` energies (see step 4).
- **Decomposition coefficients look "wrong"**, e.g. `0.60 BS2 + 0.40 BS`
 instead of `0.50 BS2 + 0.50 BS` for B2S3, this is by design.
 `get_decomp_and_e_above_hull` returns coefficients on *normalized*
 compositions (one atom total): B2S3 is B0.4S0.6, and it decomposes to
 0.60 of B0.333S0.667 (BS2) plus 0.40 of B0.5S0.5 (BS). Multiply back out
 by the atom counts before comparing with a balanced equation.
- **Plot renders with phases floating off the hull lines**, stale energy
 mix, or a `CompoundPhaseDiagram` built without the right
 `terminal_compositions`. `CompoundPhaseDiagram(entries,
 terminal_compositions=[...])` pins the reference end-members; wrong
 terminal compositions silently re-reference every formation energy.

## 2. Always process entries before building the hull

This is the single most common cause of a wrong phase diagram, and it is
documented in the MP release notes and forum guidance:

```python
from mp_api.client import MPRester
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
from pymatgen.analysis.phase_diagram import PhaseDiagram

with MPRester() as mpr:
    raw_entries = mpr.get_entries_in_chemsys(["Li", "Co", "O"])

compat = MaterialsProjectCompatibility()
entries = compat.process_entries(raw_entries)
pd = PhaseDiagram(entries)
```

Notes:

- `process_entries` *drops* entries whose metadata is incompatible with the
 correction scheme (unknown run types, missing correction data). The
 returned list is shorter than the input, that is filtering, not data
 loss. If your phase of interest vanishes here, its entry metadata is the
 problem (check `entry.data` for run type and corrections).
- The hull is only meaningful over a complete chemical system: include the
 terminal elements. `get_entries_in_chemsys` fetches the full system, which
 is why it is the recommended entry source.
- Never mix MP entries with your own VASP entries unless the calculations
 used the same input parameters *and* the same correction scheme. Parse
 your VASP outputs with `Vasprun.get_computed_entry()` from
 `pymatgen.io.vasp.outputs`, then apply the matching compatibility class
 to both sets together.

## 3. Read hull energies off the diagram, not the entry

`entry.energy_per_atom` is a total DFT energy per atom; `e_above_hull` is a
hull property. The supported read pattern:

```python
entry_of_interest = next(
    e for e in entries if e.entry_id == "mp-19128"
)
pd = PhaseDiagram(entries)
print(pd.get_e_above_hull(entry_of_interest))        # eV/atom
print(pd.get_form_energy_per_atom(entry_of_interest)) # formation energy
decomp, e_above = pd.get_decomp_and_e_above_hull(entry_of_interest)
```

`stable_entries` gives the hull vertices; `pd.all_entries` gives
everything that went into the construction. For ternary and quaternary
systems, `PDPlotter(pd, show_unstable=True)` labels the unstable phases
with their hull distances, build the plot *after* confirming the hull
list is complete, since plotting a partial hull misleads silently.

## 4. Two traps when round-tripping website data

1. **Rebuilding from website formation energies is lossy.** Users who copy
 the "13 stable phases" and their formation energies off the MP site into
 `PDEntry(composition, energy)` entries get a different hull, because
 `PhaseDiagram` treats `PDEntry.energy` as a *total* energy, not a
 formation energy, and the convex-hull reference frame is reconstructed
 from the entries you supply. If you must hand-build entries, supply
 total energies with the same reference as the hull, or accept a
 different (often wrong) result.
2. **`CompoundPhaseDiagram` dummy entries need to win the hull.**
 Injecting `PDEntry(composition, energy)` for a composition not in MP
 only shows up if its energy puts it on or near the hull (within the
 `show_unstable` window of the plotter). An energy of 0 almost never
 qualifies; the phase is silently absent, not erroring.

## Checklist for a wrong-looking phase diagram

1. Read the symptom: TypeError (wrong constructor input), missing hull
 phases (unprocessed entries), wrong coefficients (normalization, not a
 bug), re-referenced energies (wrong terminals).
2. Run every entry set through `MaterialsProjectCompatibility()`
 `.process_entries()` before `PhaseDiagram`.
3. Confirm the hull contains the terminal elements and your phase of
 interest survived filtering.
4. Read energies with `get_e_above_hull` / `get_decomp_and_e_above_hull`
 on the diagram object; never trust `entry.energy` alone.
5. Plot only after the hull list is confirmed complete.


---

Source: [Vectle](https://vectle.com/skills/skl_gkMAcOhJOSFPfyacgqWyJA). Version: `skv_SVOjfsPP_kOTysi7xIjI5g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
