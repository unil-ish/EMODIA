import pandas as pd #ce sera importé avant mais il ne faut pas l'oublier
import seaborn as sns
#seaborn est plus adaptée aux dataframe et est construite au-dessus de matplot. De plus, elle offre moins de possibilités de custom, ce qui simplifie le code. Si on voulait des graphiques plus complexes, il faudrait peut-être travailler avec matplot.
import matplotlib.pyplot as plt

#Déclaration de la classe CreateGraph qui va créer les graphiques demandés
class CreateGraph: 
    
    #constructeur de la classe BaseGraph, avec les paramètres qui seront utilisés pour initialiser les attributs de la classe
    def __init__(self, title, xlabel, ylabel):
        self.title = "Graph title goes here"
        self.xlabel = "x-axis label goes here"
        self.ylabel = "y-axis label goes here"
    
    def create_graph(self, data, graph_type, **kwargs):
        if graph_type == 'scatter':
            self.create_scatterplot(data, **kwargs)
        elif graph_type == 'histogram':
            self.create_histogram(data, **kwargs)
        elif graph_type == 'heatmap':
            self.create_heatmap(data, **kwargs)
            
    #on peut ajouter d'autres types de graph si besoin: ici on choisirait d'implémenter de nouvelles méthodes mais si on voit qu'il y a 56 types de graphiques, on pourrait créer des sous-classes
            
    def create_scatterplot(self, data, x, y): 
        sns.scatterplot(x=x, y=y, data=data)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()
    
    def create_histogram(self, data, column):
        sns.histplot(data=data[column])
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()
        
    def create_heatmap(self):
        pivot_table = data.pivot_table(values = values, index = y, columns = x)
        sns.heatmap(data=pivot_table, cmap="coolwarm")
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()
        
# tentatives de création de graphiques 

#analyse de l'année de sortie

df_release_year = pd.DataFrame('Release_year': list_all_release_years_id, columns=['Release_year'])

graph = CreateGraph(title='Analyse temporelle des films', xlabel='Année de sortie', ylabel='Nb de films')
graph.create_graph(data=df_release_year, graph_type='histogram', column='Release_year')
#si ça fonctionne pas on peut essayer de définir data avant 

#analyse des genres 

df_genres = pd.DataFrame('Genres': list_all_genres_id, columns=['Genres'])

graph = CreateGraph(title='Analyse des genres de films', xlabel='Genres', ylabel='Nb de films')
graph.create_graph(data=df_genres, graph_type='histogram', column='Genres')



#rating et votes

df_rating = pd.DataFrame('Rating': list_all_ratings_id, 'Votes': list_all_votes_id, 'Genres': list_all_genres_id, columns=['Rating', 'Votes', 'Genres'])

graph = CreateGraph(title='Analyse des votes et de la cote', xlabel='Cote IMBD', ylabel='Nb de votes')
graph.create_graph(data=df_rating, graph_type='scatterplot', x='Rating', y='Votes', hue='Genres')


#personnages

df_characters = pd.DataFrame('Gender': list_all_genders, 'Credit_position': list_all_credits_positions, columns=['Gender', 'Credit_position'])

graph = CreateGraph(title='Analyse croisée des personnages en fonction du genre et de la position dans les crédits', xlabel='Position', ylabel='Nombre de personnages')
graph.create_graph(data=df_characters, graph_type='create_stacked_bar_chart', x='Credit_position', hue='Gender')


#dialogues par personnages et films krkrkrkrkrkr je comprend pas à quoi doit ressembler ce graphique, est-ce qu'il faudrait compter le nombre de dialogue par personnags?

df_dialogues = pd.DataFrame('Movies' = all_movies_id, 'Characters' = list_characters #dans la classe conversation)
graph = CreateGraph(title='Fréquence des dialogues par personnages', xlabel='Personnage', ylablel='Nombre de personnage')
graph.create_graph(data=df_dialogues, graph_type='stacked_bar_chart', x='Characters', hue='Movies')


#Exécuter une analyse de sentiment sur les répliques pour comprendre les dynamiques émotionnelles des dialogues.
??

#Créer des graphes de réseau pour visualiser les interactions entre personnages dans les films, en illustrant la fréquence et la profondeur des dialogues.

graph = CreateGraph(title='Graphe de Réseau des Interactions entre Personnages')
edges = 
character_list = 
graph.create_graph(data=None, graph_type='network_graph', edges=edges, character_list=character_list)


#Utiliser des cartes de chaleur pour montrer la densité des échanges entre différents personnages principaux
get_all_characters()
get_all_characters()

df_density_exchanges = pd.DataFrame('X' = list_characters, 'Y' = list_characters

graph = CreateGraph(title='Carte de chaleur des échanges entre personnages principaux')
graph.create_graph(data=df_density_exchanges, graph_type='heatmap', x='X', y='Y')


#Tracer des graphiques de série temporelle montrant l'évolution des sentiments au cours des conversations pour visualiser comment les émotions fluctuent à travers un dialogue.
??

#Modélisation des Flux Emotionnels: Modèle Navier-Stokes

