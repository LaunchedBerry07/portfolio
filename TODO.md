# État des livrables

_Mise à jour du 2 novembre 2026 après les corrections P1/P2 appliquées à la copie auditée._

## Travaux de la livraison initiale

- [x] Séparer le CSS du HTML pour les pages alors présentes et organiser les styles réutilisables.
- [x] Réorganiser les pages, styles et ressources dans une arborescence logique.
- [x] Adapter et vérifier les chemins, liens et fichiers pour GitHub Pages.
- [x] Appliquer une barre de navigation et un pied de page uniformes.
- [x] Ajouter après le hero de Services un menu d’accès rapide vers les services.
- [x] Créer un emplacement dédié aux actifs visuels à ajouter ultérieurement.
- [x] Créer et vérifier les renvois internes, liens entre pages et états de navigation.
- [x] Conserver les contenus existants et respecter l’identité visuelle du portfolio et du guide artistique.
- [x] Ajouter la page Clients & Sectors, ses visuels optimisés pour le rôle et son CSS dédié.
- [x] Ajouter le lien Clients & Sectors à la navigation et au pied de page.

Bilan historique de la livraison : 25 blocs de pied de page hérités ont été supprimés; le CSS commun a été dédupliqué (46 blocs répétés ou redondants retirés) et le commentaire mal formé supprimé. Les liens de contact conservés ont été redirigés vers la page Contact.

## État courant de la copie auditée

L’archive comprend **28 fichiers HTML** (27 pages du site et `404.html`), 12 études de cas et 8 projets techniques. Le menu d’accès rapide de Services contient **cinq raccourcis**. Le `baseurl` courant est `/portfolio`. Les 15 fichiers SVG de `assets/images/` sont des emplacements explicitement temporaires à remplacer par les visuels approuvés.

## Vérifications postérieures

- [x] Balayer les 28 pages à six largeurs de viewport et corriger les débordements P1 relevés.
- [x] Vérifier au clavier le lien d’évitement, le menu compact, les CTA et les filtres dans les scénarios ciblés.
- [x] Exécuter l’audit Axe de contraste sur les pages rendues à 390, 768 et 1 440 px : aucune violation signalée sur 84 rendus.
- [x] Contrôler 13 états interactifs (survol, filtre actif, menu ouvert et focus) sans violation de contraste.

## À faire avant une validation finale de publication

- [ ] Examiner manuellement les cas Axe « incomplets » : 258 occurrences de vérification non concluante à cause notamment des gradients, images, pseudo-éléments et chevauchements. Ce ne sont pas des violations automatiques confirmées.
- [ ] Effectuer un essai avec un lecteur d’écran réel; aucune lecture vocale avec un lecteur d’écran n’a été réalisée.
- [ ] Remplacer les 15 emplacements SVG temporaires par les visuels définitifs et approuvés, si ceux-ci doivent être présents avant publication.
- [ ] Confirmer la provenance, les autorisations et l’approbation des contenus et identités de clients.
- [ ] Décider si Google Fonts et Font Awesome doivent rester servis depuis des CDN publics ou être hébergés localement.
