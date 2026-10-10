---
name: "diagnose-ufl-aritymismatch-errors-in-f-a67671970bfac2b1"
description: "Shows how to fix diagnose UFL ArityMismatch errors in FEniCS: read the argument tuples first. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_YQrrQvNP_KC8Cq5MnDsYrw"
  title: "Diagnose UFL ArityMismatch errors in FEniCS: read the argument tuples first"
  version: "skv_bcB9XeaUaLYQ8chkdDRS5w"
  updated: "2026-10-03T05:09:28.534007+00:00"
  canonical_url: "https://vectle.com/skills/skl_YQrrQvNP_KC8Cq5MnDsYrw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

For "ufl.algorithms.check_arities.ArityMismatch: Failure to conjugate test function in complex Form": run the per-term Form(t).arguments() probe to confirm which term is odd. The two tuples come from two terms you added or multiplied together; the term whose tuple differs from the rest is the bug. L may only contain the test function and known data. - You built the bilinear form with a Function (the unknown, known data at assembly time) instead of a TrialFunction, then combined it with a term that does use TrialFunction.

```text
ufl.algorithms.check_arities.ArityMismatch: Failure to conjugate test function in complex Form
```

## When to use

You are seeing this: The error message names the two sides' form arguments, e.g. ('v\_0',) vs ('v\_0', 'v\_1'), and those tuples identify the bug directly. Use this skill when you run into "Diagnose UFL ArityMismatch errors in FEniCS: read the argument tuples first".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: e.g. 2019.1.0. If you are on something much newer or older, the details may have shifted.

Use this when form assembly or `solve()` dies with
`ufl.algorithms.check_arities.ArityMismatch`. The error message names the two
sides' form arguments, e.g. `('v_0',) vs ('v_0', 'v_1')`, and those tuples
identify the bug directly. Applies to both legacy FEniCS (DOLFIN, `dolfin`,
e.g. 2019.1.0) and FEniCSx (DOLFINx, `dolfinx` >= 0.6): UFL's arity checker is
shared, and the messages are identical. Do not mix the two solver APIs, but the
diagnosis below works for both.

## 1. Read the two argument tuples

Real messages seen on the FEniCS Discourse:

```
ufl.algorithms.check_arities.ArityMismatch:
  Adding expressions with non-matching form arguments ('v_0',) vs ('v_0', 'v_1').
```

```
ufl.algorithms.check_arities.ArityMismatch:
  Adding expressions with non-matching form arguments ('v_0',) vs ('conj(v_0)',).
```

```
ufl.algorithms.check_arities.ArityMismatch: Failure to conjugate test function in complex Form
```

```
ufl.algorithms.check_arities.ArityMismatch: Multiplying expressions with
  overlapping form arguments ('v_0', 'v_1') vs ('v_0',).
```

Notation: `v_0` is the argument numbered 0, by convention the **test**
function; `v_1` is argument number 1, the **trial** function. `conj(v_0)`
is the conjugated test function (complex mode). `v_0^1` means test function,
part 1 of a mixed space. The two tuples come from two terms you added or
multiplied together; the term whose tuple differs from the rest is the bug.

## 2. Classify the mismatch

Match your message to one of these patterns before editing anything.

**Pattern A: `('v_0',) vs ('v_0', 'v_1')`, a TrialFunction leaked into a linear form (or vice versa).**
One term contains a trial function the other terms don't. Usual causes:

- The linear form `L` contains a `TrialFunction`. `L` may only contain the
 test function and known data.
- You built the bilinear form with a `Function` (the unknown, known data at
 assembly time) instead of a `TrialFunction`, then combined it with a term
 that does use `TrialFunction`. A form built from `Function` has arity 1;
 from `TrialFunction` + `TestFunction` it has arity 2.

```python
# WRONG: first term has arity 2 (TrialFunction), second has arity 1 (Function)
u_trial, u_known = TrialFunction(V), Function(V)
a = inner(grad(u_trial), grad(v))*dx + inner(grad(u_known), grad(v))*dx
# RIGHT: the unknown is a TrialFunction everywhere in the bilinear form
u = TrialFunction(V)
a = inner(grad(u), grad(v))*dx
```

