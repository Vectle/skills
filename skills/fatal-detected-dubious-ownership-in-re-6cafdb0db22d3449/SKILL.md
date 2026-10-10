---
name: "fatal-detected-dubious-ownership-in-re-6cafdb0db22d3449"
description: "git refuses with fatal: detected dubious ownership in repository at ... when the repo directory is owned by a different user than the one running git: Docker bind mounts, CI runner workspaces, sudo clones. Use this skill when an agent hits this exact error to add the repo to git safe.directory trust, with per-user vs system scope, the wildcard caveat, and how to tell it apart from real permission errors. Not for repos you do not trust; not a fix for actual file permissions."
metadata:
  skill_id: "skl_zd0S9Q3wiUJhEl-X4OGIVQ"
  title: "fatal: detected dubious ownership in repository at '[path]'"
  version: "skv_GTiRXpmr_BKrTbNaM2usXw"
  updated: "2026-10-03T06:08:15.419339+00:00"
  canonical_url: "https://vectle.com/skills/skl_zd0S9Q3wiUJhEl-X4OGIVQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

git refuses to run because the repository directory is owned by a different user than the one running git. Trust the repo once and move on:

```bash
git config --global --add safe.directory /path/to/the/repo
```

Re-run the original git command; it should work now. This guard is a real security feature (CVE-2022-24765), so only trust repos you actually control.

## Verbatim error

```text
fatal: detected dubious ownership in repository at '/path/to/the/repo'
'
```

(The trailing quote is a shell quirk of the error print; ignore it.)

## Fix it

### Step 1: confirm you own the directory

```bash
whoami && ls -ld /path/to/the/repo
```

Expected: the owner printed by `ls` differs from the user running git. Common causes: the repo was cloned by root, copied from another user, or is a Docker bind mount that shows up as root-owned inside the container.

### Step 2: add the repo to git's safe list

```bash
git config --global --add safe.directory /path/to/the/repo
```

Expected: no output, exit code 0. Verify it stuck:

```bash
git config --global --get-all safe.directory
```

Expected output lists the path you just added:

```text
/path/to/the/repo
```

### Step 3: re-run the original command

```bash
git status
```

Expected: normal `git status` output instead of the fatal error.

## When this applies

- git errors with "dubious ownership" in Docker containers with bind mounts (the classic: files owned by root, container runs as a different user).
- CI runners where the workspace was created by a different user (root in the runner image, job user at runtime).
- You ran `sudo` for a clone and now use git as a normal user.
- Repos copied or rsynced from another user or machine without preserving the working directory ownership.

## When it does NOT apply

- The repo sits on a machine with multiple users and you do not trust whoever owns `.git`; an untrusted `.git` can contain malicious hooks and config. Inspect `.git/config` and `.git/hooks` first.
- You only need one command to run: prefer the per-invocation form instead of trusting globally:

```bash
git -c safe.directory=/path/to/the/repo status
```

- Actual permission errors (e.g. "Permission denied" on `.git/objects`): that is a file-permission problem, not this one.

## Version compatibility

- git 2.35.2 and later enforce the ownership check.
- git 2.36.2 and later also accept a `*` wildcard (`safe.directory='*'`); avoid it on shared machines because it trusts everything.

Check your version with `git --version`.

## Variant phrasings

The message is identical across platforms; only the path changes:

- Windows: `fatal: detected dubious ownership in repository at 'C:[HOME]/...'`
- Docker: the container path, e.g. `/app` or `/workspace`, owned by root
- CI: the runner workspace path, owned by the image build user

## Why it happens (root cause)

Git fixed CVE-2022-24765 by refusing to read `.git` metadata it does not trust. The `.git` directory can hold executable hooks and config that git would honor; if another user owns it, running git commands could execute that user's code. The ownership check forces you to opt in per repository via `safe.directory`.

## Edge cases

- **Dockerfiles:** bake the trust into the image (`RUN git config --global --add safe.directory /app`) or set it at container start for one-off containers.
- **The wildcard `*`:** `git config --global --add safe.directory '*'` works on git 2.36.2+, but on a shared host it disables the protection for every repo. Prefer listing paths.
- **sudo users:** each user has their own global config; a trust you add as root does not cover your normal user. Add it as the user who runs git.
- **System-wide trust:** admins can set `safe.directory` in the system config (`git config --system --add safe.directory [path]`) instead of per-user.

---

Source: [Vectle](https://vectle.com/skills/skl_zd0S9Q3wiUJhEl-X4OGIVQ). Version: `skv_GTiRXpmr_BKrTbNaM2usXw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
