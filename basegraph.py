from abc import ABC, abstractmethod
#importe la classe 'ABC' et le décorateur abstractmethod du module abc, qui sont utilisés pour définir une classe abstraite et des méthodes abstraites respectivement.
import pandas as pd #ce sera importé avant mais il ne faut pas l'oublier
import seaborn as sns
#seaborn est plus adaptée aux dataframe et est construite au-dessus de matplot. De plus, elle offre moins de possibilités de custom, ce qui simplifie le code. Si on voulait des graphiques plus complexes, il faudrait peut-être travailler avec matplot.
import matplotlib.pyplot as plt

#Déclaration de la classe abstraite BaseGraph qui hérite de la classe ABC.
class BaseGraph(ABC): 
    
    #constructeur de la classe BaseGraph, avec les paramètres qui seront utilisés pour initialiser les attributs de la classe
    def __init__(self, title, xlabel, ylabel):
        self.title = "Graph title goes here"
        self.xlabel = "x-axis label goes here"
        self.ylabel = "y-axis label goes here"
 
         
    #def xy_values(self, data):
        #pass
    
    #@abstractmethod 
    #def type(self, data):
        #pass
    
    #@abstractmethod
    #def show(self, data):
        #pass
    
    @abstractmethod
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
    
    def create_histogram(self):
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
        
# exemples d'utilisations à implémenter dans la fonction main: 

# Création d'une instance de la classe abstraite avec un titre approprié
#graph = BaseGraph(title='Title', xlabel='X', ylabel='Y')

#charger les données des DataFrame créé dans les autres classes: 
#exemple_pd = pd.read_csv('exemple.pd')

# Création d'un scatterplot en utilisant la méthode create_graph: il faut modifier le nom du df
#graph.create_graph(data=exemple_pd, graph_type='scatter', x='ID', y='Score')

# Création d'un histogramme en utilisant la méthode create_graph: il faut modifier le nom du df
#graph.create_graph(data=exemple_pd, graph_type='histogram', column='Score')

# Création d'une carte de chaleur en utilisant la méthode create_graph: il faut modifier le nom du df
#graph.create_graph(data=exemple_pd, graph_type='heatmap', x='ID', y='Titre', values='Score')
