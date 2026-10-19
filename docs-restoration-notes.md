# Restoration pass — 2026-10-19

## Decisions applied
- Base restored from the earlier `Portfolio_Home_v2.zip` rather than the Manus-inspired single-page structure.
- Hero uses the supplied globe-only illustration at a contained 3:2 ratio; the repeated `Language that works in context` note is removed. Hero primary CTA is navy; CTA-section primary action remains pink.
- Profile has three columns on wide screens: heading, existing approved body copy, and the exact quote: “A sentence can be perfectly correct in isolation and still fail within the larger system it belongs to.”
- Pink/turquoise short rules are applied below section headings.
- Six illustrated linguistic assignment cards are preserved. Since the standalone case-study pages are not part of this homepage-only prototype, cards are not linked to missing pages.
- A four-column principles band and five-step quality band create repeated multi-column structures alongside the service and assignment grids. Their labels are descriptive proposals, not claims or statistics.
- Technology & AI uses a two-column layout: explanatory title/body/actions on the left, the Email Triage project card on the right. The marginal note is unchanged: “Independent and internal projects are distinct from professional client assignments.” It is styled as handwritten HTML text, not embedded in an image.
- CTA uses the supplied portrait/globe composite and CSS masking to blend it into the navy background.
- Footer and navigation retain the earlier composition. CV is visible but intentionally not interactive because its destination is out of scope for this homepage-only prototype.

## Validation
- HTML parsed: one H1, no duplicate IDs.
- All 16 local image references exist.
- All in-page anchors resolve; no missing local destinations detected.
- JavaScript syntax check passed with `node --check`.
- Chromium screenshot attempt timed out in this environment; no claim of visual browser validation is made. Manual visual review at desktop/tablet/mobile widths remains necessary.
- Not deployed or pushed to GitHub.
