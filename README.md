# Stéphanie Nadeau — Homepage prototype

An independent static homepage prototype for GitHub Pages. It uses semantic HTML, plain CSS and a small JavaScript file for the mobile navigation. There is no build step, server-side component, analytics, cookie, API or external dependency.

## Local preview

From this directory, run:

```sh
python3 -m http.server 4173
```

Then open <http://localhost:4173>.

## Files

- `index.html` — homepage markup and approved English copy
- `css/styles.css` — palette, typography, responsive layout and component styling
- `js/site.js` — accessible mobile navigation
- `assets/images/` — supplied logo and illustrations, plus service icons
- `screenshots/` — captures from the previous prototype version; these are not screenshots of the newest direction review
- `docs/direction-review-2026-10-19.md` — design decisions and technical project claims boundaries
- `docs/test-report.md` — automated checks and remaining visual QA

## Current review scope

The current iteration retains the preferred hero, language-service cards, selected assignments, CTA, footer, navigation and global typography. It adds a four-column working-principles band, a five-step approach band, and a featured technical-project card under Technology & AI.

The project card describes a personal Gmail automation built with Google Apps Script and JavaScript. It is not presented as a trained AI model or validated security detector. See the direction review notes before publishing any implementation details.

## Publication status

This is a review prototype only. It has not been deployed, published or merged into the source portfolio repository. The CV destination and detailed standalone pages remain outside this homepage prototype.
