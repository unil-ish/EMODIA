# code de la classe line
import pandas


class Line:
    # initialisation dans le même ordre que les données dans movie_line.tsv
    all_lines_objects = []
    all_lines_id = []
    all_characters_id = []
    all_movies_id = []
    all_lines_content = []

    def __init__(self, line_id, movie_id, character_id, line_content):
        """ initialise la ligne
        Args:
            line_id (str) : id de la ligne
            movie_id (str) : id de film
            character_id (str) : id de personnage
            line_content (str) : contenu de la ligne
        """
        self.id = line_id
        self.character_id = character_id
        self.movie_id = movie_id
        self.line_content = line_content

    @classmethod
    def get_character_id(cls, line_id):
        """ un getter qui prend un id en input, pour retourner la valeur cherchée correspondante
        on crée un dictionnaire à partir de deux listes : la liste de toutes les id de conversation et la liste
        des id de personnages, on cherche la valeur associée à la clé fournie
        Args:
            line_id (str) : id de la ligne
        Returns:
            character_id (str) : id du personnage
        Examples:
            >> line_id = L3
            >> get_character_id(line_id)
            u23
        """
        merged_list = dict(zip(cls.all_lines_id, cls.all_characters_id))
        return merged_list[line_id]

    def get_movie_id(self, line_id):
        """ un getter qui prend un id en input, pour retourner la valeur cherchée correspondante
        Args:
            line_id (str) : id de la ligne
        Returns:
            movie_id (str) : id du film
        Examples:
            >> line_id = L3
            >> get_movie_id(line_id)
            m12
        """
        merged_list = dict(zip(self.all_lines_id, self.all_movies_id))
        return merged_list[line_id]

    def get_line_content(self, line_id):
        """ un getter qui prend un id en input, pour retourner la valeur cherchée correspondante
        Args:
            line_id (str) : id de la ligne
        Returns:
            character_id (str) : id du personnage
        Examples:
            >> line_id = L3
            >> get_line_content(line_id)
            "bla bla"
        """
        merged_list = dict(zip(self.all_lines_id, self.all_lines_content))
        return merged_list[line_id]

    @property
    def _all_lines_id(self):
        """
        permet de récupérer la liste des id de lignes
        """
        return self.all_lines_id

    @property
    def _all_characters_id(self):
        """
        permet de récupérer la liste des id de personnages
        """
        return self.all_characters_id

    @property
    def _all_movies_id(self):
        """
        permet de récupérer la liste des id de film
        """
        return self.all_movies_id

    @property
    def _all_lines_content(self):
        """
        permet de récupérer la liste des contenus de lignes
        """
        return self.all_lines_content

    # les classmethod pour accéder à des listes d'éléments voulus, demande une liste de id line
    @classmethod
    def get_list_characters_id(cls, id_list):
        """ un getter qui prend une liste d'id en input, pour retourner une liste de valeurs correspondantes
        Args:
            id_list ([str]) : une liste d'ids de ligne
        Returns:
            list_characters_id ([str]) : liste d'ids de personnages
        Examples:
            >> id_list = [L1,L2,L3]
            >> get_list_characters_id(id_list)
            [u1,u2,u3]
        """
        merged_list = dict(zip(Line.all_lines_id, Line.all_characters_id))
        list_characters_id = []
        for ids in id_list:
            list_characters_id.append(merged_list[ids])
        return list_characters_id

    @classmethod
    def get_list_movies_id(cls, id_list):
        """ un getter qui prend une liste d'id en input, pour retourner une liste de valeurs correspondantes
        Args:
            id_list ([str]) : une liste d'ids de lignes
        Returns:
            list_movie_id ([str]) : liste d'ids de films
        Examples:
            >> id_list = [L1,L2,L3]
            >> get_list_movies_id(id_list)
            [m1,m2,m3]
        """
        merged_list = dict(zip(Line.all_lines_id, Line.all_movies_id))
        list_movie_id = []
        for ids in id_list:
            list_movie_id.append(merged_list[ids])
        return list_movie_id

    @classmethod
    def get_list_contents_id(cls, id_list):
        """ un getter qui prend une liste d'id en input, pour retourner une liste de valeurs correspondantes
        Args:
            id_list ([str]) : une liste d'ids de lignes
        Returns:
            list_content ([str]) : liste des contenus de lignes
        Examples:
            >> id_list = [L1,L2,L3]
            >> get_list_contents_id(id_list)
            ["bla1","bla2","bla3"]
        """
        merged_list = dict(zip(Line.all_lines_id, Line.all_lines_content))
        list_content = []
        for ids in id_list:
            list_content.append(merged_list[ids])
        return list_content

    @staticmethod
    def create_line_dataset(provided_data):
        """lit les données du dataset et créé des objets Line
        Args:
            provided_data (str) : les données lues
        Returns:

        Examples:
            >> provided_data = "L1045	u0	m0	BIANCA	They do not!"
            >> Line.create_line_dataset(provided_data)
        """
        for line in provided_data.splitlines():
            parts = line.split('\t')

            try:
                entries = {
                    'line_id': parts[0],
                    'character_id': parts[1],
                    'movie_id': parts[2],
                    'line_content': parts[4],
                }
            except IndexError:
                entries = {}

            try:
                Line.all_lines_objects.append(
                    Line(**entries)
                )
            except (ValueError, TypeError):
                Line.all_lines_objects.append(
                    Line("?", "?", "?", "?")
                )

            Line.all_lines_id.append(entries.get('line_id', '?'))
            Line.all_characters_id.append(entries.get('character_id', '?'))
            Line.all_movies_id.append(entries.get('movie_id', '?'))
            Line.all_lines_content.append(entries.get('line_content', '?'))
