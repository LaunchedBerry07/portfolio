# Rapport de vérification — itération 2

## Vérifications terminées

- Les captures WebDev pleine page montrent la version actualisée aux viewports 1440 × 1000, 768 × 1024 et 390 × 844. Le contrôle visuel confirme l’annotation rose sous le titre, l’ornement fourni redimensionné entre titre et copie, les six cartes carrées avec leurs titres alignés et l’illustration 323144 dans la carte du projet personnel.
- Dimensions des exports : bureau 1440 × 6607 px; tablette 675 × 7500 px; mobile 246 × 7500 px. Le moteur de capture réduit les pages longues à une hauteur maximale de 7500 px; les images tablette/mobile couvrent la page complète mais sont réduites par rapport à leur largeur CSS d’origine.
- Les six illustrations de mandats sont presque carrées : 506 × 507, 504 × 507, 510 × 507, 506 × 509, 504 × 509 et 510 × 509 px. Le CSS leur donne un cadre commun 1:1; les attributs intrinsèques du HTML concordent avec les dimensions des fichiers.
- L’ornement conserve son alpha et son ratio : source 900 × 1350 px, sortie 600 × 900 px. L’image du projet est l’asset fourni en 1100 × 1100 px, affiché sans recadrage.
- `python3 tools/check_site.py` réussit : `lang=en`, un `h1`, six services, 36 éléments liés vérifiés, 12 images HTML et manifeste local correct.
- `node --check script.js` et `python3 -m json.tool manus-routes.json` réussissent. La page et les deux nouveaux fichiers WebP répondent en HTTP 200 sur le serveur local.
- La nouvelle phrase d’Expertise a été comparée à la formulation exacte demandée. La copie du projet Email-Triage n’a pas été changée.
- Le comportement clavier du menu n’a pas été modifié dans cette itération visuelle; l’essai clavier de l’itération précédente avait passé Entrée, Escape, retour du focus et activation du lien Services. Les captures de cette itération ont été vérifiées visuellement.

## Non vérifié / en attente

- Ce n’est pas une certification WCAG exhaustive; les contrastes ponctuels et tests clavier complets n’ont pas été répétés lors de cette itération.
- Le contrôle numérique de `scrollWidth` à chaque viewport n’a pas été relancé après les changements; aucun débordement n’est visible dans les captures.
- Les permissions de publication des témoignages, affiliations, noms de clients/marques et illustrations — y compris les deux nouveaux visuels — ne sont pas établies par le prototype; elles restent à confirmer avant publication publique.
- Aucun PDF de CV approuvé n’était fourni : l’entrée CV reste visible mais non cliquable.
- Les destinations des futures pages Services, Portfolio, Technology & AI, Projects et Profile, et la confirmation des coordonnées publiques, restent à définir.
- Aucun déploiement ou test sur un hébergement public n’a été effectué; le dépôt d’origine n’a pas été modifié.
