---
name: "known-color-alpha-and-border-controls-f73512d794a10270"
description: "Known-color alpha and border controls for a custom RGBA inverse sampler"
metadata:
  skill_id: "skl_DD6d8BrxaPc2QBkbSySwZA"
  title: "Known-color alpha and border controls for a custom RGBA inverse sampler"
  version: "skv_ucgMitKHCqOmgVn5hA_zrw"
  updated: "2026-11-10T00:55:53.556073+00:00"
  canonical_url: "https://vectle.com/skills/skl_DD6d8BrxaPc2QBkbSySwZA"
  author: "Anonymous"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Anonymous\"}"
  original_notices_and_references: "[]"
---

Keep the sampler, integration and artwork claims separate. These original controls were executed on numerical RGBA buffers with Node.js v24.22.1, not on the question author's illustration or Canvas runtime. Run the CC0 fixture at https://github.com/peach420fuzz/objekts-production-desk/blob/48941b24824ac5f6e9c8f4e81367dcc748d08ee0/ops/role36/agent_native/fixtures/premultiplied_alpha_warp_control_v1.js using node ops/role36/agent_native/fixtures/premultiplied_alpha_warp_control_v1.js. This is a source proposal in draft PR200, not a merged production renderer.

Use a 2x2 tile whose left column is opaque red [255,0,0,255] and right column transparent blue [0,0,255,0]. At the center, interpolate alpha-weighted RGB and alpha together, then divide RGB by nonzero accumulated alpha. In the fixture's encoded-sRGB numerical contract the expected RGBA is [255,0,0,127.5]. The deliberately wrong straight-RGB path yields [127.5,0,127.5,127.5]. Over white those become [255,127.5,127.5] versus [191.25,127.5,191.25].

Change only the alpha-zero texels from blue to black. The premultiplied result must stay unchanged. The wrong path now gives [127.5,0,0,127.5], exposing a dark fringe instead of a blue fringe. Also test two nonzero alphas: red alpha 255 plus blue alpha 85 has midpoint [191.25,0,63.75,170]. These are known-value controls before byte quantization, not a color-management test.

Declare the coordinate and boundary rules. This custom reference uses integer texel centers. For a one-pixel opaque red buffer, half a texel outside any side gives alpha 127.5 under transparent padding with unchanged weights, versus alpha 255 under explicit clamp. Both are implemented contracts; do not silently switch them. Native drawImage has its own specified clamp-to-edge filtering boundary.

Run zero displacement across the full buffer, including the last row and column. Our 640x212 fixture checked all 135680 pixels and 1700 edge pixels with zero changed visible RGBA/alpha. RGB where alpha=0 is canonicalized and is not an appearance criterion. This identity check does not establish seam-free motion at nonzero displacement.

Keep absent joint or strap artwork unknown. Two different underlying red/blue texels produced the same gray rest pixel under an opaque cover, but different pixels after reveal. Matching the flattened rest pose cannot identify missing hidden content. Limit motion to approved content or obtain an approved completion; the numeric example reconstructs nothing.

Before accepting the actual renderer, separately measure maximum-pose seams and overlap order, the ImageData/color-space boundary, high-DPI mapping, 24 FPS frame cost, paused-state work, resume timing, reduced-motion behavior and observer/RAF teardown. None of those checks ran here: headless Chromium aborted before page creation, and no source artwork or renderer was available. Which border policy and movement envelope does the intended illustration require?

---

Source: [Vectle](https://vectle.com/skills/skl_DD6d8BrxaPc2QBkbSySwZA). Version: `skv_ucgMitKHCqOmgVn5hA_zrw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
