---
name: "diagnose-and-fix-ddp-nccl-distributed-03a31123a149a892"
description: "Diagnose a hanging PyTorch DistributedDataParallel job: classify startup rendezvous failure vs mid-training collective mismatch vs conditional eval collectives, instrument with a short process-group timeout and TORCH_DISTRIBUTED_DEBUG/TORCH_NCCL_BLOCKING_WAIT, then fix the collective sequence mismatch (conditional backward, uneven iteration counts, unused parameters, rank-gated barriers)."
metadata:
  skill_id: "skl_AmA7aSd-lnN5Qrp74TmqtA"
  title: "Diagnose and fix DDP/NCCL distributed training hangs"
  version: "skv_o3ZrB25rdiEooWsO6grY8A"
  updated: "2026-10-03T04:11:45.978476+00:00"
  canonical_url: "https://vectle.com/skills/skl_AmA7aSd-lnN5Qrp74TmqtA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Diagnose and fix DDP/NCCL distributed training hangs

## TL;DR

DDP/NCCL hangs are almost always collective mismatches: some rank took a different code path and never entered (or never left) a collective the others wait on. Classify WHERE the hang occurs first: at startup (rendezvous/TCP store), at a training step (backward or all-reduce divergence), or at teardown. Fix the launch or the divergent branch; do not guess at timeouts.

Use this when multi-GPU (or multi-node) PyTorch training with
`DistributedDataParallel` hangs — the job stops making progress, GPUs go idle,
or after a long wait the NCCL watchdog aborts with a collective-operation
timeout. DDP hangs are almost always collective mismatches: some rank took a
different code path and never entered (or never left) a collective that other
ranks are waiting on. Classify WHERE the hang occurs before changing anything.

**When not to use this skill:** single-GPU training (no collectives involved); the job crashes with an error instead of hanging (debug the traceback); NCCL is not installed or GPUs are not visible (environment problem).

## 1. Classify the failure from where the hang occurs

**A. Hang at startup, before the first batch.** Ranks never rendezvous. Typical
sign:

```
TimeoutError: The client socket has timed out after 3000s while trying to
connect to (HOST, 12355).
```

This is the TCP store / rendezvous failing: `MASTER_ADDR`/`MASTER_PORT`
mismatch between ranks, a firewall blocking the port, or ranks launched with
different `world_size`. Fix the launch (section 4) — this is not a model bug.

**B. Hang at a specific training step, usually in backward or a logging
all-reduce.** The job runs fine for a while, then stops. After the watchdog
timeout (default 30 minutes) you get:

```
[E ProcessGroupNCCL.cpp] [Rank 1] Watchdog caught collective operation timeout:
WorkNCCL(OpType=ALLREDUCE, Timeout(ms)=1800000) ran for 1802784 milliseconds
before timing out.
[E ProcessGroupNCCL.cpp] Some NCCL operations have failed or timed out. ...
we are taking the entire process down.
```

This is the signature of a collective mismatch: at least one rank never entered
that collective (or entered a different one). Work through section 3.

**C. Hang only on evaluation / checkpoint / logging steps.** Collectives that
run conditionally — `dist.all_reduce` of a loss dict, a `dist.barrier()` before
saving, broadcast of metrics — must be executed by ALL ranks or by NONE. A
`if rank == 0: save_checkpoint()` is fine; a `if rank == 0: dist.barrier()`
hangs every other rank forever. Same for code that only runs when a condition
holds on some ranks (e.g. NaN detected on rank 3 only → early skip).

## 2. Instrument before debugging: get the watchdog to point at the culprit

Do not debug a silent hang at default settings. Shrink the timeout and turn on
the debug machinery so the failure names the stuck collective and the lagging
rank:

```python
from datetime import timedelta
import torch.distributed as dist

dist.init_process_group(
    backend="nccl",
    init_method="env://",
    timeout=timedelta(seconds=300),  # fail fast while debugging; default is 30 min
)
```

```bash
TORCH_DISTRIBUTED_DEBUG=DETAIL \
TORCH_NCCL_BLOCKING_WAIT=1 \
TORCH_NCCL_ASYNC_ERROR_HANDLING=1 \
torchrun --nproc_per_node=8 train.py
```

What each flag buys you:
- `timeout=timedelta(...)` — the watchdog aborts a stuck collective after this
  long instead of the default 30 minutes. Use a short value while debugging,
  restore a generous one for production (legitimately slow steps must not trip
  it).
- `TORCH_DISTRIBUTED_DEBUG=DETAIL` — logs every collective launch with
  sequence numbers, so you can see which ranks entered which collective and
  which rank fell behind.
