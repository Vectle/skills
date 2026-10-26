---
name: "error-unable-to-render-paypalbuttons-b-178d7b2bc734e4c2"
description: "Fixes 'Unable to render [PayPalButtons] because window.paypal.Buttons is undefined' in react-paypal-js by passing components: 'buttons' to the parent PayPalScriptProvider, plus fixes for the intermittent variant (dataNamespace and element id collisions). Use when PayPal buttons fail to render in a React app. Not for backend PayPal API errors or sandbox credential problems."
metadata:
  skill_id: "skl_UfaLTWl2BszcF223k9wumQ"
  title: "Error: Unable to render [PayPalButtons] because window.paypal.Buttons is undefined"
  version: "skv_H8pYM4hBGwzusgxDEUs02g"
  updated: "2026-10-03T04:31:17.249201+00:00"
  canonical_url: "https://vectle.com/skills/skl_UfaLTWl2BszcF223k9wumQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/paypal/paypal-js/issues/572\"]"
---

Fix first: pass `components: "buttons"` in the options of your parent PayPalScriptProvider, and make sure PayPalButtons is rendered inside that provider. Thats the whole fix in most cases. If the button loads sometimes and not others, keep reading.

```text
Uncaught runtime errors:
ERROR Unable to render [PayPalButtons] because window.paypal.Buttons is undefined.
To fix the issue, add 'buttons' to the list of components passed to the parent PayPalScriptProvider
```

1. In the PayPalScriptProvider options, set `components: "buttons"`. Expected: the error is gone on reload and the button renders.
2. Confirm PayPalButtons sits inside the provider tree. Expected: `window.paypal.Buttons` is defined when you check the console.
3. If it loads intermittently, add `dataNamespace: "paypal_sdk"` to the script options. One user confirmed this fixed flaky loads caused by namespace conflicts. Expected: the button loads on every refresh.
4. Check for a DOM element with `id="paypal"`. Another user found one was shadowing `window.paypal`. Expected: `document.getElementById("paypal")` returns null.

When to use: your React app renders PayPalButtons via react-paypal-js and the button wont render.

When not to use: backend PayPal API failures, sandbox credential problems, or plain script-tag integrations that dont use the React wrapper.

Compatibility: react-paypal-js (also published as @paypal/react-paypal-js), paypal-js. Reported in paypal/paypal-js#572.

Variants:
- "paypal button sometimes loads sometimes doesnt"
- "window.paypal.Buttons is undefined react"
- "PayPalScriptProvider components buttons"

Root cause: the PayPal SDK script was loaded without the buttons component, so `window.paypal.Buttons` never got defined. Flaky cases came from a namespace conflict or a page element whose id shadowed `window.paypal`.

Edge cases: more than one PayPalScriptProvider on the page, the SDK script loaded twice, or an ad blocker eating the PayPal CDN script. The fix above wont help if the script never loads, so check the network tab if nothing changes.

---

Source: [Vectle](https://vectle.com/skills/skl_UfaLTWl2BszcF223k9wumQ). Version: `skv_H8pYM4hBGwzusgxDEUs02g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
