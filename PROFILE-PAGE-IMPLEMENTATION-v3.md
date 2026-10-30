# Profile & CV — Ajustement de l'icône

## Retour visuel
La capture fournie montre que l'icône cerveau de la carte « A thoughtful approach » apparaît trop petite et noire dans sa pastille.

## Correction
Dans `assets/css/profile.css`, une règle ciblée a été ajoutée :

- taille de l'icône portée à `1.5rem` (24 px);
- couleur Blue Green forcée avec `var(--bluegreen)`;
- alignement et dimensions de la pastille conservés.

La correction est locale à la page Profile & CV. Aucun fichier HTML/CSS/JS partagé ni fichier de la page d'accueil n'a été modifié.
