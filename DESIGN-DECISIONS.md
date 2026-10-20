# Décisions de conception

Le prototype conserve le langage visuel éditorial des références : titres serif, texte fonctionnel sans serif, palette officielle, surfaces claires alternées, petites annotations contrôlées et logo SN préservé. Aucun framework, service ou appel de police externe n’est requis; Georgia et les polices système assurent le repli typographique local.

Le hero utilise l’illustration globe-réseau en Mist et l’agrandit par rapport au texte, avec un débordement contrôlé. Sur tablette et téléphone, l’image se replace sous le texte et conserve une échelle généreuse.

Dans la section Expertise, le flourish quitte le dessous du titre et occupe une colonne dédiée entre titre et copie. Sur mobile, il se place à côté du titre avant que la copie ne prenne toute la largeur. Cela enlève sa hauteur artificielle du dessous de la section sans obstruer la lecture.

Le ruban Audience / Context / Terminology / Purpose est conservé visuellement et sémantiquement tel qu’il est pour cette itération. Seul son retour à la ligne est autorisé sur un petit écran afin d’éviter le débordement horizontal.

La composition CTA réutilise l’asset portrait/globe transparent sur Navy, sans encadrement. Un masque CSS progressif fond son bord gauche dans le fond de section; le contenu textuel reste en HTML au premier plan. Sur téléphone, l’illustration est déplacée sous la copie et demeure intégrée au fond.

La grille de services comporte six éléments; Data Annotation utilise le libellé et la description approuvés exactement. Les mandats clients et le projet Gmail sont présentés dans des sections différentes. L’illustration technique est abstraite et CSS pour ne pas suggérer une capture ou un livrable réel.
