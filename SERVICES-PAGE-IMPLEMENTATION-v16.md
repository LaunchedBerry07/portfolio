# Services page — implementation v16

## Scope
Updated `services/index.html` to reflect the approved editorial hierarchy and visual proposal. This implementation preserves the existing static multi-page architecture and reuses the current illustration assets.

## Files changed
- `services/index.html` — rebuilt page structure and copy; removed duplicate Clients & Sectors navigation link; corrected favicon reference; consolidated all 2026 rates into one accessible table; replaced the full sector inventory with a concise overview linking to Clients & Sectors.
- `assets/css/services.css` — new page-specific responsive styles.

## Editorial decisions implemented
- Canadian French is identified as the primary specialization, without implying it is the only French variety used. Quebec French, European French and International French are also named.
- Four core language-service pillars are given visual priority: Translation & Localization; Editing, Comparative Revision & Proofreading; MTPE & Linguistic QA; Terminology Management & Editorial Control.
- Creative Adaptation & Writing and Audiovisual & Multimedia are presented as complementary services.
- Guideline-Based Data Annotation is visually secondary and explicitly limited to entry-level, rubric-based tasks.
- Technology is presented as a supporting capability, not as an equivalent primary service offering.
- The detailed sector inventory is replaced with a short experience statement and a link to the Clients & Sectors page.
- Existing rate values and commercial terms were carried over unchanged from the Services page and the 2026 rate card source. They remain subject to reconfirmation before publication.

## Visual implementation
- Reuses `assets/images/general/hero-language-illustration-transparent.webp` for the hero.
- Reuses all six existing service illustrations in `assets/images/services/`.
- Reuses `assets/images/portrait/cta-language-globe.jpg` in the final contact section.
- Adds no image assets, JavaScript dependencies or framework dependencies.
- Uses a dedicated `services.css` file; shared site CSS and JavaScript were not changed.
- Retains the existing service anchor IDs where applicable for deep-link continuity.

## Static checks performed
- HTML parsed with Python's standard HTML parser.
- No duplicate element IDs detected.
- All images have an `alt` attribute; decorative service illustrations use empty alternatives.
- All local links and image paths in the Services page resolve to existing files or directories in the supplied project.
- Source image dimensions were checked and intrinsic width/height attributes are declared.
- A browser-rendered desktop/mobile test could not be completed in this environment: Chromium navigation was blocked by the execution environment. Responsive layout and keyboard interaction should therefore receive a final browser check before publication.

## Publication checks still required
- Reconfirm 2026 rates and terms.
- Inspect desktop, tablet and mobile rendering in a normal browser.
- Test keyboard navigation, mobile menu, anchor navigation and external font/icon loading.
- Check browser console and actual GitHub Pages project-site paths after deployment preview.
