# Rapport de livraison — Portfolio Stéphanie Nadeau

Date : 2 novembre 2026  
Périmètre : corrections d’accessibilité, de structure HTML, de typographie, de navigation et de responsive design.

## 1. Corrections livrées

### Contraste et lisibilité

- Remplacement des nuances d’accent utilisées comme texte par des variantes conformes au contraste WCAG AA sur fond blanc et Mist.
- Conservation des couleurs de marque d’origine pour les bordures, aplats et éléments décoratifs qui ne portent pas de texte.
- Assombrissement contrôlé de l’aplat `darkpink` lorsqu’il porte du texte blanc.
- Chargement explicite des graisses Inter 300, 400, 500, 600 et 700 sur les 28 pages.
- Suppression des tailles de texte mobiles extrêmes dans le panneau Ford : les textes concernés restent à une taille lisible sur les écrans étroits.

### Hiérarchie des titres

- Promotion des titres de section qui commençaient directement à `h3` après le `h1`.
- Passage en `h3` des sous-sections de contenu qui étaient artificiellement marquées `h4`.
- Correction de la section « Industry Experience » afin que Caveat ne soit plus utilisé comme police principale d’un titre structurel.
- Vérification automatisée : un seul `h1` par page et aucun saut de niveau détecté dans les 28 pages.

### Structure sémantique et clavier

- Ajout d’un unique `<main id="main-content">` sur les pages qui en étaient dépourvues.
- Ajout d’un lien d’évitement commun « Skip to main content » sur les pages concernées.
- Ajout d’un style commun qui révèle le lien d’évitement au focus clavier.
- Ajout de `scroll-margin-top` pour que la cible du lien reste visible sous la navigation sticky.
- Conservation des traitements spécifiques déjà présents sur la page 404 et l’étude Polaris.

### Validité HTML et ressources

- Suppression des DOCTYPE dupliqués : exactement un `<!DOCTYPE html>` par page.
- Normalisation des favicons vers le fichier local `assets/images/favicon.webp` avec le type MIME correspondant.
- Suppression de la fermeture invalide `</img>` dans l’étude Ford.
- Vérification des attributs `aria-current` existants sur les navigations de section.

### Responsive et repli fonctionnel

- Correction du menu mobile : il n’est masqué par CSS qu’après l’initialisation JavaScript. Sans JavaScript, la navigation reste accessible.
- Conservation de la synchronisation `aria-expanded`, du libellé du bouton et de l’icône lors de l’ouverture et de la fermeture du menu.
- Passage du panneau Ford en colonne unique sous 767 px afin d’éviter une illustration et un texte comprimés côte à côte.
- Réduction des risques de débordement horizontal des visuels de la page Services : largeur maximale limitée à 100 % du conteneur.

## 2. Vérifications effectuées

- 28 pages HTML analysées.
- 28 landmarks principaux contrôlés : un seul `<main id="main-content">` par page.
- 28 DOCTYPE contrôlés : un seul par page.
- 0 ancienne référence `favicon.svg` restante.
- 0 balise `</img>` restante.
- Ratios contrôlés : `#A62F52` sur blanc 6,67:1 ; `#006B76` sur blanc 6,24:1 ; `#006B76` sur Mist 5,59:1 ; `#315E78` sur blanc 6,99:1.
- Vérification des 28 pages pour le chargement complet des graisses Inter.
- Syntaxe JavaScript contrôlée avec `node --check`.
- Équilibre des accolades contrôlé dans les feuilles CSS.
- Contrôle HTML avec le parseur standard Python sans anomalie signalée.
- Vérification ciblée du repli du menu mobile sans JavaScript.

## 3. Limites connues

- La validation visuelle réelle dans plusieurs largeurs de viewport et avec un lecteur d’écran n’a pas été exécutée dans cette passe. Les contrôles livrés sont statiques et automatisés.
- Les polices Google Fonts et Font Awesome restent chargées depuis leurs CDN publics, comme dans la version précédente.
- À la date de cette livraison initiale, le nom du dépôt GitHub Pages et le `baseurl` restaient à confirmer. Mise à jour du 2 novembre 2026 : la copie auditée utilise `baseurl: "/portfolio"`, cohérent avec l’URL indiquée dans le README.
- Les textes et visuels métier n’ont pas été réécrits ni remplacés.

## 4. Contenu de l’archive

L’archive contient le site statique complet : pages HTML, feuilles CSS, JavaScript, images, documents, configuration Jekyll, inventaire des routes et ce rapport de livraison. Les scripts temporaires d’application des corrections ne sont pas inclus dans le site livré.


## 5. Mise à jour de suivi — 2 novembre 2026

Depuis la livraison initiale, les corrections P1 ciblées ont été appliquées à cette copie : contraste des états actif/survolé du menu, menu compact sur tablette, lien d’évitement avant la navigation et corrections de débordements mobiles. Le balayage responsive a couvert 28 fichiers HTML à six largeurs (168 rendus) sans débordement horizontal du document ou du corps; les scénarios clavier ciblés du menu, des CTA et des filtres ont réussi.

La passe P2 a corrigé les contrastes signalés et harmonisé le README, l’architecture, le TODO et les références de baseurl. L’audit Axe n’a relevé aucune violation de contraste sur 84 rendus ni dans 13 états interactifs. Il a toutefois laissé 258 occurrences « incomplètes » à examiner manuellement en raison de fonds complexes, d’images, de pseudo-éléments et de chevauchements. L’annotation Contact corrigée reste dans son illustration et présente un contraste de 9,59:1 contre le panneau sombre à 390 et 1 440 px.

Ces résultats ne remplacent pas un essai avec lecteur d’écran ni une validation WCAG complète. Les cas Axe incomplets, l’approbation des contenus et visuels métier, la décision concernant les CDN et la vérification sur l’hébergement réel restent à traiter. Aucune publication ni modification distante n’a été effectuée.
