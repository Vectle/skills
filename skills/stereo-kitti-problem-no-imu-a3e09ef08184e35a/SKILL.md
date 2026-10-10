---
name: "stereo-kitti-problem-no-imu-a3e09ef08184e35a"
description: "Fixes the ORB-SLAM3 stereo KITTI example failing to parse the settings YAML by changing Viewer.ViewpointY: -100 to -100.0 (the parser needs the decimal point). Use when the stereo KITTI example dies on settings load. Not for IMU or tracking failures at runtime."
metadata:
  skill_id: "skl_VHLAnC0hTzMyB7YHYEPVdA"
  title: "stereo kitti problem no IMU"
  version: "skv_yuYQUmttTRN4y9_x09uiAA"
  updated: "2026-10-03T04:41:31.465469+00:00"
  canonical_url: "https://vectle.com/skills/skl_VHLAnC0hTzMyB7YHYEPVdA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

Fix first: in your settings YAML, change `Viewer.ViewpointY: -100` to `Viewer.ViewpointY: -100.0`. The YAML parser treats the bare integer as the wrong type; the decimal form parses correctly. Commenter-verified.

```text
# failing value
Viewer.ViewpointY: -100
# fixed value
Viewer.ViewpointY: -100.0
```

1. Open the settings YAML you pass to the stereo KITTI example.
2. Change `Viewer.ViewpointY: -100` to `Viewer.ViewpointY: -100.0`.
3. Re-run the example. Expected: the settings parse and the example starts.

When to use: the ORB-SLAM3 stereo KITTI example fails while parsing the settings YAML.

When not to use: tracking or IMU problems at runtime (the settings loaded fine there), or other SLAM systems.

Compatibility: ORB-SLAM3, stereo KITTI example, settings YAML.

Variants:
- "orb slam3 kitti yaml parse error"
- "Viewer.ViewpointY -100"
- "stereo kitti example settings yaml"

Root cause: the settings parser expects a floating-point value for Viewer.ViewpointY and chokes on the bare integer -100.

Edge cases: if the parser complains again, check the other numeric settings for the same bare-integer problem.

---

Source: [Vectle](https://vectle.com/skills/skl_VHLAnC0hTzMyB7YHYEPVdA). Version: `skv_yuYQUmttTRN4y9_x09uiAA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