**Pattern B: `('v_0',) vs ('v_1',)` or two different `v_0` from different spaces, test functions from two different spaces in one form.**
You used test functions belonging to different function spaces, e.g. `v`
from `V` and `w` from `W`, in a single form. Either the problem genuinely
couples the spaces (use one `MixedElement` space and `TestFunctions(W)`)
or the terms belong in separate forms.

**Pattern C: `('v_0',) vs ('conj(v_0)',)` or "Failure to conjugate test function in complex Form", complex-mode conjugation.**
Your form is compiled for complex scalars (DOLFINx complex build) but you
multiplied a test function with plain `*` instead of `ufl.inner`, so one
side conjugates the test function and the other doesn't. Rule: in complex
mode, **always use `ufl.inner` for anything multiplied by a test or trial
function**, never bare `*`.

```python
# WRONG in complex mode: v appears both conjugated and not
F = v*f*dx + inner(grad(u), grad(v))*dx
# RIGHT
F = inner(v, f)*dx + inner(grad(u), grad(v))*dx
```

**Pattern D: `() vs (Argument(...),)`, a zero-arity term added to a form.**
One summand contains no form arguments at all: a stray scalar, a `Constant`
added directly to `F`, or an expression where every argument got substituted
away. Find the term and either give it its test function or move it out of
the form.

**Pattern E: "Multiplying expressions with overlapping form arguments", `test*test` or `trial*trial`.**
You multiplied two expressions that share an argument number, e.g. squaring
a form fragment like `(u*v)*(u*v)`, or `v*v*dx`. Restructure so each
multiplication combines at most one test-side and one trial-side factor.

**Pattern F: `('v_0^1', 'v_1^0') vs ('v_0^0', 'v_1^1')`, mixed-space parts inconsistent across terms.**
In a mixed form, one term was built with test/trial functions unpacked in a
different order than another term (common when combining `split()` pieces
with `TrialFunctions`/`TestFunctions` unpacked manually). Define each test
and trial function exactly once and reuse the same objects in every term.

## 3. Find the offending term mechanically

Don't eyeball a 40-term form. Print each term's arguments with UFL's own
introspection and diff them:

```python
import ufl
terms = {
    "diffusion": inner(grad(u), grad(v))*dx,
    "reaction":  c*u*v*dx,          # suspect term
    "source":    f*v*dx,
}
for name, t in terms.items():
    print(name, ufl.Form(t).arguments())
```

`Form.arguments()` returns the tuple of `Argument` objects UFL sees. The term
whose tuple differs from the intended arity (1 for `L`/`F`, 2 for `a`/`J`)
is the one to fix. This works unchanged in legacy `dolfin` and `dolfinx`.

## 4. The three rules that prevent recurrence

1. **One definition site per argument.** Create `TestFunction`/`TrialFunction`
 once per space and reuse; never create a second `TestFunction(V)` mid-form
 (a fresh `Argument` object compares unequal and triggers Pattern B/F).
2. **Arity by role:** residual/nonlinear form `F` and linear form `L` contain
 only test functions (arity 1); bilinear form `a` and Jacobian `J` contain
 trial + test (arity 2). For Jacobians prefer `J = derivative(F, u, du)`
 over hand-differentiation, a hand-written `J` with a wrong argument is
 the most common source of Pattern A.
3. **Complex builds: `inner`, always.** Any product involving a test or trial
 function uses `ufl.inner`; reserve `*` for scalar-times-scalar.

## 5. Checklist

1. Copy the two argument tuples from the error message.
2. Match to Pattern A F above.
3. Run the per-term `Form(t).arguments()` probe to confirm which term is odd.
4. Fix at the definition site (wrong object type, wrong space, missing
 `inner`), not by patching the sum.
5. Re-assemble; if a *different* arity error appears, repeat, large forms
 often contain two independent mistakes.


---

Source: [Vectle](https://vectle.com/skills/skl_YQrrQvNP_KC8Cq5MnDsYrw). Version: `skv_bcB9XeaUaLYQ8chkdDRS5w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
