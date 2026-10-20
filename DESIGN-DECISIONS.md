# Décisions de conception

Le prototype conserve le langage éditorial déjà validé : titres serif, sans serif fonctionnelle, palette officielle, espaces généreux et logo SN dans ses proportions. Il reste un site statique sans framework, serveur applicatif, appel de police externe ou service tiers.

Le hero conserve le globe-réseau fourni et son échelle généreuse. L’annotation « A word rarely stands alone » a été retirée de son voisinage et placée immédiatement sous le titre de la section Expertise. Elle est rose, légèrement inclinée et utilise une pile de polices manuscrites système avec repli cursif; sa taille et sa graisse sont renforcées pour rester lisibles, sans chevaucher la copie.

Le premier paragraphe d’Expertise suit maintenant exactement la formulation fournie : “The meaning of a text depends on the document, the audience, the task, the terminology already in use and the constraints of the medium. I look at those relationships as part of the work—not as details to address after the translation is complete.”

L’ancien flourish est remplacé uniquement dans cette section par le visuel de lignes colorées fourni. La source transparente de 900 × 1350 px a été redimensionnée proportionnellement en 600 × 900 px; alpha et ratio sont conservés. CSS limite sa largeur à l’espace disponible avec un maximum responsive. Aucun réemploi dans d’autres sections n’est fait dans cette itération.

Les six illustrations de mandats sources sont presque carrées (environ 504–510 × 507–509 px). Le cadre commun est donc 1:1, et non 16:9, afin de garder leur composition entière. Le balisage utilise les dimensions natives exactes. L’espace des cartes est régulier; les métadonnées réservent deux lignes et les titres deux lignes pour aligner leur départ et le texte descriptif à chaque rangée. Le ratio carré reste le même sur mobile.

L’illustration CSS abstraite de la carte technique a été retirée et remplacée par l’image carrée fournie `323144.webp`, présentée sans recadrage. Son texte alternatif décrit le tri illustré des courriels; le contenu du projet reste inchangé et clairement qualifié de projet personnel.

Le ruban Audience / Context / Terminology / Purpose et le CTA Navy avec portrait/globe restent inchangés. L’ornement de lignes est essayé dans la seule section Expertise; son éventuelle réutilisation ailleurs sera décidée après revue.
