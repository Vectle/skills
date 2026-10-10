---
name: "404-not-found-code-deployment-not-foun-0d991fcf93c4fe22"
description: "You open your Vercel URL and get \"404: NOT_FOUND\" with \"Code: DEPLOYMENT_NOT_FOUND\" instead of your site. Vercel has no deployment attached to that hostname: the domain is not assigned to the project, the deployment was deleted, or you opened a stale preview URL. Fix: attach the domain in Settings, or promote a Ready build to Production. Not for in-app 404s or build failures."
metadata:
  skill_id: "skl_mvyUa1NSOeqcMwybJ8ey0w"
  title: "404: NOT_FOUND Code: DEPLOYMENT_NOT_FOUND"
  version: "skv_zKbn2DWjHEKVYJIkWf4wPw"
  updated: "2026-10-03T05:42:32.009078+00:00"
  canonical_url: "https://vectle.com/skills/skl_mvyUa1NSOeqcMwybJ8ey0w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# 404: NOT_FOUND Code: DEPLOYMENT_NOT_FOUND (Vercel)

TL;DR: Vercel is telling you it has no deployment attached to that hostname. Your DNS works, but the domain is not assigned to any project, or the deployment behind the URL is gone. Fix it in the dashboard: Settings -> Domains -> add the domain to the project, or open the Deployments tab and promote a Ready build to Production. No code change needed.

```text
404: NOT_FOUND
Code: DEPLOYMENT_NOT_FOUND
ID: cpt1::abc-123
```

## 1. Read the code, not just the 404

Vercel prints two different 404s and they mean different things:

- `NOT_FOUND`: a deployment IS serving, but its route table has no match for your URL. That is a routing/build-output problem.
- `DEPLOYMENT_NOT_FOUND`: no deployment is attached to the hostname at all. That is a domain/project problem, and it is this skill.

Expected: you confirm the page shows `DEPLOYMENT_NOT_FOUND`.

## 2. Attach the domain to the project

In the Vercel dashboard, open your project -> Settings -> Domains. Type the domain (e.g. `carbcleantruckcheck.app`) and click Add. It takes effect within seconds; you do not need to redeploy.

Expected: refreshing the URL loads your site instead of the error page.

## 3. Check you are opening the right URL

Preview URLs (`project-git-branch-team.vercel.app`) are ephemeral: they die when the branch or project is deleted. The production domain (`project.vercel.app` or your custom domain) is the stable one. If you bookmarked a preview URL months ago, that is your 404.

Expected: the production URL from the latest deployment's Visit button works.

## 4. Confirm a Ready production deployment exists

Open the Deployments tab. If the latest Production deployment shows Error or Canceled, there is nothing to serve: fix the build error first, then redeploy. If a good build exists but is not Production, promote it.

Expected: Deployments tab shows a Ready build marked Production.

## When this applies

- The Vercel error page shows `Code: DEPLOYMENT_NOT_FOUND`
- Custom domain added but never attached to the project, or project renamed
- Old preview/deployment URL that no longer exists

## When it does not apply

- `Code: NOT_FOUND` without `DEPLOYMENT_`: routing or output-directory issue, different fix
- Your app renders its own 404 page: that is your code, not Vercel
- Build failures in the deploy log: fix the build first

## Compatibility

All Vercel plans. Applies to `*.vercel.app` domains and custom domains alike. Dashboard steps are the same on Hobby, Pro, and Enterprise.

## Why it happens

Vercel routes each hostname to a specific deployment. If the domain was never added under the project's Domains settings, was removed, or the deployment the URL pointed at was deleted, the edge has nowhere to send the request and returns this code. Redeploying does not attach a domain, which is why people get stuck in a redeploy loop.

## Edge cases

- Domain shows as assigned but still 404s: DNS may still be propagating (up to 24h), or the domain is assigned to a different project/team.
- `project.vercel.app` taken by someone else: pick another name or rename the project so the default slug is free.
- Deployment Protection on: deployment URLs ask for a Vercel login by design; that is not DEPLOYMENT_NOT_FOUND, use the production domain instead.

---

Source: [Vectle](https://vectle.com/skills/skl_mvyUa1NSOeqcMwybJ8ey0w). Version: `skv_zKbn2DWjHEKVYJIkWf4wPw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
