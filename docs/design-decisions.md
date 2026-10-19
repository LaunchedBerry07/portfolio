# Design decisions and asset map

## Design summary

The page uses an editorial portfolio language: expressive Georgia serif headlines, restrained sans-serif interface and body text, generous whitespace, asymmetrical but stable section layouts, fine rules and a deliberately selective palette. Navy anchors the content and contact area; Mist and white alternate across sections; Blue Green and Turquoise provide functional accents; Dark Pink appears selectively. No remote fonts, framework, illustration generation, pervasive gradients or decorative motion were added. CTA and button colors use darker shades derived from the official Blue Green and Dark Pink values where needed to meet text contrast.

The hero keeps the approved headline and copy in a clear left column. The network-globe illustration occupies the right side at a much larger scale than the small corner treatment in the reference mockups; on mobile it moves below the text and is resized rather than squeezed into the desktop layout.

The final contact block follows the supplied 321243.png reference: navy field, readable HTML text and buttons on the left, portrait/globe artwork integrated on the right, and CSS fades that merge the artwork into the navy surface. On mobile the artwork is recropped toward the portrait, with the text remaining on the darker left side. Supplied art and logos are preserved; the screenshot is not used as an image asset and contains no interface text embedded in the page artwork.

Service cards present all six approved groups, with Data Annotation as the sixth and the exact description supplied by the user. The selected-assignment section is text-led and uses no third-party logos or invented client deliverables. Independent/technical projects are described only at the scope approved in the homepage copy and remain clearly distinct from professional client assignments.

## Asset map

| Prototype asset | Supplied source | Homepage use | Treatment |
|---|---|---|---|
| `assets/images/hero-globe.webp` | `321055.webp` | Hero globe/network illustration | Reused unchanged; displayed on the pale hero surface with responsive object positioning; decorative image semantics (`aria-hidden`) |
| `assets/images/cta-portrait-globe.webp` | `321026.webp` | Integrated portrait/globe art in the final CTA | Reused unchanged; CSS `mask-image` applies a gradual blend into navy; hidden from assistive technology because the block is decorative alongside the CTA copy |
| `assets/images/logo-horizontal.png` | `321112.png` | Full SN globe and wordmark in the white header | Reused unchanged at its original proportions |
| `assets/images/brand-mark-white.png` | `321110.png` | White SN globe mark in the navy footer | Reused unchanged at its original proportions |
| `assets/images/brand-mark.png` | `321109.png` | Compact SN favicon | Reused unchanged |
| `assets/images/321134.webp` | `321134.webp` | Translation/localization service icon | Reused unchanged; decorative |
| `assets/images/321133.webp` | `321133.webp` | Editing/revision/proofreading service icon | Reused unchanged; decorative |
| `assets/images/321130.webp` | `321130.webp` | MTPE/linguistic QA service icon | Reused unchanged; decorative |
| `assets/images/321132.webp` | `321132.webp` | Terminology/editorial-control service icon | Reused unchanged; decorative |
| `assets/images/321129.webp` | `321129.webp` | Transcreation/content-adaptation service icon | Reused unchanged; decorative |
| `assets/images/321131.webp` | `321131.webp` | Data Annotation service icon | Reused unchanged; decorative |

The horizontal wordmark is used on white, where its dark typography and globe remain legible; the supplied white SN globe mark is used on navy. The separate source portrait is not used because the approved combined illustration better matches the supplied CTA reference. No third-party client logos are used. The provided screenshot `321243.png` served only as a layout reference.

## Copy and factual scope

The supplied English homepage draft is treated as final and approved per the user's instruction. The approved Data Annotation line is inserted verbatim. Headline statistics and project/assignment volumes are omitted. The six selected linguistic assignments and testimonials follow the approved draft. No detailed CV, project outcome, additional credential, client logo, or technical-case claim has been added.
