# Profile & CV — Professional experience & Education (V7)

## Modifications
- Replaced the former two-column experience/education block with two dedicated, full-width sections.
- Added an introductory editorial paragraph for Professional experience.
- Highlighted the ongoing independent linguistic practice and author work in two primary cards.
- Presented four additional roles in a compact responsive grid: Accounting Clerk & Language-Services Support; Marketing & Web Development Consultant; Communications Manager; Document Production Assistant.
- Added three source-supported highlights to the linguistic experience card: 13+ years, 5,000+ assignments, and 200+ brands and organizations.
- Added a chronological education timeline with seven academic/vocational entries.
- Added two Google Skills courses under Continuing education.
- Added six TransPerfect Linguist Certifications in a separate compact list.
- Retained the following Industry experience and Tools/Languages section without content changes.

## Content fidelity
- Dates, institutions, employers, job titles, and quantitative claims were taken from the supplied resume text.
- The Accounting diploma is marked "In progress" because the supplied record gives an end date of December 2026.
- The four additional employment descriptions are condensed paraphrases of the supplied resume, not new claims.
- No audience-reach metric for the author activity or client names were added to this section.

## Styling and responsive behaviour
- Uses the existing brand palette and typography: Navy, Blue Green, Dark Pink, Mist; Playfair Display, Inter, and existing site icon font.
- Primary cards reuse `.organic-border`, `.organic-border-pink`, `.shadow-handdrawn`, and `.shadow-handdrawn-pink`.
- Secondary cards, education timeline, continuing education, and certifications have dedicated `.career-*` and `.education-*` styles scoped to this page.
- Layout collapses to one column on narrower screens; the education timeline keeps its date/description columns until small mobile widths.
- Semantic section headings, ordered education list, descriptive labels, and decorative icons hidden from assistive technology are used.

## Files changed
- `profile/index.html`
- `assets/css/profile.css`
- Added this implementation note.

## Protected files
The following files were compared byte-for-byte with the V6 archive and remain unchanged:
- `index.html` (homepage)
- `assets/css/site.css`
- `assets/css/utilities.css`
- `assets/js/site.js`

## Checks performed
- HTML parsed successfully.
- Six experience cards detected.
- Seven education entries detected.
- Two continuing-education entries detected.
- Six certification entries detected.
- Unique HTML IDs checked.
- CSS brace balance checked.
- Protected shared files verified byte-for-byte against V6.

## Not yet tested
- No browser-rendered screenshot or live responsive browser test was performed in this pass.
- Keyboard/focus and screen-reader behaviour should be checked in the browser before publication.
- Recheck the visual rhythm at desktop, tablet, and mobile widths before merging into the publication branch.
