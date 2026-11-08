---
name: "factorytalk-optix-reusable-faceplate-p-7c2ce6c7ec774dda"
description: "FactoryTalk Optix reusable faceplate parameter passing: pass a different PLC tag to each faceplate instance"
metadata:
  skill_id: "skl_iSSET5ftHPqJEqhf-Wsi7Q"
  title: "FactoryTalk Optix reusable faceplate parameter passing: pass a different PLC tag to each faceplate instance"
  version: "skv_DsST9YLfx1PqeZL4F3Mxww"
  updated: "2026-11-08T12:01:02.311929+00:00"
  canonical_url: "https://vectle.com/skills/skl_iSSET5ftHPqJEqhf-Wsi7Q"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Start from the library pattern before building your own. Open the FactoryTalk Optix Library v5.30 motor or pump faceplate in Optix Studio and look at how it is structured: it is a reusable UI object whose controls are not bound to a fixed PLC tag. Success check: you can select the faceplate object itself and see the variable it exposes for the device.

Make your faceplate a reusable UI object. Select the panel or user control that holds the faceplate graphics and convert it into a reusable type in the UI library, so instances stay linked to the one definition. Success check: editing the type updates every instance, and the object can be dropped onto a screen more than once.

Add one object variable to the faceplate type. Give it a name like Device and set its type to the model or PLC tag type the faceplate controls (for example the motor data type), not to a plain string. This variable is the Optix replacement for a View parameter. Success check: the variable shows up as a property on each placed instance, separate from the internal controls.

Bind the insides relatively, never to a fixed tag. For each control inside the faceplate (run status, start button, speed value), bind its value to a member of the Device variable using a dynamic link that references the faceplates own variable, so the path is effectively Device dot member name. Success check: no binding inside the faceplate names a real PLC tag directly; every binding goes through Device.

Place one instance per device and set Device on each. Drop the faceplate onto the screen once per motor or pump, select each instance, and set its Device variable to that devices PLC tag (for example the first motor tag on instance one, the second motor tag on instance two). Success check: in the editor each instance shows a different Device value while sharing the same type.

Test with two different devices running. Download or run the project and change something on one device only (start the first motor, leave the second stopped). Success check: only the first faceplate shows that motor running; if both faceplates mirror the same device, an instance still points at the wrong tag or a binding was made absolute.

---

Source: [Vectle](https://vectle.com/skills/skl_iSSET5ftHPqJEqhf-Wsi7Q). Version: `skv_DsST9YLfx1PqeZL4F3Mxww`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
