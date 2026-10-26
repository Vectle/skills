---
name: "pennylane-vqc-angle-embedding-strongly-baea68cd5ad46d8d"
description: "Shows how to fix pennyLane VQC: angle embedding, strongly entangling layers, gradient-based training. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_ol87h5Ui_kmhlP0jb9UYYg"
  title: "PennyLane VQC: angle embedding, strongly entangling layers, gradient-based training"
  version: "skv_BS78DjkyQzr4v6Fwajlx0w"
  updated: "2026-10-03T05:35:11.147602+00:00"
  canonical_url: "https://vectle.com/skills/skl_ol87h5Ui_kmhlP0jb9UYYg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.pennylane.ai/en/stable/\"]"
---

## TL;DR

``python import pennylane as qml from pennylane import numpy as np from sklearn.datasets import make\_moons from sklearn.model\_selection import train\_test\_split from sklearn.preprocessing import minmax\_scale n\_qubits = 2 n\_layers = 3 dev = qml.device("default.qubit", wires=n\_qubits) def circuit(weights, x): qml.AngleEmbedding(x, wires=range(n\_qubits)) qml.StronglyEntanglingLayers(weights, wires=range(n\_qubits)) return qml.expval(qml.PauliZ(0)) circuit = qml.QNode(circuit, dev) def variational\_classifier(weights, bias, x): # circuit output is in [-1, 1]; bias shifts the decision bound

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Variational Quantum Classifier in PennyLane

Binary classifier: `qml.AngleEmbedding` feature map, `qml.StronglyEntanglingLayers` ansatz, Pauli-Z expectation as the prediction, trained with a classical gradient optimizer. Tested pattern for PennyLane 0.33 and later on `default.qubit`.

## When to use this

- Building a hybrid quantum-classical binary classifier from scratch.
- Debugging a VQC whose loss does not decrease, whose gradients are None/zero, or that behaves differently with finite shots.

## End-to-end code

```python
import pennylane as qml
from pennylane import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import minmax_scale

n_qubits = 2
n_layers = 3

dev = qml.device("default.qubit", wires=n_qubits)

def circuit(weights, x):
    qml.AngleEmbedding(x, wires=range(n_qubits))
    qml.StronglyEntanglingLayers(weights, wires=range(n_qubits))
    return qml.expval(qml.PauliZ(0))

circuit = qml.QNode(circuit, dev)

def variational_classifier(weights, bias, x):
    # circuit output is in [-1, 1]; bias shifts the decision boundary
    return circuit(weights, x) + bias

def cost(weights, bias, X, Y):
    preds = [variational_classifier(weights, bias, x) for x in X]
    return np.mean((np.stack(preds) - Y) ** 2)

# weights shape for StronglyEntanglingLayers: (n_layers, n_wires, 3)
weights = np.random.uniform(0, 2 * np.pi, size=(n_layers, n_qubits, 3), requires_grad=True)
bias = np.array(0.0, requires_grad=True)

# data 2 features for 2 qubits; scale to radians for angle embedding
X, Y = make_moons(n_samples=200, noise=0.1, random_state=42)
Y = np.where(Y == 0, -1, 1)                      # labels must match expval range [-1, 1]
X = np.array(minmax_scale(X, feature_range=(0, np.pi)), requires_grad=False)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

opt = qml.GradientDescentOptimizer(stepsize=0.4)
batch_size, n_epochs = 32, 30
for epoch in range(n_epochs):
    perm = np.random.permutation(len(X_train))
    for i in range(0, len(X_train), batch_size):
        idx = perm[i:i + batch_size]
        weights, bias = opt.step(cost, weights, bias, X_train[idx], Y_train[idx])

def accuracy(weights, bias, X, Y):
    preds = [variational_classifier(weights, bias, x) for x in X]
    return np.mean(np.sign(np.stack(preds)) == Y)

print("train acc:", accuracy(weights, bias, X_train, Y_train))
print("test acc:", accuracy(weights, bias, X_test, Y_test))
```

