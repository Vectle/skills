---
name: "fix-not-supported-on-device-deviceerro-54c38f6ebc955fbd"
description: "Shows how to fix 'not supported on device' DeviceErrors in PennyLane. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_UyDRQO4MMh4i3B-NVzhE1Q"
  title: "Fix 'not supported on device' DeviceErrors in PennyLane"
  version: "skv_8dmHPBD5foEX8sKAsEhWaQ"
  updated: "2026-10-03T05:08:10.590484+00:00"
  canonical_url: "https://vectle.com/skills/skl_UyDRQO4MMh4i3B-NVzhE1Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.pennylane.ai/en/stable/code/api/pennylane.devices.preprocess.validate_observables.html\",\"https://docs.pennylane.ai/en/stable/code/api/pennylane.devices.preprocess.decompose.html?highlight=qml%20devices%20preprocess%20decompose\",\"https://discuss.pennylane.ai/t/using-a-cv-circuit/1189\",\"https://docs.pennylane.ai/projects/strawberryfields/en/stable/devices/remote.html\"]"
---

## TL;DR

For "pennylane.exceptions.DeviceError": | Error pattern | What's rejected | Typical cause | |---|---|---| | Operator X(wires=[...]) not supported on device and does not provide a decomposition. (older versions: Gate X not supported on device...) | a gate | The device's native gate set lacks the op and PennyLane found no decomposition path, e.g.

```text
pennylane.exceptions.DeviceError
```

## When to use

You are seeing this: The error names which of the three was rejected, classify that first, then check the execution mode, before editing the circuit. Use this skill when you run into "Fix 'not supported on device' DeviceErrors in PennyLane".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Fix "not supported on device" DeviceErrors in PennyLane

Use this when executing a QNode raises `pennylane.exceptions.DeviceError`
saying an operator, observable, or measurement is not supported or not accepted
on the device. The error names which of the three was rejected, classify that
first, then check the execution mode, before editing the circuit.

## 1. Read the error, it tells you which of three things is rejected

| Error pattern | What's rejected | Typical cause |
|---|---|---|
| `Operator X(wires=[...]) not supported on device and does not provide a decomposition.` (older versions: `Gate X not supported on device ...`) | a gate | The device's native gate set lacks the op and PennyLane found no decomposition path, e.g. `DeviceError: Gate RX not supported on device default.gaussian` |
| `Observable ... not supported on device` | an observable inside `qml.expval`/`qml.var` | The observable is outside the device's accepted set |
| `Measurement ... not accepted for analytic simulation on device.` | the measurement type | The measurement is invalid in the current mode: `qml.state()`/`qml.density_matrix()` on hardware (simulator-only measurements), or sample-based measurements with `shots=None` |

## 2. Classify, then check the mode

- **Op rejected**: CV devices (`default.gaussian`) support only Gaussian
 operations, use `qml.Rotation` instead of `qml.RX`, or move the circuit to
 `default.qubit`. On hardware plugins, check the plugin's native gate set;
 PennyLane decomposes automatically when a decomposition exists, so this error
 means no decomposition path was found, swap in a natively supported
 equivalent rather than forcing the op.
- **Observable rejected**: rewrite the observable from supported pieces
 (e.g. a `qml.Hamiltonian`/`qml.LinearCombination` of Paulis on qubit devices)
 instead of a single unsupported observable.
- **Measurement rejected**: `qml.state()` and `qml.density_matrix()` are
 simulator-only, on hardware or remote devices (e.g. Strawberry Fields
 remote) they are rejected outright; use `qml.expval`, `qml.probs`, or
 `qml.sample` instead. Sample-based measurements (`qml.sample`,
 `qml.counts`) need finite shots: `qml.device("default.qubit", wires=2,
 shots=1000)`. Devices validate measurements differently for analytic
 (`shots=None`) vs finite-shot runs, so the same circuit can pass on one mode
 and fail on the other.

## 3. Diagnose before editing

```python
import pennylane as qml

specs = qml.specs(circuit)(params)   # device_name, gate counts, depth
print(specs["device_name"])
print(qml.draw(circuit, wire_order=dev.wires)(params))
```

`qml.specs` confirms which device actually executed the tape and breaks down
the gate set in use, the fastest way to spot the offending op before guessing.

## 4. Checklist for the failing execution

1. Copy the exact DeviceError; identify op / observable / measurement from the
 table in step 1.
2. Confirm the mode: `shots=None` (analytic) vs finite shots, acceptance
 rules differ between the two.
3. Op rejected: swap for a natively supported equivalent, or move to a more
 general device (`default.qubit`).
4. Measurement rejected: `qml.state()` means simulator only; sampling means
 set `shots`.
5. Re-run `qml.specs` after the change to confirm the fix, not just the
 absence of the error.


---

Source: [Vectle](https://vectle.com/skills/skl_UyDRQO4MMh4i3B-NVzhE1Q). Version: `skv_8dmHPBD5foEX8sKAsEhWaQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
