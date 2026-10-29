# Portfolio — Stéphanie Nadeau

Site statique issu des 26 pages de l’archive d’origine. Les pages, les feuilles CSS et les scripts sont séparés; le CSS utilitaire compilé est inclus dans le dépôt pour permettre un hébergement direct, sans serveur, build ni framework côté GitHub Pages.

## Arborescence

- `index.html` : accueil
- `services/` : services linguistiques
- `portfolio/linguistic-case-studies/` : index et 12 études de cas
- `portfolio/technical-projects/` : index et 8 projets techniques
- `profile/` et `contact/` : profil/CV et contact
- `assets/css/` : CSS compilé et styles communs
- `assets/js/site.js` : navigation mobile, année et filtres du portfolio
- `assets/images/` : visuels temporaires locaux et emplacements des futurs médias
- `assets/documents/` : emplacement futur des documents téléchargeables
- `404.html` : page d’erreur assortie au site
- `manus-routes.json` : inventaire des 26 routes du site

## Publier sur GitHub Pages

1. Déposez le contenu de ce dossier à la racine de votre dépôt GitHub.
2. Dans **Settings → Pages**, choisissez **Deploy from a branch**, la branche voulue et le dossier `/(root)`.
3. Toutes les URLs internes et les chemins CSS/images sont relatifs : le site fonctionne donc aussi bien à la racine d’un domaine qu’à l’adresse de projet `https://utilisateur.github.io/nom-du-depot/`. Aucun `baseurl`, serveur, base de données, action GitHub ou outil de compilation n’est requis pour servir le site livré.

Pour modifier les classes Tailwind et régénérer le fichier compilé, installez Node.js, puis exécutez `npm install` et `npm run build:css`. Le CSS compilé se trouve déjà dans `assets/css/utilities.css`; cette étape ne fait pas partie du déploiement GitHub Pages.

La navigation partagée comprend aussi un lien `Methodology` qui pointe vers la section correspondante de l’accueil. L’index technique référence les huit fiches de projet disponibles dans l’archive.

## Ajouter vos visuels

Les visuels SVG temporaires sont rangés par rôle sous `assets/images/`. Remplacez-les par vos fichiers définitifs et mettez à jour le chemin et l’extension du `src` correspondant si le format change. Un lien « Download my CV » sans fichier fourni dans l’archive a été changé en demande par courriel; ajoutez le PDF dans `assets/documents/` puis liez-le si vous souhaitez offrir un téléchargement direct.

Les polices Google Fonts et Font Awesome restent chargées depuis leurs CDN publics; elles ne sont pas nécessaires à l’hébergement, mais leur chargement requiert une connexion réseau.
