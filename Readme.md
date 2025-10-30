
# Univers WizeCosm
![[Pasted image 20251029202225.png]]


## Présentation générale

WizeCosm est un univers fictionnel riche et complexe, où cohabitent magie, divinités, et civilisations en lutte. Ce monde se distingue par la présence unique de l'énergie Cosm, source de vie et de pouvoir, mais aussi de mutations profondes chez les êtres vivants. L’univers mêle mythologie, intrigues politiques et conflits mystiques sur un fond de géographie variée et de cultures distinctes.

## L'Énergie Cosm

L’énergie Cosm est une force magique primordiale synthétisée naturellement par certaines aptitudes physiques hors norme chez les Yamé, et par une manipulation magique chez les Gamé. Cette énergie bouleverse profondément l’équilibre de la planète WizeCosm, provoquant notamment des altérations physiques et psychiques chez les créatures vivant dans certaines zones frontalières, dites « zones de front ». Ces régions sont le théâtre d’affrontements entre les Cosmers, des guerriers d’élite contrôlant le Cosm, et les créatures altérées par cette force.

## Panthéon et Mythologie

Les Dieux sont les entités suprêmes de WizeCosm, créateurs des créatures célestes et des astres qui peuplent cet univers. Leur volonté façonne les mondes, parfois en conflit, ce qui engendre chaos et renouveau. Ces conflits divins ont des répercussions directes sur les mortels et sur l’équilibre cosmique. Parmi ces créatures célestes, certains astres sont considérés comme des embryons d’âme-monde, porteurs d’une mystique profonde.

## Cultes et religions

Parmi les croyances dominantes, le Culte de la Lumière tient une place centrale. Originellement né d’une époque où les êtres vivants habitaient dans l’obscurité des souterrains, ce culte célèbre la lumière comme source de vie et de révélation. Les fidèles vénèrent la lumière solaire comme un pouvoir sacré capable de guider et de protéger. La religion se manifeste par des croyances, rites et sociétés secrètes, qui influencent fortement la dynamique sociale et politique des peuples.

## Zones de front

Les zones de front sont des territoires où les effets du Cosm sont les plus puissants et où surviennent les plus violents affrontements. Ces zones sont variées : glaciers irradiés, embouchures agitées, déserts ensablés, marécages lumineux ou ruines antiques. Chaque zone possède une atmosphère unique et abrite des créatures altérées aux capacités redoutables, auxquelles les Cosmers sont envoyés pour contenir la menace.

## Géographie et nations

Le monde de WizeCosm comprend plusieurs continents et régions majeures, tels que l’Amarthie, la Kramargue et la Kritia. Ces territoires possèdent leurs propres cultures, races dominantes, et systèmes politiques. Certains centres urbains, comme la cité-état de Glothäm, jouent un rôle commercial et stratégique crucial. La géographie est marquée par des mers intérieures, des montagnes riches en ressources et des terres façonnées par les conflits divins ou cosmiques.

## Objectifs du projet

Ce projet vise à documenter avec précision tous les aspects narratifs de l’univers WizeCosm, afin de structurer la trame, les personnages, lieux et conflits. Il servira aussi de base pour d’éventuelles créations multimédias (écrits, jeux, visuels). Une attention particulière est portée à la cohérence mythologique et à l’équilibre entre magie, politique et évolution des mondes.

---

# Détails Techniques du Projet WizeCosm

## Notes et définitions - Obsidian

Pour centraliser et organiser toutes les notes, définitions et recherches liées à l’univers WizeCosm, Obsidian est utilisé.  
- Obsidian permet de stocker les notes au format Markdown localement avec un lien facile entre elles.  
- Les définitions sont structurées dans des dossiers dédiés (ex : dossier "Definitions") qui peuvent être référencés dans tout le vault.  
- L’interface permet de survoler les termes pour afficher leur définition en prévisualisation, favorisant une navigation fluide entre concepts.  
- Des plugins Obsidian permettent de faire des listes de définitions détaillées, de baliser les notes avec des tags et de créer des tableaux de contenus dynamiques pour les projets.  
- Cette méthode garantit un référentiel viviant et facilement évolutif des connaissances et règles narratives [web:20][web:21][web:24].

## Géographie - QGIS + PostGIS

La cartographie et la gestion des données géographiques de WizeCosm sont opérées via l’intégration de QGIS avec une base spatiale PostGIS.  
- PostGIS est une extension PostgreSQL qui apporte la prise en charge complète des données géospatiales complexes.  
- QGIS, outil SIG open source, se connecte nativement à PostGIS pour visualiser, interroger et manipuler ces données spatiales.  
- La gestion via PostGIS assure une base de données centralisée, multi-utilisateurs, robuste et extensible, idéale pour gérer les cartes, zones de front, zones altérées, etc.  
- QGIS est utilisé pour importer/exporter des données géographiques, réaliser des analyses spatiales tout en exploitant la puissance des fonctions PostGIS (ex : requêtes spatiales, intersections, buffers).  
- Cette architecture assure une cohérence parfaite entre données narrative et géographique dans le projet [web:25][web:29][web:33].

## Timeline - Aeon Timeline

La gestion des timelines du projet, notamment des événements imbriqués, relations entre événements et entités (personnages, lieux, objets), est assurée par Aeon Timeline :  
- Aeon Timeline offre une interface chronologique visuelle puissante, avec prise en charge d’événements multiples, sous-événements et relations croisées.  
- Chaque événement peut contenir de nombreuses métadonnées : dates de début/fin, tags, notes, catégories, permettant une organisation fine des récits temporels.  
- L’outil permet aussi la gestion d’entités (personnes, lieux, objets) et la visualisation de leurs cycles de vie à travers le temps.  
- Aeon Timeline propose plusieurs styles de calendriers (dates absolues, flottantes, relatives) adaptées aux besoins narratifs du projet.  
- L’outil favorise la cohérence temporelle des histoires complexes, garantissant la continuité et la clarté des arcs narratifs dans WizeCosm [web:26][web:30][web:34].

## Intégration des notes avec Postgres via Dagster ETL

Pour connecter le référentiel de notes (comme Obsidian) et gérer les flux de données (notes, annotations, logs d’événements) dans une base PostgreSQL, un pipeline ETL orchestré par Dagster est utilisé :  
- Dagster est un orchestrateur open source pour construire et gérer des pipelines de données robustes, facilitant Extract-Transform-Load.  
- Le module dagster-postgres permet de stocker les logs d’exécution, métadonnées et résultats de pipelines dans PostgreSQL, assurant traçabilité et persistance.  
- Cette configuration facilite la synchronisation des notes structurées, leur transformation en formats exploitables pour analyses ou visualisation, et leur chargement dans la base centralisée.  
- Dagster permet également de gérer la programmation des tâches, leur monitoring, et l’intégration dans un workflow global de gestion de données narratives et géographiques.  
- Cette architecture modernise la gestion des informations liées à WizeCosm, proposant un couplage efficace entre prise de notes incrémentale et base relationnelle performante [web:27][web:31][web:35].

---

Ce README technique peut être complété ou modifié selon l’évolution des outils adoptés et les besoins du projet WizeCosm.
