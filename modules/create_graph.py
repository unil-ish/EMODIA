import pandas as pd #ce sera importé avant mais il ne faut pas l'oublier
import seaborn as sns
#seaborn est plus adaptée aux dataframe et est construite au-dessus de matplot. De plus, elle offre moins de possibilités de custom, ce qui simplifie le code. Si on voulait des graphiques plus complexes, il faudrait peut-être travailler avec matplot.
import matplotlib.pyplot as plt
import networkx as nx

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
        elif graph_type == 'stacked_bar_chart':
            self.create_stacked_bar_chart(data, **kwargs)
        elif graph_type == ('network_graph')
            edges = kwargs.get(edges, character_list)
            G = self.create_network_graph(edges, character_list)
            self.visualize_network_graph(G)
        else: 
            print("Ce type de graphe n'est pas pris en compte par le programme :(")
            
    #on peut ajouter d'autres types de graph si besoin: ici on choisirait d'implémenter de nouvelles méthodes mais si on voit qu'il y a 56 types de graphiques, on pourrait créer des sous-classes
            
    def create_scatterplot(self, data, x, y): 
        sns.scatterplot(x=x, y=y, data=data)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()
    
    def create_histogram(self, data, column):
        sns.histplot(data=data[column], palette='tab10')
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
        
    def create_stacked_bar_chart(self):
        sns.countplot(data=data, x=x, hue=hue, palette='tab10')
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()
        
    def create_network_graph(self, dialogue_list):
        # Initialiser un graphe vide
        G = nx.Graph()

        # Ajouter les arêtes au graphe
        G.add_edges_from(edges)

        return G
    
    def visualize_network_graph(self, G):
        # Afficher le graphe de réseau
        plt.figure(figsize=(10, 6))
        pos = nx.spring_layout(G)  # Choisir une disposition pour les nœuds
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, font_weight='bold', edge_color='gray')
        plt.title(self.title)
        plt.show()
