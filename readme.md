# Guide de Direction Artistique — Stéphanie Nadeau (Services Linguistiques)
**Style :** L'Éditorial Vivant & Humaniste (Le Collage Structuré)
**Objectif :** Allier l'efficacité scannable et structurée (cartes, grilles) à une touche artistique, chaleureuse et humaine (doodles, annotations, couleurs vibrantes).

---

## 1. Palette de Couleurs Officielle (Tailwind Config)
Les couleurs de la marque doivent être rigoureusement respectées sur l'ensemble des 27 pages :
- **Navy (`#13293D`)** : Couleur dominante pour les titres, le texte principal, et les fonds de sections sombres (pied de page, sections contrastées).
- **Dark Pink (`#D14D72`)** : Couleur d'accentuation principale pour les boutons d'appel à l'action (CTA), les bordures de cartes importantes et les éléments dynamiques (écho à l'étoile du logo).
- **Blue Green (`#087E8B`) & Turquoise (`#149E92`)** : Couleurs secondaires pour les icônes, les sous-titres, les étiquettes et les éléments de navigation.
- **Seafoam (`#83E0D0`)** : Utilisé pour les ombres portées, les arrière-plans de mise en avant (ex: projets techniques) et les accents doux.
- **Mist (`#EAF4F8`)** : Couleur de fond de page principale (`#FAFCFD` ou `#EAF4F8`) pour offrir un espace visuel aéré et lumineux.
- **Sky (`#5B96BD`)** : Utilisé pour les métadonnées, les sous-titres de cartes et les séparateurs.

---

## 2. Typographie & Hiérarchie
- **Titres (H1, H2, H3) :** Police `Playfair Display` (Serif), élégante, éditoriale et haut de gamme.
- **Corps de texte :** Police `Inter` (Sans-serif), ultra-lisible, moderne et épurée.
- **Annotations & Gribouillis (Doodles) :** Police `Caveat` (Cursive/Handwriting) pour les petits mots en marge, flèches, étiquettes et touches créatives informelles.

---

## 3. Composants UI & Règles d'Intégration
- **Les Cartes (« Cards ») :** 
  - Utiliser la classe `.organic-border` ou `.organic-border-pink` pour donner un aspect légèrement organique/dessiné aux bordures de cartes.
  - Toujours associer une ombre portée décalée typique (ex: `shadow-[4px_4px_0px_0px_#13293D]`).
- **Le Style « Collage » :**
  - Intégrer des bulles de dialogue flottantes (`bubble-1`, `bubble-2`, etc.) sur les sections d'introduction ou les portraits.
  - Utiliser des soulignements décoratifs SVG (`.scribble-underline`) sur les mots clés importants des titres principaux.
- **Les Icônes :** Utiliser FontAwesome (`fa-solid`) logées dans des pastilles circulaires aux couleurs de la palette (fond Mist, icône Blue Green ou Dark Pink).

---

## 4. Instructions pour les 27 pages subséquentes
Lorsque tu entameras une nouvelle conversation pour créer une page (ex: *Portfolio, Services, À propos, Contact, Études de cas*), procède ainsi :
1. **Partage ce fichier** (`design_system_guidelines.md`) ou rappelle simplement : *« Applique le guide de direction artistique "L'Éditorial Vivant & Humaniste" de Stéphanie Nadeau »*.
2. **Indique le contenu textuel et l'objectif spécifique** de la page en question.
3. Je générerai directement le fichier HTML unique complet, prêt à être testé et validé !