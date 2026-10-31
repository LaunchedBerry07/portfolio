# Services page update — v17

## Scope

Targeted visual refinement of the Services page, based on the four user-supplied reference images. No other page was intentionally redesigned.

## Changes

1. Replaced the three Font Awesome symbols in the Audiovisual & Multimedia card with the supplied clapperboard / headphones / playback illustration, exported as optimized WebP.
2. Replaced the Services hero globe illustration with the supplied geometric-tray illustration. The source's left text-safe area was cropped from the image asset so the tray occupies the available hero column at a comparable visual scale to the previous globe.
3. Replaced the Services CTA image with the supplied paper-plane / globe illustration. The crop retains both the paper plane and the globe; the globe is enlarged through the new crop and display sizing.
4. Corrected the four-card core-services layout: cards now size to their own content rather than stretching to the height of the tallest card in each grid row. This removes excessive empty space inside the Translation & Localization and Terminology cards without adding filler copy or changing approved wording.

## Files changed

- `services/index.html`
- `assets/css/services.css`
- `assets/images/services/audiovisual-multimedia-clapperboard.webp` (new)
- `assets/images/general/hero-geometric-language-context.webp` (new)
- `assets/images/portrait/cta-paper-plane-globe.webp` (new)
- `assets/images/services/README.md`

## Asset preparation

The three supplied illustrations were exported to WebP and resized/cropped for their actual display contexts. The original illustrations remain available in the conversation attachments; only optimized WebP assets are included in the site archive.

## Validation

- Confirmed all image references in `services/index.html` resolve to files in the archive.
- Confirmed the previous hero and CTA image references are no longer used on Services.
- Confirmed the old three-icon Audiovisual markup and corresponding CSS are removed.
- Confirmed four core-service cards remain present.
- Confirmed the new image files are valid WebP images and recorded their dimensions and sizes.
- CSS/HTML structural checks completed.
- A headless Chromium screenshot attempt timed out in the execution environment; desktop/mobile visual rendering therefore remains unverified.

## Not changed

- Service copy and approved language-variety positioning.
- Rates and commercial terms.
- Other portfolio pages, including Clients & Sectors.
- Site dependencies and JavaScript.
