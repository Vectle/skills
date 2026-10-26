---
name: "sonarqube-quality-gates-for-monorepos-0419bcfe60143c4b"
description: "Fixes the concrete pain of one failing SonarQube quality gate blocking an entire monorepo: how to model each service as its own SonarQube project, assign per-project gates, keep conditions on new code instead of overall code, and suppress false positives through issue resolution, exclusions, or NOSONAR without hiding real debt."
metadata:
  skill_id: "skl_ScCQb8yvWq_gnvlfkwDv7g"
  title: "SonarQube quality gates for monorepos: per-project gates, new-code conditions, and safe false-positive suppression"
  version: "skv_4778A08M3sAxQY007MaWoA"
  updated: "2026-10-03T04:06:59.843126+00:00"
  canonical_url: "https://vectle.com/skills/skl_ScCQb8yvWq_gnvlfkwDv7g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.sonarsource.com/sonarqube-server/2026.1/quality-standards-administration/managing-quality-gates/associating-projects-with-quality-gate\",\"https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/changing-quality-gate.md\",\"https://docs.sonarsource.com/sonarqube-server/user-guide/about-new-code\",\"https://docs.sonarsource.com/sonarqube-server/10.1/project-administration/analysis-scope\",\"https://github.com/sshyran/sonarqube/blob/HEAD/server/sonar-docs/src/pages/faq.md\",\"https://community.sonarsource.com/t/quality-gate-is-not-failing-even-when-my-code-duplication-is-4-3-and-quality-gate-is-set-to-4/130700\",\"https://community.sonarsource.com/t/how-do-we-avoid-developers-to-use-nosonar-avoid-bypassing-of-rule-using-nosonar/30620\",\"https://community.sonarsource.com/t/more-than-one-sonarqube-project-per-prb/92389\"]"
---

# SonarQube quality gates for monorepos: stop one red gate from blocking every service

## TL;DR

Model each deployable service as its own SonarQube project, give each project its own quality gate, keep conditions on new code instead of overall code, and suppress false positives through the Issues UI first. Four changes, and one service's red gate stops blocking every other service's pipeline.

Use this skill when a monorepo's SonarQube quality gate keeps failing for reasons unrelated to the change at hand: one service's coverage gap or legacy duplication turns the whole repo red, or every service inherits the same default gate and teams start muting alerts instead of fixing issues.

**When not to use this skill:** you have a single-service repo (one project and the default gate are fine); your SonarQube edition lacks multi-project monorepo binding and you cannot upgrade; the gate failure is a scanner misconfiguration rather than a modeling problem.

## The core problem

A quality gate is evaluated per SonarQube project, and each condition is either on **new code** or on **overall code**. Almost every monorepo gate problem traces back to getting one of those two facts wrong:

- One giant SonarQube project for the whole repo means one gate. Any failing condition anywhere in the repo blocks the whole repo, even if the change touched an unrelated service.
- Many projects all left on the default gate means one strict policy applied to services with very different risk profiles, languages, and legacy debt. Teams respond by gaming the gate instead of fixing code.
- Conditions silently evaluated on new code only are the top source of "why did this pass / why did this fail" confusion.

The fix has four steps: model each deployable unit as its own SonarQube project, give each project its own gate, gate on new code instead of overall code, and suppress false positives through the auditable channels first.

## Step 1 — one SonarQube project per deployable unit

A quality gate is attached to a project, not to a repository. If you want independent pass/fail signals per service, you need independent SonarQube projects — one gate cannot be scoped to a subdirectory.

