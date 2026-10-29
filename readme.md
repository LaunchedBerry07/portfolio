# Site Stéphanie Nadeau — Services linguistiques

Ce dépôt contient un site statique en HTML et CSS : la page d’accueil (`index.html`) et 26 pages intérieures, pour 27 pages au total. Les textes du site sont en anglais afin de respecter les documents de contenu fournis.

## Publication sur GitHub Pages

Aucune compilation ou dépendance serveur n’est requise. Dans GitHub, ouvrir **Settings → Pages**, choisir **Deploy from a branch**, sélectionner la branche de publication (par exemple `main`) et le dossier **/(root)**. Une fois le déploiement terminé, GitHub Pages sert directement `index.html`, les autres fichiers HTML, le favicon et `styles.css`. Le `_config.yml` exclut du site publié les notes de planification, le README et les métadonnées internes de WebDev.

Tous les liens entre pages sont relatifs; le site fonctionne donc aussi bien à la racine d’un domaine qu’au sous-chemin d’un site de projet GitHub Pages. Pour prévisualiser les fichiers localement, lancer depuis ce dossier `python3 -m http.server 8000`, puis ouvrir `http://localhost:8000`.

## Remplacer les placeholders

Le bloc de logo « SN » dans l’en-tête et le footer est une représentation provisoire. `brand-placeholder.svg` est également un favicon temporaire et peut être remplacé par le fichier du logo officiel; dans les pages HTML, remplacer le composant `.brand-mark` ou `.logo-placeholder` par le logo définitif, avec un texte alternatif approprié si le logo est une image. Les blocs `.media-placeholder` identifient les emplacements destinés au portrait et aux visuels des projets. Pour ajouter une illustration, placer le fichier dans le dépôt (par exemple `assets/portrait.jpg`) et remplacer le bloc HTML concerné par `<img src="./assets/portrait.jpg" alt="Description utile">`. Le chemin doit rester relatif.

Les règles visuelles partagées sont dans `styles.css`. Les Google Fonts sont facultatives; les polices de repli maintiennent la lisibilité si le service de polices externe n’est pas disponible. Le site publié ne requiert ni JavaScript, ni serveur, ni base de données.
