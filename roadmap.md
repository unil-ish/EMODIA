Feuille de route du projet

1. **Préparation**

  * Élaboration des objectifs (objectifs.md).
  * Création d'une feuille de route (roadmap.md).
  * Fréquence: RDV chaque semaine en classe, le mardi matin de 09h15 à 12h00.
  * Chaque personne élabore un modèle du futur projet, à revoir en équipe.
 
3. **Exécution**
  * Distribution des rôles.
    * Classes
      * Character -> Sophie
      * Conversation -> Virgile
      * Movie -> Sophie
      * Line -> Virgile
      * Code review -> Lorelei
    * Graphes (cf.readme: UML)
    * **-> Analyses statistiques et visualisations**
      * Distribution des genres de film (6.i: _MovieGenresAnalysisGraph_)
        * type: Histogramme
      * Analyse de la cote IMDB et des votes (6.iii: _RatingsAndVotesAnalysisGraph_)
        * .color
        * type: Scatterplot
      * Analyse temporelle des films (6.ii: _TemporalAnalysisGraph_)
        * type: Histogramme
      * Analyse des personnages (6.iv: _CharacterAnalysisGraph_)
        * Position dans le générique en fonction du genre
        * type: Double histogramme
      * Exploration des dialogues (6.v)
        * Analyse de fréquence et distribution des dialogues par film (_ConversationByMovieGraph_) et personnage (_ConversationByCharacterGraph_) pour identifier les personnages clés dans la narration.
        * Exécuter une analyse de sentiment sur les répliques pour comprendre les dynamiques émotionnelles des dialogues (_LinesFlowAnalysisGraph_)
        * Pour simplifier pour commencer: histogrammes (à voir pour l'analyse de sentiments sur les répliques)
     * **-> Visualisations des données textuelles**
       * À redéfinir et distribuer quand on y arrive au vu de la taille de l'étape mais en attendant:
       * Cartographies des dialogues (6.2.i)
         * Graphes de réseau pour visualiser les interactions entre personnages dans les films, en illustrant la fréquence et la profondeur des dialogues (_InteractionsGraph_)
         * Utiliser des cartes de chaleur pour montrer la densité des échanges entre différents personnages principaux (_ConversationDensityGraph_)
       * Chronologie des Echanges Emotionnels (6.2.ii) 
         * Tracer des graphiques de série temporelle montrant l'évolution des sentiments au cours des conversations pour visualiser comment les émotions fluctuent à travers un dialogue. (_ConversationEmotionalTimelineGraph_)
       * Modélisation des Flux Emotionnels (6.2.iii)
         * Modèle Navier-Stokes (_EmotionnalFlowGraph_)  
  * Planification de qui, quoi, quand. Via plan de projet Github?
  * Writing the code 🧑‍💻
    * Finish main -> Lorelei
      * Fix read_data (d> 23.05)
      * Make sure all preset_commands work etc. (d> 26.05)
    * Update classes to work with preset_command & read_data
      * Virgile & Sophie (d> 24.05)
    * Create preset_commands for data visualisation
      * Erica, Lorelei (d> 26.05)
    * Translate comments and UI
      * Lorelei (d> 28.05)
  * Documentation
    * README in branch-erica (> 27.05)
    * Structure: Erica
    * UML (d> 24.05)
    * Each person documents the code they've written 
  * Presentation
    * PowerPoint: Erica (d> 26.05), shared on MS365
      * Each person presents their part, fills their slides

4. **Présentation**
  * Quand? `2024-05-28`
  * Qui a fait quoi?
  * Projet accompli.
  * Résultats (Graphiques, etc.).

5. **Questionaire invididuel de peer-review**
  * Chaque personne évalue le reste de l'équipe.
 
6. **Note finale collective, pondérée par la qualité de la collaboration**.
