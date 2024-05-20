# Objectifs
## Fournir une visualisation des points suivants :
- la distribution des genres de film
- distribution des films par date de sorties
- popularité IMDB en fonction du nombre de vote proportionnellement 
- distribution des personnages par sexe et position dans le générique 
- fréquence de la distribution des dialogues par film et par personnage 
- créer graphe de réseau pour les dialogues entre personnages 
- cartes de chaleur pour la densité des échanges
- graphiques de séries temporelles pour montrer l'évolution des sentiments
- simuler les flux émotionnels entre les personnages, en représentant la dynamique et l'intensité des échanges
-

## Classes candidates: 
- films: id, date de sortie, cote IMDB, nombres de vote IMDB, genre
- personnages: id, idfilm, nom, sexe, position dans le générique 
- émotions: id,  
- répliques: id, idpersonnage, idfilm, (nom du personnage), contenu de la réplique
- dialogue: id, idpersonnage1, idpersonnage2, idfilm, *répliques

