---
name: "error-maximum-update-depth-exceeded-wh-f53972570628ff53"
description: "Fixes 'Maximum update depth exceeded' with the useCompletion hook on long gpt-4o responses in Next.js. Memoize your message component: import { memo } from 'react' and export memo(ChatMessage). Memoizing stops the render recursion that blows the update depth. Use when the error hits on long streaming responses. Not for other render errors."
metadata:
  skill_id: "skl_1-EnU40IqA89bY13EeP5lg"
  title: "Error: Maximum update depth exceeded. When using useCompletion hook in nextjs, on long response on gpt-4o"
  version: "skv_BvJx-BvZwUQCpxUYw5L46A"
  updated: "2026-10-03T05:32:33.448099+00:00"
  canonical_url: "https://vectle.com/skills/skl_1-EnU40IqA89bY13EeP5lg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/vercel/ai/issues/1610\"]"
---

Fix first: memoize your message component.

```tsx
import { memo } from 'react';
export default memo(ChatMessage);
```

1. Wrap the message component in memo.
2. Re-run with the long gpt-4o response. Expected: no more 'Maximum update depth exceeded'; the UI stops hanging.

When to use: useCompletion from the AI SDK on a long gpt-4o response in streaming mode hangs the UI with 'Maximum update depth exceeded'.

When not to use: other render errors (different causes).

Compatibility: AI SDK (useCompletion), Next.js, React. Reported in vercel/ai#1610.

Variants:
- "useCompletion Maximum update depth exceeded"
- "useCompletion long response hang"
- "ai 1610"

Root cause: the hook updates completion state very fast; the unmemoized component re-renders recursively and blows the update depth.

Edge cases: this only bites on long responses, where the update pace is high enough to recurse.

---

Source: [Vectle](https://vectle.com/skills/skl_1-EnU40IqA89bY13EeP5lg). Version: `skv_BvJx-BvZwUQCpxUYw5L46A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
