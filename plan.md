# Plan — page Services de Stéphanie Nadeau

## Périmètre et décisions

Créer une page HTML statique autonome en anglais (`services.html`), à partir de la copie approuvée du document Services. La page doit présenter les six familles de services, leurs prestations et les tarifs 2026 confirmés, puis la méthode, les secteurs, l’appui technologique, les conditions tarifaires et un CTA de contact. Les notes éditoriales internes du DOCX ne sont pas du contenu public et ne seront pas publiées.

Réutiliser l’archive statique fournie comme base du site. L’accueil existant reste visuellement et éditorialement inchangé : seules les destinations `href` Services des navigations d’en-tête et de pied de page seront reliées à `services.html`, afin que la page soit accessible depuis le site. Aucun autre élément de l’accueil ne sera modifié.

## Direction artistique approuvée

Portfolio éditorial contemporain : titres serif expressifs (Playfair Display avec Georgia en repli), texte fonctionnel sans serif (Work Sans avec repli système), grille régulière et compositions asymétriques contrôlées. Alterner blanc, Mist `#EAF4F8` et accents pastel ; structurer avec Navy `#13293D` et Blue Green `#087E8B`, soutenir la fraîcheur avec Turquoise `#149E92` et Seafoam `#83E0D0`. Donner davantage de présence au rose `#D14D72` — accents de section, filets, repères, fonds pâles et CTA — car les visuels de hero et de fin sont plus discrets. Employer les illustrations fournies sans créer d’images supplémentaires ; globe/carte et avion de papier servent respectivement au hero et au CTA final.

La page reste longue mais navigable : ancrages vers les six services, blocs éditoriaux alternés et tarifs lisibles, notamment sur mobile. Les décorations ne portent pas d’information essentielle ; le focus clavier, le contraste, les textes alternatifs et le mouvement réduit sont pris en compte.

## Structure du projet

- `index.html` : accueil extrait à l’identique de l’archive, hormis les deux destinations de navigation Services (en-tête et pied de page).
- `services.html` : nouvelle page Services autonome, contenu anglais conforme au document.
- `assets/css/services-page.css` : styles propres à cette page ; `assets/css/styles.css` et `assets/js/script.js` restent réutilisés pour l’identité partagée et le menu mobile.
- `assets/img/services/` : les huit visuels fournis, préparés au besoin pour une intégration propre sans toucher aux originaux du projet partagé.
- `manus-routes.json` : déclaration des routes publiques `/` et `/services.html`.

## Livraison

Le serveur statique local écoute sur le port configuré 3000 pour Preview. Ne pas publier le site ; conserver les changements dans le projet et le checkpoint WebDev.