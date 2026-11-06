# Portfolio page update — v23

## Scope
Updated only the linguistic case-studies listing page and its page-specific filtering/style assets. The shared navigation, footer, other pages, individual case-study pages, and technical-projects section were left unchanged.

## Changes
- Integrated all 12 user-supplied editorial illustrations as optimized WebP files (1536 × 1147 source dimensions).
- Added meaningful English alternative text and lazy loading for the card images.
- Introduced a responsive organic card rhythm while keeping all 12 case studies in the same grid and available by default.
- Replaced the previous single-category filter controls with multi-select service-family filters: Translation & Localization, Editing & Proofreading, and MTPE & Linguistic QA. Matching uses OR logic.
- Added an All projects reset and a live visible-case count.
- Removed the explanatory note about editorial illustrations; retained the documented word-volume qualification.
- Corrected the page's repeated DOCTYPE declarations and favicon path.
- Corrected the Portfolio statistic label to make clear that the eight sectors refer to the selected cases.

## Image mapping
Bell Media, Nakanishi, Public Works / GSC, Fédération adventiste du Québec, WSP Global, Thomson Technology, U.S. Bank, RGA Reinsurance Group, R.E.M. International Mechanics, Beholder, Polaris Industries, Ford.

## Validation performed
- Confirmed 1 DOCTYPE declaration.
- Confirmed 12 case-study cards and 12 image references.
- Confirmed all local image, stylesheet, script, and case-study-page links referenced by the Portfolio page resolve within the archive.
- Confirmed JavaScript syntax with `node --check`.
- Confirmed all 12 optimized WebP images retain 1536 × 1147 dimensions.

## Not performed
No live GitHub Pages deployment, browser-based responsive visual test, keyboard interaction test, or screen-reader test was performed in this update.

## Note on filter assignments
The service-family mapping is a working classification derived from the existing case-study descriptions and metadata. It should be reviewed if any mandate's actual service scope differs from the published description.
