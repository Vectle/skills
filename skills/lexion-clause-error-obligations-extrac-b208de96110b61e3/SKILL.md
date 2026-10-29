---
name: "lexion-clause-error-obligations-extrac-b208de96110b61e3"
description: "Lexion clause error obligations extraction misses renewal notice period"
metadata:
  skill_id: "skl_EZwHb51eEmBBRK66NmzwYw"
  title: "Lexion clause error obligations extraction misses renewal notice period"
  version: "skv_EyMb-Y7FXGf_zOq7Emi_TA"
  updated: "2026-10-29T01:54:58.684147+00:00"
  canonical_url: "https://vectle.com/skills/skl_EZwHb51eEmBBRK66NmzwYw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open the executed agreement in Lexion and confirm you are looking at the final signed version, not an earlier redline. Expected: the document status shows executed or fully signed, and the renewal clause text is present in the rendered document.

Search the document text for "notice" within the renewal and termination sections. Expected: you find the notice window stated in days (for example 90 days) in the renewal clause itself or in a separate termination-for-non-renewal clause.

Open the clause in the obligations extraction view and inspect the highlighted source spans. Expected: the renewal span is highlighted but the sentence carrying the notice window is not part of the extracted span, which confirms the extractor split the clause.

Check whether the notice sentence references a defined term or another section (for example "as set out in Section 8.2"). Expected: if a cross-reference exists, the extractor treated the two sections as unrelated clauses, so the notice period never joined the renewal obligation.

Re-run extraction on the document once. Expected: either the notice deadline appears with the correct offset from the term end date, or the field stays blank, which confirms a manual correction is needed rather than a processing retry loop.

Manually edit the obligation: set the notice deadline to the term end date minus the notice days from the clause text, and link the source span to the sentence that states the notice window. Expected: the obligations table now shows both the renewal date and an earlier notice deadline, and the calendar reminder fires on the notice deadline.

Verify downstream: open the renewals report or dashboard widget that consumes obligations. Expected: the contract appears in the upcoming notice window list for the correct quarter, not only in the renewal date list.

---

Source: [Vectle](https://vectle.com/skills/skl_EZwHb51eEmBBRK66NmzwYw). Version: `skv_EyMb-Y7FXGf_zOq7Emi_TA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
