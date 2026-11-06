# Contact page implementation — v1

## Scope
Updated only the Contact page and added its page-specific visual assets and styles. The rest of the site is retained from `portfolio-main-services-update-v18.zip`.

## Changes
- Reorganized the Contact introduction into a two-column hero.
- Reused the organic border and offset seafoam shadow treatment from the Profile hero portrait for the video frame.
- Added decorative handwritten annotations around the frame.
- Integrated the supplied geometric animation as a silent, looping MP4.
- Normalized the source video's display orientation and removed its audio track.
- Added a WebP poster and a reduced-motion fallback that displays the still image instead of playing the video.
- Preserved the existing language-services checklist, workflow-project information, email, LinkedIn, location and confidentiality note.
- Updated the hero copy to identify Canadian French as the specialization while also naming Quebec French, European French and International French.
- Removed the duplicate Clients & Sectors navigation item and corrected the favicon reference to the existing WebP asset.
- Added page-specific responsive CSS and a meta description.

## Files changed or added
- `contact/index.html`
- `assets/css/contact.css` (new)
- `assets/video/contact-geometric-loop.mp4` (new)
- `assets/images/contact/contact-video-poster.webp` (new)
- `assets/images/contact/README.md` (new)
- `ARCHITECTURE.md`

## Dependencies
No new runtime or build dependencies.

## Verification
Structural HTML, local asset paths, duplicate IDs, CSS parsing, video orientation, video codec and absence of an audio stream were checked programmatically. Browser rendering, real-device playback and GitHub Pages deployment were not performed in this environment.


## Video replacement — v20
The initial Contact hero clip was replaced with the user's corrected upload (`329814.mp4`). The new source is 728 × 720 px at 24 fps and 7.936 seconds. The encoded web copy retains the near-square composition, has no audio track, and uses the updated WebP poster. The frame aspect ratio was adjusted accordingly to avoid cropping the new composition.