- `TORCH_NCCL_BLOCKING_WAIT=1` — makes collectives block on the calling thread,
  so a stuck rank's Python stack trace shows the actual collective call instead
  of an unrelated line. (Do not combine with async error handling in
  production; use it for diagnosis.)
- `TORCH_NCCL_ASYNC_ERROR_HANDLING=1` — lets the watchdog abort stuck
  collectives and, under torchelastic, restart from the last checkpoint instead
  of hanging forever.

When the watchdog fires, read the `OpType` and `SeqNum` (or the per-rank debug
log): it names the exact collective the ranks disagreed on. That is where you
look in your code.

## 3. Fix the collective mismatch

Every rank must execute the same sequence of collectives in the same order.
Check these in order:

1. **Conditional backward / conditional collectives.** Any `if` that is true on
   some ranks and false on others, wrapping `loss.backward()`, `optimizer.step()`
   with DDP gradient sync, `dist.all_reduce`, `dist.barrier`, or broadcast, is a
   hang. Restructure so the collective runs unconditionally, or so ALL ranks
   skip it together.
2. **Uneven iteration counts.** With `DistributedSampler` and
   `drop_last=False`, ranks can see different numbers of batches when the
   dataset size is not divisible by `world_size`. A rank that finishes its loop
   early exits while others still all-reduce. Set `drop_last=True`, or make
   sure every rank runs the same number of steps.
3. **Parameters skipped in forward.** If a parameter is unused in some forward
   passes (conditional branches, auxiliary heads), DDP's gradient reduction
   disagrees across iterations. The telltale error is:

   ```
   Expected to mark a variable ready only once. This error is caused by one of
   the following reasons: 1) ...
   ```

   The fix is `DistributedDataParallel(model, find_unused_parameters=True)`
   (costs extra overhead — only use it when branches are genuinely dynamic), or
   restructure the model so every parameter participates every iteration.
4. **Multiple forwards per backward.** Calling forward twice before one
   backward (e.g. accumulating two losses) desynchronizes DDP's bucket
   reduction unless you wrap the extra forwards in `model.no_sync()`.
5. **Eval/checkpoint collectives.** Reduce metrics on all ranks, then let only
   rank 0 write files. Never gate a collective itself on `rank == 0`.

A quick bisection: insert `dist.barrier()` plus a per-rank print before the
suspect region. The last barrier that all ranks pass marks the end of the
agreed-upon collective sequence; the hang is in the region right after it.

## 4. Fix rendezvous and network issues (class A)

- All ranks must agree on `MASTER_ADDR`, `MASTER_PORT`, and `world_size`. With
  `torchrun`, these are set for you — mixing `torchrun` on some nodes with
  manual `python -m torch.distributed.launch` on others is a classic mismatch.
- If NCCL picks the wrong network interface (common on multi-NIC machines),
  pin it: `NCCL_SOCKET_IFNAME=eth0` (or `ib0` for InfiniBand). Confirm with
  `NCCL_DEBUG=INFO`, which logs the interface NCCL chose at startup.
- A port already in use on the master produces connection timeouts that look
  like hangs — pick a free `MASTER_PORT`.

## 5. Checklist for the hanging job

1. Classify: startup rendezvous (A), mid-training collective (B), or
   eval/logging collective (C).
2. Instrument: short `timeout=timedelta(seconds=300)`,
   `TORCH_DISTRIBUTED_DEBUG=DETAIL`, `TORCH_NCCL_BLOCKING_WAIT=1` — rerun and
   read which collective and which rank the watchdog names.
3. Audit for collective mismatch: conditional backward/collectives, uneven
   iteration counts (`drop_last`), unused parameters (`find_unused_parameters`),
   multiple forwards without `no_sync()`.
4. If startup: verify `MASTER_ADDR`/`MASTER_PORT`/`world_size` agree everywhere;
   pin the NIC with `NCCL_SOCKET_IFNAME` if NCCL chose badly.
5. Restore a generous timeout for production; short timeouts are a debugging
   tool only.

## Compatibility

- PyTorch 1.13+ with NCCL backend (Linux, NVIDIA GPUs). Gloo backend hangs have different diagnostics.
- Multi-node: rendezvous via TCP store or etcd.

## Variant phrasings

- pytorch DDP hang NCCL timeout
- distributed training hangs collective mismatch
- NCCL watchdog abort collective operation timeout
- torchrun hang at startup rendezvous


---

Source: [Vectle](https://vectle.com/skills/skl_AmA7aSd-lnN5Qrp74TmqtA). Version: `skv_o3ZrB25rdiEooWsO6grY8A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
