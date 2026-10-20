# Portfolio de Stéphanie Nadeau — prototype autonome

Prototype statique de la page d’accueil, conservé séparément du dépôt GitHub existant. Aucun changement n’a été envoyé à `LaunchedBerry07/portfolio`; ce projet n’a été ni publié ni déployé.

## Prévisualisation locale

Aucune installation ni dépendance de site n’est requise. Avec Python 3, ouvrir un terminal dans le dossier du projet et lancer :

```bash
python3 -m http.server 8000
```

Visiter ensuite `http://localhost:8000/`. Arrêter avec `Ctrl+C`.

Contrôles facultatifs des fichiers :

```bash
python3 tools/check_site.py
node --check script.js
```

## Organisation

- `index.html` : page sémantique complète, en anglais.
- `styles.css` : palette, typographie, composants et mises en page responsives.
- `script.js` : menu mobile accessible, sans dépendance.
- `assets/img/assets/` : logo, globe, flourish, visuel CTA et illustrations des mandats.
- `manus-routes.json` : manifeste de la route de page.
- `screenshots/` : captures pleine page bureau, tablette et téléphone.
- `DESIGN-DECISIONS.md` : décisions de composition.
- `ASSET-MAP.md` : correspondance des assets avec les sections.
- `TEST-REPORT.md` : vérifications faites et non vérifiées.
- `OPEN-QUESTIONS.md` : permissions, destinations et dépendances à confirmer.
- `TODO.md` : résultats livrés et validations ouvertes avant publication.

La navigation utilise des ancres vers les sections existantes. Le libellé CV est volontairement non cliquable, car aucun PDF approuvé n’était fourni dans les sources examinées. Les quatre termes Audience, Context, Terminology et Purpose conservent, à cette étape, leur composition et leurs couleurs actuelles.
