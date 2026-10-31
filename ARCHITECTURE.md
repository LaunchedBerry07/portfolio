# Architecture du site

| Contenu | Emplacement |
|---|---|
| Accueil | `index.html` |
| Services | `services/index.html` |
| Études de cas linguistiques | `portfolio/linguistic-case-studies/index.html` et les 12 fichiers de détail voisins |
| Projets techniques | `portfolio/technical-projects/index.html` et les 8 fichiers de détail voisins |
| Clients et secteurs | `clients-sectors/index.html` |
| Profil et CV | `profile/index.html` |
| Contact | `contact/index.html` |
| CSS partagé et styles propres aux pages | `assets/css/site.css`, `assets/css/clients-sectors.css`, `assets/css/profile.css`, `assets/css/services.css` |
| Utilitaires CSS compilés | `assets/css/utilities.css` |
| Interactions globales | `assets/js/site.js` |
| Images et futurs médias | `assets/images/` |
| Documents futurs | `assets/documents/` |

Les liens des composants de navigation et de pied de page utilisent des chemins relatifs calculés selon la profondeur de chaque page afin de fonctionner sur les GitHub Pages de type « project site ».


### Clients & Sectors — visual refinements (v10)
- The hero map asset is cropped to remove unused whitespace and give the illustration more visual presence in the right-hand column.
- The nine industry cards use a repeating three-colour sequence: Blue Green (`#087E8B`), Dark Pink (`#D14D72`) and Sky (`#5B96BD`). The sequence is evenly distributed across the nine sectors.


### Clients & Sectors — final hero artwork (v11)
- Replaced the world-map hero image with an original watercolor illustration focused on language and communication: paper airplane, English/French speech bubbles, documents and flowing connection lines.
- The hero visual uses a taller desktop display to avoid a shallow banner effect; on mobile it returns to a responsive 4:3 crop.
- The separate TransPerfect illustration and the three-colour sector-card sequence remain unchanged.


## Contact page — video hero

The Contact page uses a decorative, silent, portrait-oriented MP4 in the same organic editorial frame treatment as the Profile hero portrait. The source video is normalized to its displayed orientation and encoded without audio at `assets/video/contact-geometric-loop.mp4`. Its WebP poster is stored at `assets/images/contact/contact-video-poster.webp`. Playback is started only when the visitor has not enabled `prefers-reduced-motion`; otherwise the poster remains visible. The page-specific styles are in `assets/css/contact.css`.
