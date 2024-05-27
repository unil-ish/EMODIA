# code de la classe conversation
# on importe pandas pour faire des dataframes
import pandas
import pandas as pd


class Conversation:
    all_conversations_objects = []
    all_conversations_id = []  # une liste de tous les id
    all_characters_id = []  # une liste de dictionnaires de tous les id de characters
    all_movies_id = []  # une liste de tous les id de film
    all_lines_id = []  # une liste de liste de tous les id de line

    def __init__(self, conversation_id, characters_id, movie_id, lines):
        self.id = conversation_id
        self.characters_id = characters_id  #un dictionnaire qui se présente ainsi : {"character1":u1,"character2":u2}
        self.movie_id = movie_id
        self.lines = lines

    # les getter qui prennent un conversation_id en input, pour retourner la valeur cherchée correspondante
    def get_characters_id(self, conversation_id):
        # on crée un dictionnaire à partir de deux listes : la liste de toutes les id de conversation et la liste
        # des dictionnaires des id de personnages
        merged_list = dict(zip(self.all_conversations_id, self.all_characters_id))
        return merged_list[conversation_id]

    def get_movie_id(self, conversation_id):
        merged_list = dict(zip(self.all_conversations_id, self.all_movies_id))
        return merged_list[conversation_id]

    def get_lines(self, conversation_id):
        merged_list = dict(zip(self.all_conversations_id, self.all_lines_id))
        return merged_list[conversation_id]

    # on crée des @property pour pouvoir accéder aux attributs
    @property
    def _all_characters_id(self):
        return self.all_characters_id

    @property
    def _all_movies_id(self):
        return self.all_movies_id

    @property
    def _all_lines_id(self):
        return self.all_lines_id

    @property
    def _all_conversations_id(self):
        return self.all_conversations_id

    # les classmethod pour accéder à des listes d'éléments voulus, demande une liste de id conversation
    @classmethod
    def get_list_characters(cls, id_list):
        merged_list = dict(zip(Conversation.all_conversations_id, Conversation.all_characters_id))
        list_characters = []
        for ids in id_list:
            list_characters.append(merged_list[ids])
        return list_characters

    @classmethod
    def get_list_movie_ids(cls, id_list):
        merged_list = dict(zip(Conversation.all_conversations_id, Conversation.all_movies_id))
        list_all_movies = []
        for ids in id_list:
            list_all_movies.append(merged_list[ids])
        return list_all_movies

    @classmethod
    def get_list_lines(cls, id_list):
        merged_list = dict(zip(Conversation.all_conversations_id, Conversation.all_lines_id))
        list_all_lines = []
        for ids in id_list:
            list_all_lines.append(merged_list[ids])
        return list_all_lines

    @staticmethod
    def create_conversation_dataset(provided_data):
        # Using enumerate so we don't have to increment a variable.
        for index, line in enumerate(provided_data.splitlines()):
            parts = line.split('\t')

            entries = {
                'conversation_id': index,
                'characters_id': {
                    'character_1': parts[0],
                    'character_2': parts[1],
                },
                'movie_id': parts[2],
                'lines': parts[3:]
            }
            #print(entries)
            # Crée un objet Conversation et lui attribue les données splitées
            # la première conversation serait : u0	u2	m0	['L194' 'L195' 'L196' 'L197']
            # S'il y a un problème, toute la ligne de données devient "?", sauf l'index
            try:
                conversation_obj = Conversation(**entries)

                conversation_obj.all_conversations_id.append(index)
                conversation_obj.all_characters_id.append(conversation_obj.characters_id)
                conversation_obj.all_conversations_objects.append(conversation_obj)
            except TypeError:
                conversation_obj = Conversation(index, "?", "?", "?")
        return
