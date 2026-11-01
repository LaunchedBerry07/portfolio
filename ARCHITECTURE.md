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
| CSS partagé et styles propres aux pages | `assets/css/site.css`, `assets/css/clients-sectors.css`, `assets/css/profile.css`, `assets/css/services.css`, `assets/css/404.css` |
| Utilitaires CSS compilés | `assets/css/utilities.css` |
| Interactions globales | `assets/js/site.js` |\n| Configuration GitHub Pages / Jekyll | `_config.yml` |\n| Page d’erreur personnalisée | `404.html` (avec front matter Jekyll et chemins `relative_url`) |
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


## Page 404 — GitHub Pages

La page `404.html` est traitée par Jekyll afin que le filtre `relative_url` préfixe correctement les feuilles CSS, le JavaScript, le favicon et les liens internes. Cette précaution est nécessaire parce que le navigateur conserve l’URL inexistante demandée au lieu de naviguer réellement vers `/404.html`.

La valeur `baseurl` est définie dans `_config.yml` :
- `""` pour un User Site ou un domaine personnalisé publié à la racine ;
- `"/nom-du-depot"` pour un Project Site.

Le nom du dépôt n’étant pas connu au moment de la livraison, la configuration contient une valeur vide par défaut et documente explicitement le réglage requis pour un Project Site. Aucun autre fichier de page n’est modifié.


## Configuration GitHub Pages — adresse de publication

Le portfolio est publié à `https://launchedberry07.github.io/portfolio/`.
Même si le nom d'hôte est celui d'un compte GitHub, le chemin `/portfolio/`
correspond à un **Project Site**. Le fichier `_config.yml` doit donc contenir
`baseurl: "/portfolio"`. La page `404.html` utilise le filtre Jekyll
`relative_url` pour construire les chemins des ressources et des destinations
internes. Si le dépôt ou le chemin de publication change, `baseurl` doit être
mis à jour en conséquence.