- For each independently deployable service, run a separate analysis with a distinct `sonar.projectKey` (per-service `sonar-project.properties`, or per-CI-job `-Dsonar.projectKey [your value] flags). Key pattern: one org prefix, one repo slug, one service name.
- SonarQube's monorepo support binds multiple SonarQube projects to the same repository. Each project analyzes and decorates pull requests separately — on GitHub that is one status check per project, typically named `[PROJECT_NAME] SonarQube Code Analysis`, and each can be required independently in branch protection.
- On SonarQube Server, multi-project monorepo binding has historically been an Enterprise Edition or above feature — confirm against your edition's documentation before planning around it.
- Do not use the legacy `sonar.modules` mechanism to split one project; it gives you one project and therefore still one gate.

Result: a failing gate names exactly one service, and no other service's pipeline is affected.

## Step 2 — assign each project its own quality gate

The default gate applies to every project that is not explicitly assigned one. The built-in `Sonar way` gate is read-only — copy it and adjust the copy rather than trying to edit it.

Create the gate: open the **Quality Gates** page (top menu) or **Administration > Quality Gates**, choose **Create**, name it per team or service, and add conditions. Then associate it with projects using exactly one of these two paths — the most recently saved association always wins, so do not mix both paths for the same project:

1. **At the gate level.** From the Quality Gates page, associate projects with the gate. Requires the **Administer Quality Gates** permission.
2. **At the project level.** Open the project, go to **Quality Gate**, select **Use a specific quality gate**, pick the gate from the list, and **Save**. Requires the **Administer Quality Gates** or **Administer Project** permission.

Repeat for every service whose risk profile differs from the default. A backend payments service and a static docs site should never share a gate.

## Step 3 — gate on new code, not overall code

The built-in `Sonar way` gate defines conditions on **new code only**. New code is the code added or modified inside the project's new code definition; overall code is everything. The two scopes produce different numbers — a project can hold an A for overall maintainability while new code drags a B.

Concrete confusion this avoids: a condition "Duplicated Lines > 4% fails" evaluated on new code does **not** fail when overall duplication is 4.3% but the changed lines in the new-code window are below 4%. If a gate seems to pass or fail for no reason, check the **New Code** tab versus the **Overall Code** tab before touching configuration.

Set the new code definition per project (project settings) to match the team's workflow:

- **Previous version** (default): everything changed since the last `sonar.projectVersion` you set. Bump the version with every release or the "new" window grows unbounded.
- **Number of days**: a rolling window, e.g. the last 30 days.
- **Specific date**: a fixed baseline, useful when onboarding a legacy codebase.
- **Reference branch**: compare against a branch such as `main`. Available in editions that support branch analysis; the standard choice for feature-branch and PR workflows.

For a monorepo with mixed services, the pragmatic split is: reference branch for services developed on long-lived branches, previous version for services cut as releases.

One more mechanism worth knowing: the **fudge factor**. Duplication and coverage conditions are ignored until the change has at least 20 new lines, so a two-line fix cannot fail on coverage alone. It is enabled by default and can be toggled per project under the project's Quality Gate settings (**Ignore duplication and coverage on small changes**). If tiny PRs behave differently than expected, check this setting before changing conditions.

## Step 4 — suppress false positives without hiding real debt

Work through these in order. Each step down the list is broader, less auditable, and more likely to hide real problems.

### 4a. Resolve the issue in the UI (preferred)

Open the issue in the project's **Issues** view and change its status:

- **False positive**: the analyzer is wrong. Mark it as such with a one-line reason.
- **Won't fix**: the issue is real but the team deliberately accepts it. Mark it as such with a one-line reason.

Why first: the resolution is attached to the issue instance, shows up in the issue history, is visible to every reviewer, and — with branch or pull request analysis — survives merges, so nobody re-triages it on the next branch. No code churn, no blanket suppression.

### 4b. Exclude whole classes of noise via analysis scope

When an entire category of files can never be fixed meaningfully — generated code, vendored libraries, build output — exclude it from analysis instead of resolving issues one by one:

- In `sonar-project.properties` (or the equivalent scanner properties per service job): `sonar.exclusions`, `sonar.test.exclusions`, `sonar.coverage.exclusions`, and `sonar.cpd.exclusions` for copy-paste detection. Note the naming trap: sources use `sonar.sources`/`sonar.exclusions` while test scope uses `sonar.tests` with `sonar.test.exclusions` and `sonar.test.inclusions`.
- In the UI at **Project Settings > General Settings > Analysis Scope > Files**: Source File Exclusions, Test File Exclusions, coverage exclusions.
- At **Project Settings > General Settings > Analysis Scope > Issues**: **Ignore Issues on Files** (regex matched against file content, e.g. generated-code markers) and **Ignore Issues in Blocks** (start/end markers such as `BEGIN-NOSCAN` / `END-NOSCAN` delimiting code that stays scanned-outside-the-block).

Rule of thumb: exclude what nobody can fix by design. Never exclude a service's real source just to turn a red gate green — the debt is still there, you just stopped measuring it.

### 4c. NOSONAR comments (last resort, single line only)

Most language analyzers support a trailing comment such as `//NOSONAR` (use the comment style of the language) at the end of the offending line. It suppresses **all** issues on that line — current and future, for every rule. That breadth is exactly why it is the last resort:

- Use it only when UI resolution and exclusions cannot express the case, and always put a rationale comment on the line above explaining why this line is special.
- Expect reviewers to challenge every NOSONAR. Enable the **Track uses of NOSONAR** rule in your quality profile so every suppression itself raises an issue you can audit periodically.

## Compatibility

- SonarQube Server / Community Build: per-project gates and new-code conditions are core features in all recent versions.
- Multi-project monorepo binding (several SonarQube projects on one repo, per-PR decoration per project) has historically required Enterprise Edition or above; confirm against your edition's docs.
- SonarQube Cloud: monorepo support varies by plan.

## Variant phrasings

- SonarQube monorepo quality gate per service
- one failing quality gate blocks entire monorepo
- SonarQube new code vs overall code conditions
- per-project quality gates monorepo

## Anti-patterns to avoid

- Gating overall-code metrics on a legacy monorepo. New-code gating lets old debt decay without blocking every deploy; pair it with a separate remediation plan for the legacy code.
- Relaxing the shared gate to accommodate one noisy service. Give that service its own gate (Step 2) instead of weakening the bar for everyone.
- NOSONAR as a habit, or NOSONAR with no rationale. It suppresses future issues on the line too — a rule change next quarter will be silently swallowed.
- Commenting out the gate check in CI (`sonar.qualitygate.wait=true` removed, `waitForQualityGate` skipped) instead of fixing the condition. The gate then exists only as decoration.
- Assuming exclusions shrink the new-code coverage denominator. Exclusions shrink both scopes only for lines inside the new-code window; if the excluded files had no changed lines in the window, `new_coverage` will not move. Measure before and after.

## Quick checklist

1. Each deployable service is its own SonarQube project with its own project key.
2. Each project has an explicitly assigned gate (never the default by accident).
3. All custom gate conditions are on new code unless you have a written reason for an overall-code condition.
4. The new code definition matches the branching/release model, and `sonar.projectVersion` is bumped per release where the previous-version definition is used.
5. False positives are resolved in the Issues UI; structural noise is excluded via analysis scope; NOSONAR appears only with a rationale comment and is tracked by a rule.
6. The fudge-factor behavior is understood before anyone "fixes" small-PR coverage failures by weakening conditions.


---

Source: [Vectle](https://vectle.com/skills/skl_ScCQb8yvWq_gnvlfkwDv7g). Version: `skv_4778A08M3sAxQY007MaWoA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