Notes:

- `qml.AngleEmbedding(features, wires, rotation="X")` needs at most one feature per wire (features shape `(N,)` with `N` at most `n_qubits`); default rotation is RX, RY and RZ are options.
- `opt.step(cost, ...)` returns new parameters; assign them back. `opt.step_and_cost(cost, ...)` returns `(new_params, previous_cost)` if you want the cost for logging.
- Swap `qml.GradientDescentOptimizer` for `qml.AdamOptimizer(stepsize=0.1)` for adaptive steps. With the Torch interface use `torch.optim` instead and wrap the QNode in `qml.qnn.TorchLayer`.
- Default `diff_method="best"` resolves to backprop on `default.qubit` (a statevector simulator), so gradients here are exact analytic simulator gradients, not parameter-shift.

## Debugging gradient issue 1: parameter-shift requirements

- The analytic two-term shift rule needs each parametrized gate to be generated by an operator with two distinct eigenvalues (e.g. Pauli rotations RX, RY, RZ, which is what `AngleEmbedding` and `StronglyEntanglingLayers` decompose into). Default recipe: the gradient equals f(theta + pi/2) minus f(theta - pi/2), all divided by two.
- Operations without a defined shift recipe fall back to finite differences, silently. If gradients look wrong, check the op's `grad_recipe` attribute; `None` means the default two-term rule, not finite-diff.
- Parameter-shift costs 2 circuit evaluations per trainable parameter per gradient step, so gradient cost scales linearly with parameter count. On simulators prefer `diff_method="backprop"` (exact, cheaper) or `"adjoint"` (lower memory); both are simulator-only.

## Debugging gradient issue 2: non-differentiable ops and measurements

- `qml.sample` and `qml.counts` have no defined gradient under any interface or differentiation method. The QNode must return `qml.expval` (or `qml.probs`) for training.
- Only `requires_grad=True` arrays are differentiated. Create data with `requires_grad=False`; feeding plain sklearn arrays into an autograd-tracked cost raises `TypeError: float() argument must be a string or a number, not 'ArrayBox'`. Fix: `np.array(X, requires_grad=False)`.
- Loss stuck from the first step usually means zero gradients: verify weights were created with `requires_grad=True` and that you use the parameters returned by `opt.step` (the optimizer does not update in place).

## Debugging gradient issue 3: finite-shot noise

- Setting `shots` on the device, e.g. `qml.device("default.qubit", wires=n_qubits, shots=100)`, turns parameter-shift gradients into noisy estimators. `"backprop"` and `"adjoint"` do not work with finite shots at all; PennyLane docs direct you to parameter-shift instead.
- Levers, in order: increase shots, reduce the optimizer stepsize, run more epochs. For persistent noise use `qml.ShotAdaptiveOptimizer` (adapts the shot rate from parameter-shift gradient variances) or `qml.SPSAOptimizer` (stochastic approximation built for noisy cost evaluations).
- Isolate the cause: train once with `shots=None`. If it trains cleanly there, the problem is shot noise, not the architecture or the gradient method.

## Quick checklist

1. QNode returns `qml.expval` (never `qml.sample`/`qml.counts`).
2. `weights` has `requires_grad=True` and shape `(n_layers, n_qubits, 3)`; data has `requires_grad=False`.
3. Labels match the measurement range (-1/+1 for Pauli-Z expval).
4. Features scaled to radians (e.g. `(0, pi)`) for angle embedding.
5. Reassign `opt.step(...)` output; log with `opt.step_and_cost`.
6. Noisy training only with shots? Increase shots or switch to `ShotAdaptiveOptimizer`/`SPSAOptimizer`.


---

Source: [Vectle](https://vectle.com/skills/skl_ol87h5Ui_kmhlP0jb9UYYg). Version: `skv_BS78DjkyQzr4v6Fwajlx0w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
