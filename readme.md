# EMODIA: ÉMotions et DIalogues Analyse
## Analyse émotionnelle des dialogues dans les films en utilisant le modèle inspiré des équations de Navier-Stokes

### Objectif du projet
L'objectif principal de ce projet est d'explorer et de quantifier la manière dont les émotions se développent et interagissent dans les dialogues des films, en utilisant une approche innovante inspirée des équations de Navier-Stokes. Le modèle vise à offrir une nouvelle lentille à travers laquelle examiner les dynamiques émotionnelles entre les personnages, permettant une compréhension plus profonde des stratégies narratives et des relations interpersonnelles au sein des films.

### Fonctionnalités
1. Importer et nettoyer les données
2. Générer divers types de représentations graphiques relatives aux données
3. Générer des représentations des flux émotionnels dans les dialogues
4. Personnaliser birèvement les visualisations ???

### Contexte
Ce projet s'inscrit dans le cours de programmation orientée objet en Informatique pour les sciences humaines à l’Université de Lausanne, au printemps 2024

### Précision
Le français a été selectionné pour la documentation du projet par simplicité.

### Description du dataset
Dans tous les fichiers, le séparateur de champs original était " +++$+++ " et a été converti en tabulations (\t). De plus, l'encodage original du fichier était ISO-8859-2. Il est possible que la conversion et le décodage du séparateur de champs aient laissé quelques artefacts.

* _movie_titles_metadata.txt_

   contient des informations sur chaque titre de film
   champs :
  
      * movieID,
      * titre du film,
      * année du film,
      * cote IMDB,
      * non. votes IMDB,
      * genres au format ['genre1', 'genre2',É, 'genreN']
  
* _movie_characters_metadata.txt_

   contient des informations sur chaque personnage de film
   champs :
  
      * characterID
      * nom du personnage
      * movieID
      * titre du film
      * sexe (" ?" pour les cas non étiquetés)
      * position dans le générique (" ?" pour les cas non étiquetés)
  
* _movie_lines_.txt

   contient le texte réel de chaque énoncé
   champs :
  
      * lineID
      * characterID (qui a prononcé cette phrase)
      * identifiant du film
      * nom du personnage
      * texte de la phrase

* _movie_conversations_.txt

   la structure des conversations
   champs
  
      * characterID du premier personnage impliqué dans la conversation
       * characterID du deuxième personnage impliqué dans la conversation
      * movieID du film dans lequel la conversation a eu lieu
      * liste des énoncés qui composent la conversation, dans l'ordre chronologique
      * chronologique : ['lineID1', 'lineID2',É, 'lineIDN'] doit être mis en correspondance avec movie_lines.txt pour reconstituer le contenu réel

* _raw_script_urls.txt_
  
   les URL à partir desquelles les sources brutes ont été récupérées

### Installation et utilisation du programme
1. 
2. 
3. 
...

### Structure logique du projet --> je sais pas à quel point il faut être précis la dessus :O 
📁 core_modules

📁 data

📁 model

📁 modules 

📁 ressources

📄 .gitignore

📄 README.md

📄 Emodia.py

📄 Objectifs.md

📄 Roadmap.md

### Contributeur-ices 
- Virgile Albasini, Université de Lausanne, virgile.albasini@unil.ch
- Erica Berazategui, Université de Lausanne, erica.berazategui@unil.ch
- Lorelei Chevroulet, Université de Lausanne, lorelei.chevroulet@unil.ch
- Sophie Ward, Université de Lausanne, sophie.ward@unil.ch
- Davide Picca, Université de Lausanne, davide.picca@unil.ch
- Johan Cuda, Université de Lausanne, johan.cuda@unil.ch
