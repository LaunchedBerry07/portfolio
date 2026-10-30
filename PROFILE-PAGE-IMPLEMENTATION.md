# Profile & CV — intégration de la première direction visuelle

Date : 2026-10-30

## Portée

Cette livraison intègre la structure approuvée pour les trois premières zones de la page `profile/index.html` :

1. Hero avec portrait, présentation, mots-clés et appels à l'action;
2. The Profile avec composition éditoriale à deux colonnes;
3. A multidisciplinary path avec quatre cartes thématiques.

Les textes descriptifs utilisés dans ces zones proviennent du contenu déjà présent dans la page. Les résumés des quatre cartes sont des formulations condensées des thèmes et éléments de ce contenu; ils ne constituent pas une validation éditoriale définitive.

La section « Writing and editorial practice », la zone « How I work » et les sections suivantes ont été conservées dans leur structure et avec leur contenu existants. Leur refonte est reportée à une étape ultérieure.

## Préservation de la page d'accueil

La page d'accueil est hors périmètre de cette livraison. Les fichiers suivants n'ont pas été modifiés :

- `index.html`
- `assets/css/site.css`
- `assets/css/utilities.css`
- `assets/js/site.js`

Leurs empreintes SHA-256 ont été comparées avant et après l'intégration; elles sont identiques.

## Réutilisation du système graphique

Les cartes et le cadre du portrait réutilisent directement les classes existantes du site :

- `.organic-border`
- `.organic-border-pink`
- `.shadow-handdrawn`
- `.shadow-handdrawn-pink`
- `.shadow-handdrawn-seafoam`

Aucune définition de ces classes communes n'a été modifiée. Les nouvelles règles de mise en page sont isolées dans `assets/css/profile.css`, chargé uniquement par `profile/index.html`.

## Autres corrections locales

- Suppression des déclarations `DOCTYPE` dupliquées dans `profile/index.html` (une seule déclaration conservée).
- Correction du lien favicon de cette page vers `assets/images/favicon.webp`, seul fichier favicon présent dans le dépôt fourni.
- Ajout d'un seul repère `<main>` autour du contenu principal.

## Vérifications effectuées

- Structure HTML analysée : une déclaration DOCTYPE, un élément `main`, un seul `h1`, sections correctement appariées.
- Liens et ressources locaux de la page vérifiés : aucune référence manquante.
- Cibles des liens d'ancrage vérifiées.
- Feuille `profile.css` analysée : aucune erreur de syntaxe CSS détectée.
- JavaScript commun vérifié syntaxiquement avec `node --check`.
- Empreintes SHA-256 de la page d'accueil et des feuilles de style communes comparées : identiques.

Une vérification visuelle réelle dans un navigateur, notamment aux largeurs desktop, tablette et mobile, reste à effectuer dans l'environnement de développement avant publication. Aucun déploiement n'a été effectué.
