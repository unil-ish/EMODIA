# EMODIA: ÉMotions et DIalogues Analyse
## Analyse émotionnelle des dialogues dans les films en utilisant le modèle inspiré des équations de Navier-Stokes

#### Objectif du projet
L'objectif principal de ce projet est d'explorer et de quantifier la manière dont les émotions se développent et interagissent dans les dialogues des films, en utilisant une approche innovante inspirée des équations de Navier-Stokes. Le modèle vise à offrir une nouvelle lentille à travers laquelle examiner les dynamiques émotionnelles entre les personnages, permettant une compréhension plus profonde des stratégies narratives et des relations interpersonnelles au sein des films.

#### Implications et applications potentielles
Le projet non seulement enrichira la compréhension des techniques narratives et de la construction des personnages dans les films mais pourra également avoir des applications pratiques dans le domaine de la production cinématographique, dans la critique de films, et dans l'industrie du divertissement en général. Il pourrait offrir aux réalisateurs et scénaristes de nouveaux outils pour évaluer et perfectionner l'efficacité émotionnelle de leurs œuvres, ainsi que fournir aux analystes et critiques une nouvelle méthode pour discuter et évaluer les œuvres cinématographiques.

### Description du dataset

**Contenu**
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

#### Phases du projet

**Le projet doit être entièrement construit selon une architecture de programmation orientée objet.**

1. **Sélection des films et collecte des dialogues** :
   - Pour la sélection des données et la préparation du projet EMODIA ("ÉMotions et DIalogues Analyse"), nous utiliserons le ["Cornell Movie-Dialog Corpus"](./movie_dialog.zip). Ce corpus         comprend un ensemble diversifié de dialogues extraits de scénarios de films, couvrant un large éventail de genres et offrant une riche variété de dynamiques émotionnelles. Cette              ressource nous permettra d'accéder directement à des transcriptions de dialogues de qualité, facilitant l'analyse des interactions et des évolutions émotionnelles entre les personnages        sans nécessiter une collecte de données supplémentaire.


2. **Extraction et Préparation des Dialogues**

   - **Extraction des Échanges Conversationnels** : À partir du "Cornell Movie-Dialog Corpus", nous procéderons à l'extraction de 220,579 échanges conversationnels entre 10,292 paires de personnages de films. Cette riche collection de dialogues, tirée de 617 films, fournira la base de données pour notre analyse émotionnelle approfondie.

3. **Segmentation et Association des Dialogues**

   - **Délimitation des Unités de Dialogue** : Utilisant le fichier `movie_lines.txt`, chaque réplique sera traitée comme une unité de dialogue individuelle, portant une attention particulière à la correspondance entre les identifiants des lignes de dialogue et les métadonnées des personnages pour préserver l'association précise avec les personnages qui les prononcent.

   - **Reconstruction des Conversations** : En s'appuyant sur le fichier `movie_conversations.txt`, nous reconstruirons les conversations intégrales en ordre chronologique en associant les identifiants des répliques aux lignes de dialogue correspondantes. Cette étape est essentielle pour analyser les flux et les dynamiques émotionnels à travers les interactions narratives authentiques entre les personnages.

4. **Enrichissement des Données avec Métadonnées**

   - **Intégration des Métadonnées des Films et des Personnages** : Les fichiers `movie_titles_metadata.txt` et `movie_characters_metadata.txt` seront utilisés pour enrichir notre analyse avec des informations contextuelles telles que le genre des films, l'année de sortie, la note IMDB, ainsi que le genre et la position dans les crédits des personnages. Cette dimension ajoutée permettra d'explorer comment les caractéristiques des films et les attributs des personnages influencent les dynamiques émotionnelles des dialogues.

   - **Analyse selon les Genres et les Caractéristiques des Personnages** : L'incorporation de ces métadonnées offrira l'opportunité d'examiner les variations des flux émotionnels en fonction du genre cinématographique et des rôles des personnages au sein du récit, fournissant ainsi une compréhension plus nuancée des stratégies narratives employées.

