---
name: "vite-default-import-fails-on-mailgun-j-6abeabc7c33aaab5"
description: "Shows how to fix vite: default import fails on mailgun.js AMD web build. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_6mur5BSMksFfSVTSdapH2w"
  title: "Vite: default import fails on mailgun.js AMD web build"
  version: "skv_MEvljRAcWxcExORWRYllsg"
  updated: "2026-10-03T16:25:37.474845+00:00"
  canonical_url: "https://vectle.com/skills/skl_6mur5BSMksFfSVTSdapH2w"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Add vite-plugin-babel and babel-plugin-transform-amd-to-commonjs to devDependencies, then in vite.config.ts use plugins: [babel({ babelConfig: { plugins: ['transform-amd-to-commonjs'] } }), react()]. What works: In a Vite project, import Mailgun from 'mailgun.js' fails because the web build ships only in AMD format, which Vite can't consume.

## When to use

You are seeing this: What was reported: Issue mailgun/mailgun-js#415 (closed, 13 comments): In a Vite + React project, import Mailgun from 'mailgun.js' fails with SyntaxError: The requested module... does not provide an export named 'default'. Use this skill when you run into "Vite: default import fails on mailgun.js AMD web build".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Steps

1. What was reported:
Issue mailgun/mailgun-js#415 (closed, 13 comments): In a Vite + React project, `import Mailgun from 'mailgun.js'` fails with `SyntaxError: The requested module ... does not provide an export named 'default'`. The web build of mailgun.js ships only in AMD format, which Vite cannot consume directly.

2. What works:
In a Vite project, import Mailgun from 'mailgun.js' fails because the web build ships only in AMD format, which Vite can't consume. Workaround: convert the AMD build to CommonJS with the Babel plugin. Add vite-plugin-babel and babel-plugin-transform-amd-to-commonjs to devDependencies, then in vite.config.ts use plugins: [babel({ babelConfig: { plugins: ['transform-amd-to-commonjs'] } }), react()]. The commenter verified this works.


---

Source: [Vectle](https://vectle.com/skills/skl_6mur5BSMksFfSVTSdapH2w). Version: `skv_MEvljRAcWxcExORWRYllsg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
