import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx

# La libririe seaborn est plus adaptée aux dataframe et est construite au-dessus de matplot.


class CreateGraph:
    """Déclaration de la classe CreateGraph pour créer différents types de graphiques"""

    def __init__(
            self,
            title="Graph title goes here",
            xlabel="x-axis label goes here",
            ylabel="y-axis label goes here",
    ):
    """Initialisation de la classe CreateGraph avec en paramètres le titre et le label des axe x et y"""
        sns.set_theme()  # utilise le thème par défaut de Seaborn
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def create_graph(self, data, graph_type, **kwargs):
    """Créer un graphique en fonction du type demandé"""
        # Todo : match: case
        # match graph_type:
        #   case: 'scatter'
        #       ...
        #
        if graph_type == 'scatter':
            self.create_scatterplot(data, **kwargs)
        elif graph_type == 'histogram':
            self.create_histogram(data, **kwargs)
        elif graph_type == 'heatmap':
            self.create_heatmap(data, **kwargs)
        elif graph_type == 'bar_chart':
            self.create_bar_chart(data, **kwargs)
        elif graph_type == ('network_graph'):
            edges = kwargs.get(edges, character_list)
            G = self.create_network_graph(edges, character_list)
            self.visualize_network_graph(G)
        elif graph_type == 'dist':
            self.create_dist_chart(data, **kwargs)
        elif graph_type == 'box':
            self.create_box_chart(data, **kwargs)
        else:
            print("Ce type de graphe n'est pas pris en compte par le programme :(")

    #Il est possible d'ajouter d'autres types de graphiques: 1. Déclarer un nouveau type de graphique et définir ses paramètres 2. L'ajouter à la méthde de création de grahpiques

    def create_scatterplot(self, data, x, y, hue=None, palette='magma_r', color=None):
    """Création d'un scatterplot."""
        sns.scatterplot(x=x, y=y, data=data, hue=hue, color=color)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.tight_layout()
        plt.show()

    def create_histogram(self, data, column, palette=None, bins='auto', discrete=True, color='coral'):
    """Création d'un histogramme."""
        with sns.color_palette(palette):
            sns.histplot(data=data[column], discrete=discrete, bins=bins, color=color)
        plt.title(self.title)
        #plt.title('test')
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()

    def create_heatmap(self):
    """Création d'une carte de chaleur."""
        pivot_table = data.pivot_table(values=values, index=y, columns=x)
        sns.heatmap(data=pivot_table, cmap="coolwarm")
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()

    def create_bar_chart(self, data, x,  hue=None, y=None, orient='v', order=None, rotation=0, palette=None, color=None):
    """Création d'un graphique en barres."""
        plot = sns.catplot(kind='bar', data=data, x=x, y=y, hue=hue, palette=palette, orient=orient, order=order, color=color)
        plot.set_xticklabels(rotation=rotation)
        plt.tight_layout()
        plt.title(self.title, y=1.0, pad=-14)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()

    def create_dist_chart(self, data, x, hue=None, y=None, palette=None, color=None):
    """Création d'un graphique de distribution."""
        sns.histplot(data=data, x=x, y=y, hue=hue, palette=palette, log_scale=False,
                           color=color, stat='proportion', cumulative=True, common_norm=False, fill=False, element='step')
        plt.tight_layout()
        plt.title(self.title, y=1.0, pad=-14)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()

    def create_box_chart(self, data, x, hue=None, y=None, palette=None, color=None):
    """Création d'un boxplot."""
        #sns.boxplot(data=data, x=x, y=y, hue=hue, palette=palette, color=color, showfliers=False, width=.5, gap=.2)
        sns.catplot(kind='violin', data=data, x=x, y=y, hue=hue, split=True, log_scale=True, gap=0.1, inner=None, palette='Pastel2')
        plt.tight_layout()
        plt.title(self.title, y=1.0, pad=-14)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()

    def create_network_graph(self, dialogue_list):
    """Création d'un grah de réseau."""
        # Initialiser un graphe vide
        G = nx.Graph()

        # Ajouter les arêtes au graphe
        G.add_edges_from(edges)

        return G

    def visualize_network_graph(self, G):
    """Affichage du graph de réseau"""
        # Afficher le graphe de réseau
        plt.figure(figsize=(10, 6))
        pos = nx.spring_layout(G)  # Choisir une disposition pour les nœuds
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, font_weight='bold',
                edge_color='gray')
        plt.title(self.title)
        plt.show()
