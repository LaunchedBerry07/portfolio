# Portfolio — Stéphanie Nadeau

Site statique composé de 28 pages HTML. Les pages, les feuilles CSS et les scripts sont séparés; le CSS utilitaire compilé est inclus dans le dépôt. GitHub Pages utilise son traitement Jekyll natif uniquement pour résoudre les chemins de la page 404; aucun framework applicatif ni compilation du site n’est nécessaire.

## Arborescence

- `index.html` : accueil
- `services/` : services linguistiques
- `portfolio/linguistic-case-studies/` : index et 12 études de cas
- `portfolio/technical-projects/` : index et 8 projets techniques
- `clients-sectors/` : expérience sectorielle et organisations associées aux mandats linguistiques
- `profile/` et `contact/` : profil/CV et contact
- `assets/css/` : CSS compilé, styles communs et `404.css`
- `assets/js/site.js` : navigation mobile, année et filtres du portfolio
- `_config.yml` : configuration Jekyll et chemin de base GitHub Pages
- `assets/images/` : logo, illustrations intégrées et 15 emplacements SVG temporaires à remplacer par les visuels propres au portfolio
- `assets/documents/` : emplacement futur des documents téléchargeables
- `404.html` : page d’erreur personnalisée (traitée par Jekyll pour résoudre les chemins)
- `RAPPORT_LIVRAISON.md` : rapport des corrections et des vérifications de cette livraison

## Publier sur GitHub Pages

1. Déposez le contenu de ce dossier à la racine de votre dépôt GitHub.
2. Dans **Settings → Pages**, choisissez **Deploy from a branch**, la branche voulue et le dossier `/(root)`. Conservez le traitement Jekyll natif de GitHub Pages : le fichier `404.html` utilise le filtre `relative_url` pour que ses ressources et ses liens restent corrects sur une URL inexistante.
3. Vérifiez la valeur `baseurl` dans `_config.yml` :
   - User Site (`utilisateur.github.io`) ou domaine personnalisé à la racine : `baseurl: ""`.
   - Project Site (`utilisateur.github.io/nom-du-depot/`) : `baseurl: "/nom-du-depot"`.
4. Enregistrez et publiez la configuration. Aucun framework applicatif, serveur, base de données, plugin Jekyll ou outil de compilation supplémentaire n’est requis. Le CSS utilitaire déjà compilé reste directement servi depuis le dépôt.

Configuration actuelle : `baseurl: "/portfolio"`, cohérente avec le Project Site publié à `https://launchedberry07.github.io/portfolio/`.

Pour modifier les classes Tailwind et régénérer le fichier compilé, installez Node.js, puis exécutez `npm install` et `npm run build:css`. Le CSS compilé se trouve déjà dans `assets/css/utilities.css`; cette étape ne fait pas partie du déploiement GitHub Pages.

La navigation partagée comprend aussi un lien `Methodology` qui pointe vers la section correspondante de l’accueil. L’index technique référence les huit fiches de projet disponibles dans l’archive.

## Ajouter vos visuels

Les 15 emplacements SVG temporaires sont rangés par rôle sous `assets/images/`. Remplacez-les par les fichiers définitifs et mettez à jour le chemin et l’extension du `src` correspondant si le format change. Un lien « Download my CV » sans fichier fourni dans l’archive a été changé en demande par courriel; ajoutez le PDF dans `assets/documents/` puis liez-le si vous souhaitez offrir un téléchargement direct.

Les polices Google Fonts et Font Awesome restent chargées depuis leurs CDN publics; elles ne sont pas nécessaires à l’hébergement, mais leur chargement requiert une connexion réseau.


La page `clients-sectors/` utilise une illustration WebP dédiée au hero (`assets/images/clients-sectors/hero-language-connections.webp`). Le visuel de la section TransPerfect demeure distinct.


## Configuration actuelle de GitHub Pages

Cette version utilise `baseurl: "/portfolio"`, car le site est publié à `https://launchedberry07.github.io/portfolio/`. Il s'agit d'un Project Site au sens de GitHub Pages.
