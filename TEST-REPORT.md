# Rapport de vérification

## Vérifications terminées

- La page répond sur le serveur statique local en HTTP 200; `manus-routes.json` répond en 200 avec du JSON valide et une route `/` correspondant à la page source.
- Captures pleine page Chromium : bureau 1440 × 1000 (fichier 1440 × 6856 px), tablette 768 × 1024 (768 × 9049 px) et téléphone 390 × 844 (390 × 12765 px). Les captures sont dans `screenshots/`.
- Aux largeurs CSS 1440, 768 et 390 px, la largeur du document demeure égale à celle du viewport : aucun débordement horizontal détecté.
- Les 11 images HTML se chargent; l’image du CTA portrait/globe se charge à chaque taille. Aucun lien d’ancre interne brisé n’a été détecté.
- Contrôle statique `python3 tools/check_site.py` : réussi — langue `en`, un seul `h1`, six cartes de services, phrases requises, liens internes, 11 images avec attribut alt, ressources locales et manifeste.
- Contrôle de syntaxe `node --check script.js` : réussi.
- Clavier mobile à 390 px : la touche Tab révèle le lien « Skip to content » et son focus visible; Entrée ouvre le menu; Escape le ferme et restitue le focus au bouton; l’activation clavier de Services ferme le menu et mène à `#services`.
- Contrastes de couleurs fonctionnelles échantillonnés : Navy/White 14,87:1; Navy/Mist 13,31:1; Blue Green/White 4,81:1; Seafoam/Navy 9,59:1. Le Dark Pink reste un accent de bordure ou un signe décoratif plutôt qu’un texte normal sur blanc.
- Relecture comparée à la copie anglaise fournie et au texte source de la page : les formulations reprises sont conservées; le sixième service porte exactement la description validée par l’utilisatrice.

## Non vérifié / en attente

- Ce rapport n’est pas une certification WCAG exhaustive; les contrastes sont des vérifications ponctuelles et les contrôles clavier couvrent principalement le menu et le lien d’évitement.
- Les permissions de publication des noms/marques de clients, témoignages et illustrations ne sont pas confirmées par les fichiers. Elles restent à valider avant toute publication publique.
- Aucun PDF de CV approuvé n’était fourni : il n’y a donc pas de téléchargement ni de lien CV actif; l’entrée est visible mais désactivée et documentée.
- Les pages Services, Portfolio, Technology & AI, Projects et Profile dédiées ne sont pas dans le dépôt reçu. La navigation du prototype utilise les sections locales correspondantes; leur future URL multipage reste à confirmer.
- L’adresse de courriel et l’URL LinkedIn reprises du site actuel sont visibles, mais leur accessibilité externe et leur confirmation comme coordonnées finales ne sont pas testées ici.
- Aucun déploiement/publication, test sur GitHub Pages réel ni contrôle juridique des marques/témoignages n’a été effectué, conformément au périmètre de prototype.
