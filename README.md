# EMODIA: ÉMotions et DIalogues Analyse
## Analyse émotionnelle des dialogues dans les films en utilisant le modèle inspiré des équations de Navier-Stokes

#### Objectif du projet
L'objectif principal de ce projet est d'explorer et de quantifier la manière dont les émotions se développent et interagissent dans les dialogues des films, en utilisant une approche innovante inspirée des équations de Navier-Stokes. Le modèle vise à offrir une nouvelle lentille à travers laquelle examiner les dynamiques émotionnelles entre les personnages, permettant une compréhension plus profonde des stratégies narratives et des relations interpersonnelles au sein des films.

#### Implications et applications potentielles
Le projet non seulement enrichira la compréhension des techniques narratives et de la construction des personnages dans les films mais pourra également avoir des applications pratiques dans le domaine de la production cinématographique, dans la critique de films, et dans l'industrie du divertissement en général. Il pourrait offrir aux réalisateurs et scénaristes de nouveaux outils pour évaluer et perfectionner l'efficacité émotionnelle de leurs œuvres, ainsi que fournir aux analystes et critiques une nouvelle méthode pour discuter et évaluer les œuvres cinématographiques.

#### Phases du projet

1. **Sélection des films et collecte des dialogues** :
   - Pour la sélection des données et la préparation du projet EMODIA ("ÉMotions et DIalogues Analyse"), nous utiliserons le ["Cornell Movie-Dialog Corpus"](./movie_dialog.zip). Ce corpus         comprend un ensemble diversifié de dialogues extraits de scénarios de films, couvrant un large éventail de genres et offrant une riche variété de dynamiques émotionnelles. Cette              ressource nous permettra d'accéder directement à des transcriptions de dialogues de qualité, facilitant l'analyse des interactions et des évolutions émotionnelles entre les personnages        sans nécessiter une collecte de données supplémentaire.


2. **Extraction et Préparation des Dialogues**

   - **Extraction des Échanges Conversationnels** : À partir du "Cornell Movie-Dialog Corpus", nous procéderons à l'extraction de 220,579 échanges conversationnels entre 10,292 paires de personnages de films. Cette riche collection de dialogues, tirée de 617 films, fournira la base de données pour notre analyse émotionnelle approfondie.

   - **Nettoyage et Standardisation** : Les données seront nettoyées pour éliminer d'éventuels artéfacts dus à la conversion du séparateur de champs original " +++$+++ " en tabulations (\t), ainsi qu'à la décodification de l'encodage original ISO-8859-2. Ce processus garantira que notre focus soit strictement sur le texte verbal des échanges, en excluant toute annotation non verbale ou instruction scénique superflue.

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

   - **Création de Cartes de Chaleur** : Les cartes de chaleur seront conçues pour démontrer la distribution et l'intensité des émotions à travers différents segments de dialogue au sein d'un film. En utilisant une gamme de couleurs, ces cartes révèleront les zones où les émotions comme la joie, la tristesse, la colère, et la surprise sont particulièrement concentrées, fournissant ainsi une vue d'ensemble de la dynamique émotionnelle du récit. Les variations de couleur au sein de la carte indiqueront l'évolution des émotions du début à la fin, offrant des insights sur la manière dont les événements clés ou les interactions entre personnages affectent le paysage émotionnel du film.

   - **Graphiques de Flux** : Les graphiques de flux illustreront le mouvement et la transition des émotions entre les personnages au fil des conversations. En visualisant ces flux, nous pourrons identifier des patterns tels que l'échange d'émotions spécifiques entre les protagonistes, les moments où les émotions s'intensifient ou se dissipent, et la manière dont ces dynamiques contribuent à l'avancement de l'histoire. Ces graphiques permettront de suivre le parcours émotionnel des personnages, mettant en évidence les interactions qui jouent un rôle pivot dans le développement de leur relation et dans la progression du récit.

   - **Présentation Intuitive des Résultats** : L'utilisation de ces visualisations nous permettra de présenter nos résultats de manière intuitive et engageante. En illustrant visuellement les découvertes clés du projet, nous faciliterons la compréhension des dynamiques émotionnelles complexes qui sous-tendent les dialogues des films. Cette approche visuelle permettra aux chercheurs, aux cinéastes et au public de saisir rapidement les aspects essentiels de notre analyse, renforçant ainsi l'accessibilité et l'impact de notre recherche.


7. **Analyse et interprétation (TENTATIVE)** :
   - Évaluer les modèles émergents de l'analyse, tels que la présence de points de tournant émotionnels, la distribution des émotions entre les personnages principaux et secondaires, et les variations d'intensité émotionnelle par rapport aux événements clés de l'intrigue.
   - Interpréter les résultats à la lumière des théories de la narratologie et de la psychologie des émotions, cherchant à relier les dynamiques émotionnelles identifiées avec l'impact sur le public et avec les techniques narratives utilisées.

