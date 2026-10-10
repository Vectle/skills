---
name: "skunotavailable-the-requested-vm-size-af6379a11ad63762"
description: "Diagnoses the Azure SkuNotAvailable error when a VM size is not offered in the chosen region or zone. Use when an agent sees this during VM creation or scale operations. Covers listing available SKUs per location, picking a nearby region, and zone constraints. Not for quota errors or allocation failures."
metadata:
  skill_id: "skl_cxcM9oWSzCpRe3j6jiKbpg"
  title: "SkuNotAvailable: The requested VM size is not available in the location"
  version: "skv_ZCr-AxjaZKetThHdeERZxA"
  updated: "2026-10-03T04:48:35.50166+00:00"
  canonical_url: "https://vectle.com/skills/skl_cxcM9oWSzCpRe3j6jiKbpg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# SkuNotAvailable: The requested VM size is not available in the location

## TL;DR
That VM size simply is not sold in that region (or zone). List what the location actually offers, pick a size that exists there, or move the deployment to a region that has your size.

## The error
```
SkuNotAvailable: The requested VM size 'Standard_D2s_v5' is not available in location 'westus'. Please try another size or deploy to another location.
```

## Fix it
1. List what the location offers: `az vm list-skus --location [region] --size [size] -o table`. Expected: you see whether the size exists there at all.
2. If the size is missing, pick the closest available size in the same region. Expected: the new size shows up in the SKU list.
3. If you need that exact size, check nearby regions with the same command and move the deployment. Expected: the target region lists your size.
4. Check zone constraints. Some sizes exist in a region but not in every zone. Expected: the SKU list shows which zones carry it.
5. Redeploy with the available size or region. Expected: the VM provisions.

## When to use this
- An agent sees SkuNotAvailable during VM creation, scale-out, or image builds.
- A template that worked in one region fails in another.

## When NOT to use this
- OverconstrainedAllocationRequest or AllocationFailed. Those mean the size exists but capacity is temporarily gone; waiting or retrying can work.
- Quota errors. Those name the quota, not the SKU.

## Compatibility
- Azure Virtual Machines, all regions. SKU availability changes over time, so re-check.

### Variant phrasings
- "SkuNotAvailable"
- "The requested VM size is not available in location"
- "Please try another size or deploy to another location"

## Root cause
Azure does not sell every VM size in every region or zone. Newer sizes roll out region by region, and some sizes are retired per region. Templates copied between regions hit this the moment they land somewhere the size was never offered.

## Edge cases
- Spot and reserved capacity follow different availability. A size can be available on-demand but not for spot.
- The portal's size picker sometimes lags the API. Trust `az vm list-skus` over the dropdown.


---

Source: [Vectle](https://vectle.com/skills/skl_cxcM9oWSzCpRe3j6jiKbpg). Version: `skv_ZCr-AxjaZKetThHdeERZxA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
