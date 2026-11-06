---
name: "qgis-layer-load-error-shapefile-shx-in-3a87c6c694a335dd"
description: "QGIS layer load error shapefile .shx index missing fails import: how to fix"
metadata:
  skill_id: "skl_SxO6s0ONrlmH6Ltq1Bj_ww"
  title: "QGIS layer load error shapefile .shx index missing fails import: how to fix"
  version: "skv_t3i4crJ1s8G7nrBWhxpsaA"
  updated: "2026-11-06T01:53:56.787935+00:00"
  canonical_url: "https://vectle.com/skills/skl_SxO6s0ONrlmH6Ltq1Bj_ww"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**List the folder contents next to the .shp file.** A working shapefile needs at least the .shp, .shx, and .dbf files with identical base names in the same folder. Expected: you can see which sidecar files are present and whether the .shx is missing, renamed, or in a different folder.

**Restore the .shx from the original source.** If the data came from a zip download or a shared drive, re-extract or re-copy the whole set rather than the .shp alone; file transfers that grab one file at a time are the usual cause. Success check: the .shx with the exact same base name sits beside the .shp and QGIS loads the layer without the error.

**Rebuild the index when the source copy is gone.** Run the GDAL check below against the .shp; when run with update access, ogrinfo rebuilds a missing .shx, and QGIS also ships a Repair shapefile tool in the Processing toolbox that does the same. Expected: a new .shx file appears with a recent timestamp.

**Check for a base name mismatch.** Files renamed by hand or by an email system can leave the index called by an old name, or with an uppercase extension the filesystem treats differently. Rename the sidecars so every file shares the .shp base name exactly. Success check: all sidecars line up and the layer loads.

**Verify the layer after loading.** Zoom to the layer extent and open the attribute table. Expected: features draw on the map and the attribute row count matches the source; an empty or zero extent result means the .shp geometry itself is damaged, not just the index.

**Convert a repaired layer to GeoPackage.** Once it loads, save it as a GeoPackage, a single file format with no sidecars, so the index problem cannot recur on the next transfer. Success check: the GeoPackage opens in a fresh QGIS project and shows the same feature count.

---

Source: [Vectle](https://vectle.com/skills/skl_SxO6s0ONrlmH6Ltq1Bj_ww). Version: `skv_t3i4crJ1s8G7nrBWhxpsaA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
