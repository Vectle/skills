---
name: "lemon-squeezy-checkout-ignores-dark-tr-87374c855ec52941"
description: "Do not pass dark: true to Lemon Squeezy's create checkout and expect a dark checkout: the option is deprecated and silently ignored. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_47Xx1UHqxOVTgi3f6_JqPQ"
  title: "Lemon Squeezy checkout ignores dark:true: theming moved out of the API"
  version: "skv_9LF6pDU5Jv4KEjOqZEeCwQ"
  updated: "2026-10-03T04:46:23.743838+00:00"
  canonical_url: "https://vectle.com/skills/skl_47Xx1UHqxOVTgi3f6_JqPQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Do not pass dark: true to Lemon Squeezy's create checkout and expect a dark checkout: the option is deprecated and silently ignored. Checkout theming is now controlled by themes in the Lemon Squeezy dashboard, and the API cannot select a theme per checkout. If your site has a light/dark toggle, match the checkout by configuring the store theme, not the API call.

## Fix

Do not pass dark: true to Lemon Squeezy's create checkout and expect a dark checkout: the option is deprecated and silently ignored. Checkout theming is now controlled by themes in the Lemon Squeezy dashboard, and the API cannot select a theme per checkout. If your site has a light/dark toggle, match the checkout by configuring the store theme, not the API call.

Context: GitHub issue lmsqueezy/lemonsqueezy.js#114: Multiple developers passed dark: true when creating a checkout and the checkout page ignored it. A Lemon Squeezy contributor confirmed the dark option was deprecated in favor of themes, and that it is currently not possible to change the theme via the API at all. The docs and SDK were updated to remove the option.

## Matched source
Source: Published skill
Original query: "Lemon Squeezy checkout ignores dark:true: theming moved out of the API"
Key terms: checkout, dark, ignores, lemon, moved, squeezy, theming, true

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_47Xx1UHqxOVTgi3f6_JqPQ). Version: `skv_9LF6pDU5Jv4KEjOqZEeCwQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
