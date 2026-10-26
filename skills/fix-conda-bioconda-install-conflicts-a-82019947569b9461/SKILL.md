---
name: "fix-conda-bioconda-install-conflicts-a-82019947569b9461"
description: "Shows how to fix conda / Bioconda install conflicts and solver failures. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_znu-CRkjOoYXQQL6BdzLeA"
  title: "Fix conda / Bioconda install conflicts and solver failures"
  version: "skv_2FU3th2ByExdlvgI4F0b9Q"
  updated: "2026-10-03T05:39:19.040286+00:00"
  canonical_url: "https://vectle.com/skills/skl_znu-CRkjOoYXQQL6BdzLeA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://www.biostars.org/p/9522705/\",\"https://www.biostars.org/p/470291/\",\"http://bioconda.github.io\",\"https://conda.github.io/conda-libmamba-solver/user-guide/\"]"
---

## TL;DR

For "Solving environment: failed with initial frozen solve. Retrying with flexible solve.": press CTRL-C to abort. ` hanging for a long time → the classic solver is struggling (class B), or a real conflict it will eventually report (class A). ` Your installed version is: 2.35 ` attached to a __glibc` complaint → the system glibc is too old for the requested builds (class A, system-level).

```text
Solving environment: failed with initial frozen solve. Retrying with flexible solve.
...
Found conflicts! Looking for incompatible packages.
This can take several minutes.  Press CTRL-C to abort.
```

## When to use

You are seeing this: The three signatures: `` UnsatisfiableError: The following specifications were found to be incompatible with each other: ` → a genuine version conflict (class A). ` Solving environment: failed with initial frozen solve. Use this skill when you run into "Fix conda / Bioconda install conflicts and solver failures".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

Use this when `conda install` or `conda create` with Bioconda packages fails
with `UnsatisfiableError`, hangs on `Solving environment`, or reports
`Found conflicts!`. These errors look alike but have four distinct causes with
different fixes. Classify from the exact error text FIRST, the fix for a
genuine version conflict is the opposite of the fix for a slow solver.

## 0. Read the error text, not just "it failed"

The three signatures:

```
UnsatisfiableError: The following specifications were found to be incompatible with each other:
```

→ a genuine version conflict (class A).

```
Solving environment: failed with initial frozen solve. Retrying with flexible solve.
...
Found conflicts! Looking for incompatible packages.
This can take several minutes.  Press CTRL-C to abort.
```

hanging for a long time → the classic solver is struggling (class B), or a
real conflict it will eventually report (class A).

```
Your installed version is: 2.35
```

attached to a `__glibc` complaint → the system glibc is too old for the
requested builds (class A, system-level).

## 1. Class A, genuine version conflict (`UnsatisfiableError`)

The solver is telling the truth: the requested combination cannot exist.
Common triggers seen on Biostars:

- **Installing into an existing environment** (especially `base`). The
 existing packages pin half the dependency tree. Almost every "conda error"
 thread is fixed the same way, install into a **fresh environment**:

 

```bash
  conda create -n sratools -c conda-forge -c bioconda sra-tools
  conda activate sratools
  ```

- **Over-pinned versions.** `samtools=1.9` on a new conda-forge stack fails
 because the old recipe's `libgcc-ng`/`libstdcxx-ng`/`zlib` pins collide with
 what modern python pulls in. Unless you have a hard reason for the old
 version, drop the pin and let the solver pick; then pin the *resolved*
 versions (`conda list --export`) for reproducibility.

- **Python version drift.** Bioconda currently builds for Python 3.10 3.13;
 old recipes expecting older Pythons conflict with the current stack.
 If you must have an old package, create the env with an old python
 explicitly (`conda create -n old -c conda-forge -c bioconda python=3.9
 [pkg]`) instead of fighting the default.

- **System glibc too old.** Errors naming `__glibc` (e.g. recipe needs
 `>=2.17` and the system reports something older) cannot be solved by
 channel juggling, you need a newer OS image or a container.

Do not "fix" class A by adding more channels or `--force`; that hides the
conflict until runtime.

## 2. Class B, solver hangs or crawls (no `UnsatisfiableError` yet)

The classic conda solver is slow on Bioconda's large dependency graph. Check
the solver first:

```bash
conda --version
```

- **conda 23.10 or newer**: the libmamba solver is already the default. If
 solving still hangs, it's probably a genuine conflict (class A), let it
 finish or Ctrl-C and read the report.
- **conda older than 23.10**: install the faster solver and make it default:

 

```bash
  conda update -n base conda
  conda install -n base conda-libmamba-solver
  conda config --set solver libmamba
  ```

 or use it for one command only:

 

```bash
  conda install -c conda-forge -c bioconda [pkg] --solver=libmamba
  ```

- **Alternative**: `mamba` / `micromamba` are drop-in replacements that use
 the same libsolv-based solver and the same channels:

 

```bash
  mamba create -n tools -c conda-forge -c bioconda samtools bcftools
  ```

## 3. Class C, wrong channel order / priority

Bioconda's documented setup (bioconda.github.io), order matters because
`conda config --add` **prepends**, so add in this exact sequence to end up
with conda-forge at highest priority:

```bash
conda config --add channels bioconda
conda config --add channels conda-forge
conda config --set channel_priority strict
```

Resulting priority (highest first): `conda-forge`, `bioconda`. Rationale from
the docs: Bioconda heavily depends on conda-forge, so conda-forge must win for
general-purpose libraries; `strict` priority "avoids cryptic errors" by
respecting that order during solving instead of mixing channels per package.

Diagnose: `conda config --show channels`, if `bioconda` outranks
`conda-forge`, or `channel_priority` is `flexible`/`disabled`, fix it with
the three commands above.

Without touching `.condarc`, pass the same policy per command (note: on the
command line, `-c` flags are read in *decreasing* priority order, the reverse
of `conda config`):

```bash
conda create -n myenv -c conda-forge -c bioconda --strict-channel-priority samtools bwa
```

## 4. Class D, environment YAML won't resolve

For `conda env create -f env.yml` conflicts:

1. Check the `channels:` list in the YAML, it must list `conda-forge`
 before `bioconda` (same priority rule as class C).
2. Loosen or drop version pins on the *tools* (`samtools`, `rsubread`);
 over-pinning transitive deps (`libgcc-ng=...`) is the usual culprit 
 remove them first, re-add only what still resolves.
3. Solve with mamba (`mamba env create -f env.yml`); its error messages name
 the conflicting chain more precisely than conda's.

## Quick decision tree

1. `UnsatisfiableError` → fresh env, drop pins, check python/glibc (class A).
2. Hangs at `Solving environment` / `Found conflicts!` → conda ≥23.10?
 yes: wait for the real report; no: libmamba solver (class B).
3. Worked before, fails now on a new machine → `conda config --show channels`;
 fix order to conda-forge > bioconda + strict priority (class C).
4. YAML create fails → channel order in YAML, unpin tools, solve with mamba (class D).
5. Never install bioinformatics tools into `base`; never "fix" a conflict with `--force`.

## Variants

Other phrasings of the same problem that show up in reports:

### UnsatisfiableError: The following specifications were found to be incompatible with each other:

```text
UnsatisfiableError: The following specifications were found to be incompatible with each other:
```


---

Source: [Vectle](https://vectle.com/skills/skl_znu-CRkjOoYXQQL6BdzLeA). Version: `skv_2FU3th2ByExdlvgI4F0b9Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
