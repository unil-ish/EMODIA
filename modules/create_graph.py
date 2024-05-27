import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx

# La libririe seaborn est plus adaptée aux dataframe et est construite au-dessus de matplot.


class CreateGraph:
    """
    Déclaration de la classe CreateGraph pour créer différents types de graphiques.
    """

    def __init__(
            self,
            title="Graph title goes here",
            xlabel="x-axis label goes here",
            ylabel="y-axis label goes here",
                ):
        """
        Initialisation de la classe CreateGraph avec en paramètres le titre et le label des axes x et y.

        Args:
            title (str): Le titre du graphique.
            xlabel (str): Le label de l'axe x.
            ylabel (str): Le label de l'axe y.
        """
        sns.set_theme()  # utilise le thème par défaut de Seaborn
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def create_graph(self, data, graph_type, **kwargs):
         """
        Crée un graphique en fonction du type demandé.

        Args:
            data (pd.DataFrame): Les données à utiliser pour le graphique.
            graph_type (str): Le type de graphique à créer.
            **kwargs: Arguments supplémentaires à passer aux fonctions de création de graphique.
        """
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
        elif graph_type == ('network'):
            self.create_network_graph(data, **kwargs)
        elif graph_type == 'dist':
            self.create_dist_chart(data, **kwargs)
        elif graph_type == 'box':
            self.create_box_chart(data, **kwargs)
        else:
            print("Ce type de graphe n'est pas pris en compte par le programme :(")

    #Il est possible d'ajouter d'autres types de graphiques:
    # 1. Déclarer un nouveau type de graphique et définir ses paramètres
    # 2. L'ajouter à la méthde de création de grahpiques

    def create_scatterplot(self, data, x, y, hue=None, palette='magma_r', color=None):
        """
        Création d'un scatterplot.

        Args:
            data (pd.DataFrame): Les données à utiliser pour le graphique.
            x (str): Colonne pour l'axe x.
            y (str): Colonne pour l'axe y.
            hue (str, optional): Colonne pour la couleur des points.
            palette (str, optional): Palette de couleurs à utiliser.
            color (str, optional): Couleur des points.
        """
        sns.scatterplot(x=x, y=y, data=data, hue=hue, color=color)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.tight_layout()
        plt.show()

    def create_histogram(self, data, column, palette=None, bins='auto', discrete=True, color='coral'):
        """
        Création d'un scatterplot.

        Args:
            data (pd.DataFrame): Les données à utiliser pour le graphique.
            x (str): Colonne pour l'axe x.
            y (str): Colonne pour l'axe y.
            hue (str, optional): Colonne pour la couleur des points.
            palette (str, optional): Palette de couleurs à utiliser.
            color (str, optional): Couleur des points.
        """
        with sns.color_palette(palette):
            sns.histplot(data=data[column], discrete=discrete, bins=bins, color=color)
        plt.title(self.title)
        #plt.title('test')
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()

    def create_heatmap(self):
        """
        Création d'une carte de chaleur.

        Args:
            data (pd.DataFrame): Les données à utiliser pour le graphique.
            values (str): Colonne pour les valeurs à afficher.
            x (str): Colonne pour les labels de l'axe x.
            y (str): Colonne pour les labels de l'axe y.
        """
        pivot_table = data.pivot_table(values=values, index=y, columns=x)
        sns.heatmap(data=pivot_table, cmap="coolwarm")
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()

    def create_bar_chart(self, data, x,  hue=None, y=None, orient='v', order=None, rotation=0, palette=None, color=None):
        """
        Création d'un graphique en barres.

        Args:
            data (pd.DataFrame): Les données à utiliser pour le graphique.
            x (str): Colonne pour l'axe x.
            hue (str, optional): Colonne pour la couleur des barres.
            y (str, optional): Colonne pour l'axe y.
            orient (str, optional): Orientation des barres ('v' pour vertical, 'h' pour horizontal).
            order (list, optional): Ordre des catégories.
            rotation (int, optional): Rotation des labels de l'axe x.
            palette (str, optional): Palette de couleurs à utiliser.
            color (str, optional): Couleur des barres.
        """
        plot = sns.catplot(kind='bar', data=data, x=x, y=y, hue=hue, palette=palette, orient=orient, order=order, color=color)
        plot.set_xticklabels(rotation=rotation)
        plt.tight_layout()
        plt.title(self.title, y=1.0, pad=-14)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()

    def create_dist_chart(self, data, x, hue=None, y=None, palette=None, color=None):
        """
        Création d'un graphique de distribution.

        Args:
            data (pd.DataFrame): Les données à utiliser pour le graphique.
            x (str): Colonne pour l'axe x.
            hue (str, optional): Colonne pour la couleur des barres.
            y (str, optional): Colonne pour l'axe y.
            palette (str, optional): Palette de couleurs à utiliser.
            color (str, optional): Couleur des barres.
        """
        sns.histplot(data=data, x=x, y=y, hue=hue, palette=palette, log_scale=False,
                           color=color, stat='proportion', cumulative=True, common_norm=False, fill=False, element='step')
        plt.tight_layout()
        plt.title(self.title, y=1.0, pad=-14)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()

    def create_box_chart(self, data, x, hue=None, y=None, palette=None, color=None):
        """
        Création d'un boxplot.

        Args:
            data (pd.DataFrame): Les données à utiliser pour le graphique.
            x (str): Colonne pour l'axe x.
            hue (str, optional): Colonne pour la couleur des boîtes.
            y (str, optional): Colonne pour l'axe y.
            palette (str, optional): Palette de couleurs à utiliser.
            color (str, optional): Couleur des boîtes.
        """
        #sns.boxplot(data=data, x=x, y=y, hue=hue, palette=palette, color=color, showfliers=False, width=.5, gap=.2)
        sns.catplot(kind='violin', data=data, x=x, y=y, hue=hue, split=True, log_scale=True, gap=0.1, inner=None, palette='Pastel2', legend=False)
        plt.tight_layout()
        plt.title(self.title, y=1.0, pad=-14)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()

    def create_network_graph(self, data, **kwargs):
        """
        Création d'un graphe de réseau.

        Args:
            data (dict): Les données à utiliser pour le graphique sous forme de dictionnaire.
            **kwargs: Arguments supplémentaires pour la création du graphe de réseau.
        """

        # plt ne supporte pas encore les arêtes multiples :( donc nous utilisons le poids
        F = nx.Graph()
        for (a, b), weight in data.items():
            F.add_edge(a, b, weight=weight)

        pos = nx.circular_layout(F)
        nx.draw_networkx_nodes(F, pos, node_color='coral', node_size=10)
        nx.draw_networkx_labels(F, pos, font_size=10, font_weight='bold')


        for edge in F.edges(data='weight'):
            nx.draw_networkx_edges(F, pos, edgelist=[edge], width=edge[2], alpha=0.4, edge_color='coral')

        plt.show()

    def visualize_network_graph(self, data):
        """
        Affichage du graphe de réseau.

        Args:
            data (dict): Les données à utiliser pour le graphique sous forme de dictionnaire.
        """
        plt.figure(figsize=(10, 6))
        pos = nx.spring_layout(G)  # Choisir une disposition pour les nœuds
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, font_weight='bold',
                edge_color='gray')
        plt.title(self.title)
        plt.show()
