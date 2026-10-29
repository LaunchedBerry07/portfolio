# Plan — site Stéphanie Nadeau

## Portée proposée

- Conserver la page d’accueil fournie comme fondation et l’adapter aux pages intérieures, à la navigation du site et à l’hébergement statique.
- Produire une page HTML intérieure pour chacun des 26 documents Word de `Website_Content.zip`. Cette interprétation donne 26 pages intérieures + l’accueil existant, soit 27 pages au total.
- Reprendre le texte source en anglais, langue des documents et du prototype, sans le remplacer par du texte générique.
- Ajouter des espaces réservés facilement remplaçables pour portrait, images de projets et logos; aucune illustration finale n’est requise à cette étape.
- Livrer un site en HTML/CSS statique, sans serveur, base de données, framework ou JavaScript d’exécution, utilisable sur GitHub Pages.

## Inventaire des pages intérieures

| Fichier | Source / contenu |
| --- | --- |
| `contact.html` | Contact |
| `caifan-accounting.html` | Projet Caifan : système comptable et automatisation |
| `sims4-linguist-career.html` | Mod de carrière linguistique The Sims 4 |
| `databerry.html` | Projet technique DataBerry |
| `databerry-nexus.html` | Projet DataBerry Nexus |
| `drive-to-notion.html` | Pipeline de migration Drive vers Notion |
| `llm-prompt-engineering.html` | Ingénierie de prompts LLM |
| `literary-voice-modeling.html` | Modélisation de voix littéraire |
| `email-triage.html` | Filtrage de sollicitations par courriel |
| `linguistic-case-studies.html` | Vue d’ensemble des études de cas linguistiques |
| `about.html` | Profil et CV de Stéphanie Nadeau |
| `services.html` | Services linguistiques |
| `wsp-global.html` | Étude de cas WSP Global |
| `us-bank.html` | Étude de cas US Bank |
| `thomson-technology.html` | Étude de cas Thomson Technology |
| `rem-international.html` | Étude de cas REM International Mechanics |
| `public-works-gsc.html` | Étude de cas Public Works / GSC |
| `polaris-industries.html` | Étude de cas Polaris Industries |
| `nakanishi.html` | Étude de cas Nakanishi |
| `federation-adventiste.html` | Étude de cas Fédération adventiste |
| `rga.html` | Étude de cas RGA |
| `bell-media.html` | Étude de cas Bell Media |
| `beholder.html` | Étude de cas Beholder |
| `ford-build-price.html` | Étude de cas Ford Build & Price |
| `ai-linguistic-technologies.html` | IA et technologies linguistiques |
| `technical-projects.html` | Vue d’ensemble des projets techniques |

## Approche d’implémentation

- Utiliser des fichiers HTML5 indépendants au même niveau que `index.html`, avec une feuille commune `styles.css` et des liens relatifs (`./nom-de-page.html`) afin que les URLs fonctionnent aussi sous un sous-chemin de projet GitHub Pages.
- Réécrire le balisage de la page d’accueil à partir du prototype fourni en conservant ses sections, sa hiérarchie et son contenu, puis remplacer les liens provisoires par les pages correspondantes.
- Construire les 26 pages avec une ossature éditoriale cohérente (en-tête/navigation, titre, résumé et métadonnées lorsque disponibles, contenu fidèle au document source, appels à l’action et pied de page). Les études de cas et projets conservent leurs propres titres, listes et données.
- Créer des placeholders visuels locaux et textuels, balisés pour être faciles à remplacer par des fichiers image et logos finaux. Aucun visuel externe ou généré ne sera nécessaire.
- Ajouter `README.md` avec les instructions GitHub Pages pour publier la racine du dépôt et les conventions de remplacement des placeholders. Ajouter `manus-routes.json` pour déclarer les 27 routes à l’aperçu.

## Structure prévue

```text
/home/ubuntu/stephanie/
├── index.html
├── contact.html, about.html, services.html, ... (26 pages intérieures)
├── styles.css
├── brand-placeholder.svg
├── manus-routes.json
├── README.md
├── _config.yml
├── app.config.ts
├── plan.md
└── TODO.md
```

## Direction artistique appliquée

- **Mouvement :** « L’Éditorial Vivant & Humaniste », collage structuré, tel que décrit dans le guide et illustré par les captures de l’accueil.
- **Principes :** information facile à parcourir; ton humain et précis; espace blanc généreux; touches dessinées à la main au service de la clarté.
- **Couleurs :** Navy `#13293D` pour le texte et les fonds contrastés; Dark Pink `#D14D72` pour les appels à l’action et accents; Blue Green `#087E8B` et Turquoise `#149E92` pour navigation et repères; Seafoam `#83E0D0` pour accents doux; Mist `#EAF4F8` et fond `#FAFCFD` pour la lumière; Sky `#5B96BD` pour métadonnées.
- **Mise en page :** hiérarchie de magazine, sections à largeur confortable, compositions éditoriales décentrées et panneaux/carnets de projet, plutôt qu’un seul bloc uniforme. Les cartes structurent le contenu sans sacrifier l’espace blanc.
- **Motifs :** bordures organiques et ombres décalées, soulignements/doodles en rose, pastilles et annotations manuscrites, placeholders identifiés.
- **Interactions :** navigation par liens HTML natifs; états de survol/focus visibles; menu mobile sans JavaScript; animation décorative discrète désactivable avec `prefers-reduced-motion`.
- **Typographie :** Playfair Display pour les titres, Inter pour le texte courant, Caveat pour les annotations; piles de remplacement système si les polices distantes sont indisponibles.
- **Essence de marque :** spécialiste bilingue aidant les équipes à produire un français canadien exact, naturel et cohérent en contexte; personnalité précise, chaleureuse et méthodique.
- **Voix :** éditoriale, concrète et attentive au contexte. Exemples : « Language that works in context. » et « The right words belong to the work they support. »
- **Wordmark/logo :** conserver le repère monogramme SN inspiré de l’accueil comme placeholder stylisé remplaçable par le logo final.
- **Couleur de marque distinctive :** Dark Pink `#D14D72`.

## Dépendances et hébergement

- Aucun serveur, framework, base de données, étape de compilation ou JavaScript requis pour le site publié.
- La feuille CSS commune et les pages seront servies directement depuis la racine du dépôt GitHub Pages. Les chemins d’images définitifs pourront être insérés localement sans changer d’architecture.
- Les polices et icônes externes restent des améliorations facultatives; les piles de repli assureront la lisibilité sans elles.
