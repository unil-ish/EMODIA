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
        self.id = line_id
        self.character_id = character_id
        self.movie_id = movie_id
        self.line_content = line_content

    # les getter qui prennent un line_id en input, pour retourner la valeur cherchée correspondante
    @classmethod
    def get_character_id(cls, line_id):
        merged_list = dict(zip(cls.all_lines_id, cls.all_characters_id))
        return merged_list[line_id]

    def get_movie_id(self, line_id):
        merged_list = dict(zip(self.all_lines_id, self.all_movies_id))
        return merged_list[line_id]

    def get_line_content(self, line_id):
        merged_list = dict(zip(self.all_lines_id, self.all_lines_content))
        return merged_list[line_id]

    # on crée des @property pour pouvoir accéder aux attributs
    @property
    def _all_lines_id(self):
        return self.all_lines_id

    @property
    def _all_characters_id(self):
        return self.all_characters_id

    @property
    def _all_movies_id(self):
        return self.all_movies_id

    @property
    def _all_lines_content(self):
        return self.all_lines_content

    # les classmethod pour accéder à des listes d'éléments voulus, demande une liste de id line
    @classmethod
    def get_list_characters_id(cls, id_list):
        merged_list = dict(zip(Line.all_lines_id, Line.all_characters_id))
        list_characters_id = []
        for ids in id_list:
            list_characters_id.append(merged_list[ids])
        return list_characters_id

    @classmethod
    def get_list_movies_id(cls, id_list):
        merged_list = dict(zip(Line.all_lines_id, Line.all_movies_id))
        list_movie_id = []
        for ids in id_list:
            list_movie_id.append(merged_list[ids])
        return list_movie_id

    @classmethod
    def get_list_contents_id(cls, id_list):
        merged_list = dict(zip(Line.all_lines_id, Line.all_lines_content))
        list_content = []
        for ids in id_list:
            list_content.append(merged_list[ids])
        return list_content

# utilisé pour la lecture des données
    @staticmethod
    def create_line_dataset(provided_data):
        # fills Line class variables from read_data

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