5. **Application du modèle de Navier-Stokes** :
   - Utiliser les équations de Navier-Stokes pour modéliser les dynamiques émotionnelles des dialogues à l'aide de ce [fichier](./analysis_navier_stocker.py), traitant les émotions comme des "flux" qui peuvent varier en intensité et direction au fil du temps et entre les personnages.
   - Analyser les séquences de dialogue pour identifier comment les émotions "coulent" entre les personnages et comment ce flux évolue au cours de la narration.
   - Pour se faire une idée de l'approche vous pouvez faire référence à cet [article](./MathNLP24__Fluid_Dynamics_Inspired_Emotional_Analysis_in_Shakespearean_Tragedies__A_Novel_Computational_Linguistics_Methodology%20(5).pdf)
     
     **ATTENTION: Notes de mise en œuvre**
     - SentimentDynamics : Encapsule les fonctions liées au calcul du flux de sentiments à l'aide de l'équation de Navier-Stokes. Accepte une liste de mots-clés (positifs et négatifs) pour
       calculer la pression du sentiment.
     - SpeechAnalysis : gère l'analyse de la parole à l'aide des méthodes définies dans SentimentDynamics. Prend en entrée le DataFrame des discours et une instance de SentimentDynamics pour 
       effectuer les calculs. **Regarder dans le fichier un exemple d'utilisation**

6. **Visualisation des Résultats**

   La phase de visualisation des résultats du projet EMODIA impliquera l'utilisation de bibliothèques Python spécialisées comme [SeaBorn](https://seaborn.pydata.org/)

    Basé sur le descriptif du dataset et le plan du projet, voici une série d'analyses et de visualisations potentielles que vous pouvez envisager pour explorer et comprendre les dynamiques    narratives et émotionnelles des dialogues de films :

   ### Analyses Statistiques et Visualisations

      1. **Distribution des Genres de Films**
         - Créer un histogramme ou un diagramme circulaire pour visualiser la distribution des genres de films dans le dataset.
         - Examiner les genres de films les plus communs et ceux moins représentés pour déterminer des tendances ou des biais potentiels dans la sélection des films.
      
      2. **Analyse Temporelle des Films**
         - Tracer la distribution des films par année de sortie pour observer les tendances cinématographiques au fil du temps.
         - Corréler l’évolution des genres avec les périodes historiques pour voir si certaines époques favorisent certains types de films.
      
      3. **Analyse de la Cote IMDB et des Votes**
         - Utiliser un scatter plot pour explorer la relation entre la cote IMDB des films et le nombre de votes reçus, potentiellement en colorant les points par genre de film pour détecter des patterns spécifiques.
      
      4. **Analyse des Personnages**
         - Répartition des personnages par sexe et par position dans le générique pour identifier les dynamiques de représentation de genre dans les films.
         - Étudier la corrélation entre le sexe des personnages et leur importance dans le film (position dans le générique).
      
      5. **Exploration des Dialogues**
         - Analyser la fréquence et la distribution des dialogues par film et par personnage pour identifier les personnages clés et leur centralité dans la narration.
         - Exécuter une analyse de sentiment sur les répliques pour comprendre les dynamiques émotionnelles des dialogues.
      
   ### Visualisations des Données Textuelles
   
      1. **Cartographie des Dialogues**
         - Créer des graphes de réseau pour visualiser les interactions entre personnages dans les films, en illustrant la fréquence et la profondeur des dialogues.
         - Utiliser des cartes de chaleur pour montrer la densité des échanges entre différents personnages principaux.
      
      2. **Chronologie des Échanges Emotionnels**
         - Tracer des graphiques de série temporelle montrant l'évolution des sentiments au cours des conversations pour visualiser comment les émotions fluctuent à travers un dialogue.
      
      3. **Modélisation des Flux Emotionnels**
         - Utiliser des modèles basés sur les équations de Navier-Stokes pour simuler les flux émotionnels entre les personnages, en représentant graphiquement la dynamique et l'intensité                de ces échanges.
         - Explorer les différences de flux émotionnel en fonction des caractéristiques du film ou des attributs des personnages.
      

   Ces analyses et visualisations pourraient offrir des insights précieux sur la structure narrative et les dynamiques émotionnelles des dialogues cinématographiques, enrichissant ainsi les recherches dans le domaine des humanités numériques et de l'analyse du texte.

7. **Analyse et interprétation (TENTATIVE)** :
      - Évaluer les modèles émergents de l'analyse, tels que la présence de points de tournant émotionnels, la distribution des émotions entre les personnages principaux et secondaires, et les variations d'intensité émotionnelle par rapport aux événements clés de l'intrigue.
      - Interpréter les résultats à la lumière des théories de la narratologie et de la psychologie des émotions, cherchant à relier les dynamiques émotionnelles identifiées avec l'impact sur le public et avec les techniques narratives utilisées.

