---
name: "tvos-projects-based-on-expo-cannot-ins-ab9df1016254038f"
description: "Fixes tvOS projects based on expo being unable to install react-native-purchases. tvOS support was added in react-native-purchases 7.26.0; the reporter confirmed it runs perfectly there. Upgrade to 7.26.0 or newer for tvOS. Use when tvOS install fails. Not for other platforms."
metadata:
  skill_id: "skl_2I2SVLxQcEitmE8LUZn7vA"
  title: "tvOS projects based on expo cannot install react-native-purchases"
  version: "skv_Jx4NuKJl1SpmvHC11BtStw"
  updated: "2026-10-03T05:58:46.382537+00:00"
  canonical_url: "https://vectle.com/skills/skl_2I2SVLxQcEitmE8LUZn7vA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

Fix first: upgrade react-native-purchases to 7.26.0 or newer. tvOS support was added there (member vegaro); the reporter confirmed it runs perfectly on 7.26.0.

1. Upgrade react-native-purchases to 7.26.0+.
2. Install on the tvOS project. Expected: it installs and runs.

When to use: a tvOS project based on expo cannot install react-native-purchases.

When not to use: other platforms (they were already supported).

Compatibility: react-native-purchases 7.26.0+. Reported in RevenueCat/react-native-purchases#947.

Variants:
- "react-native-purchases tvOS"
- "revenuecat expo tvos"
- "react-native-purchases 7.26.0"

Root cause: no tvOS support before 7.26.0.

Edge cases: none; the version gate is the whole story.

---

Source: [Vectle](https://vectle.com/skills/skl_2I2SVLxQcEitmE8LUZn7vA). Version: `skv_Jx4NuKJl1SpmvHC11BtStw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
