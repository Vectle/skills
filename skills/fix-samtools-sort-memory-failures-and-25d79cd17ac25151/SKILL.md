---
name: "fix-samtools-sort-memory-failures-and-25d79cd17ac25151"
description: "Shows how to fix samtools sort memory failures and OOM kills. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_CiQ-FnocB26XCg6YeBEaZw"
  title: "Fix samtools sort memory failures and OOM kills"
  version: "skv_2BJ3NKZzUf72fAzAukqSfg"
  updated: "2026-10-03T05:03:11.889643+00:00"
  canonical_url: "https://vectle.com/skills/skl_CiQ-FnocB26XCg6YeBEaZw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

For "couldn't allocate memory for bam_mem": from the man page: -m INT, Approximately the maximum required memory per thread, specified either in bytes or with a K, M, or G suffix. [768 MiB] So samtools sort -m 5G -@ 12 requests up to ~60 GiB (5 GiB × 12 threads), not 5 GiB. This is the single most common cause of Biostars "sort ran out of memory" threads: the declared -m looked reasonable, but multiplied by -@ it exceeded the machine or the job's memory limit.

```text
couldn't allocate memory for bam_mem
```

## When to use

You are seeing this: samtools sort -m is per thread, not total. Use this skill when you run into "Fix samtools sort memory failures and OOM kills".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## 0. The one fact that explains most failures

`samtools sort -m` is **per thread**, not total. From the man page:

> `-m INT`, Approximately the maximum required memory **per thread**,
> specified either in bytes or with a `K`, `M`, or `G` suffix. [768 MiB]

So `samtools sort -m 5G -@ 12` requests up to ~60 GiB (5 GiB × 12 threads),
not 5 GiB. This is the single most common cause of Biostars "sort ran out of
memory" threads: the declared `-m` looked reasonable, but multiplied by `-@`
it exceeded the machine or the job's memory limit.

Compute the real request before touching anything:

```
total ≈ (-m value) × (-@ threads)
```

## 1. Classify the failure

## A. `samtools sort: couldn't allocate memory for bam_mem`

The sort's per-thread allocation failed. Compare `-m × -@` against actual
available RAM (`free -g`):

- If `-m × -@` exceeds free RAM (or the scheduler/Slurm/Nextflow memory limit
 for the job): **over-requested memory**. Fix: lower `-m`, lower `-@`, or
 both so the product fits. Example on a 32 GiB node:

 

```bash
  samtools sort -m 2G -@ 8 -T /scratch/sort_tmp -o sorted.bam in.bam
  # 2G x 8 threads = ~16 GiB, comfortably inside 32 GiB
  ```

- If `-m × -@` fits easily yet allocation still fails: suspect the machine is
 actually smaller than you think (a VM resized to MB instead of GB is a real
 Biostars case) or another process holds the memory. Check `free -g` and
 `dmesg | tail` for the truth.

## B. Shell prints `Killed` / exit code 137 / `line N: [PID] Killed samtools sort`

That's the Linux OOM killer (or the scheduler killing an over-limit job), not
samtools failing cleanly. Same fix as A, the product `-m × -@` is too big 
plus check the scheduler: in Nextflow/Slurm/SGE the job's declared memory
(e.g. `memory '32 GB'`) is the limit, not the node's RAM. Size the sort to the
*declared* memory:

```
# nextflow process declaring 32 GB / 8 cpus:
samtools sort -m 3G -@ 8 -T ./sort_tmp -o out.bam in.bam
# 3G x 8 = ~24 GiB, under the 32 GB declaration with headroom
```

Splitting one process into two sequential sorts does not help an OOM: each
sort's `-m × -@` is what matters, not how many sorts ran.

## C. `No space left on device` / sort stalls with growing temp files

When the data doesn't fit in `-m × -@`, sort spills to temp files named
`[tmpprefix].NNNN.bam` in the `-T` directory, then merges them single-threaded
at the end. Two sub-causes:

1. **The `-T` directory is full or tiny.** `/tmp` is often a tmpfs 
 physical RAM, not disk, so `-T /tmp` on a big sort burns RAM twice
 (sort buffers *and* temp files) and then fails. Point `-T` at a real
 scratch filesystem with free space:

 

```bash
   mkdir -p /scratch/$USER/sort_tmp
   samtools sort -m 2G -@ 8 -T /scratch/$USER/sort_tmp -o sorted.bam in.bam
   ```

 Check with `df -h` on the `-T` directory *before* the sort.

2. **`-m` is far too small for the data**, so sort creates thousands of temp
 files and the final merge crawls. Raise `-m` (keeping the product under
 available RAM) instead of lowering it. If you can't raise `-m`, accept the
 slow merge, lowering `-m` further makes it worse.

## D. Name-sort (`-n`) pipelines OOM where coordinate sorts don't

`samtools sort -n` (name sort, used before `fixmate`/`markdup`) needs
substantially more memory than a coordinate sort on the same file. If only the
`-n` stage fails:

- Give the `-n` stage a bigger `-m` than the coordinate stage, or
- use `samtools collate` instead: the man page notes *"Consider using samtools
 collate instead if you need name collated data without a full
 lexicographical sort"*, collate is designed for exactly the
 fixmate/markdup input pattern and uses less memory.

Also remember: `-n` (and `-t`) sorts **cannot be indexed**, `samtools index`
requires coordinate sort. If a downstream tool complains about a missing
index, the fix is a second coordinate sort, not re-running the name sort.

## 2. Rules of thumb

- Default `-m` is 768 MiB per thread. On a modern node, 4 8 threads at
 1 2 GiB each (`-m 2G -@ 4`) sorts most BAMs fast; more threads help up to
 the disk's write bandwidth, then stop helping.
- `-m` has a floor of 1M (sort enforces it to avoid a temp-file explosion).
- Always set `-T` explicitly to a scratch dir with space; never rely on `/tmp`
 on shared systems.
- Verify the sorted result: `samtools view -H sorted.bam | grep '^@HD'`
 should show `SO:coordinate` (or `SO:queryname` for `-n`), and
 `samtools quickcheck sorted.bam` should exit silently.

## Quick decision tree

1. `couldn't allocate memory for bam_mem` → compute `-m × -@` vs free RAM → lower `-m`/`-@`.
2. `Killed` / exit 137 → same math, but against the *job's declared* memory (scheduler/Nextflow), not the node.
3. `No space left on device` or endless temp files → `-T` on real scratch disk (`df -h` first); don't use tmpfs `/tmp`.
4. Only `-n` fails → bigger `-m` for that stage, or `samtools collate`.
5. Merge phase slow but progressing → `-m` too small; raise it if RAM allows.


---

Source: [Vectle](https://vectle.com/skills/skl_CiQ-FnocB26XCg6YeBEaZw). Version: `skv_2BJ3NKZzUf72fAzAukqSfg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
