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
        """ initialise la conversation
        Args:
            conversation_id (int) : id de la conversation, int car on doit le créer nous-même
            characters_id ({str}) : dictionnaire d'id de personnages
            movie_id (str) : id de film
            lines ([str]) : liste d'id de lignes
        """
        self.id = conversation_id
        self.characters_id = characters_id  #un dictionnaire qui se présente ainsi : {"character1":u1,"character2":u2}
        self.movie_id = movie_id
        self.lines = lines

    def get_characters_id(self, conversation_id):
        """ un getter qui prend un id en input, pour retourner la valeur cherchée correspondante
        on crée un dictionnaire à partir de deux listes : la liste de toutes les id de conversation et la liste
        des dictionnaires des id de personnages, on cherche la valeur associée à la clé fournie
        Args:
            line_id (str) : id de la conversation
        Returns:
            character_id (str) : id de personnage
        Examples:
            >> conversation_id = 3
            >> get_characters_id(conversation_id)
            "u23"
        """
        merged_list = dict(zip(self.all_conversations_id, self.all_characters_id))
        return merged_list[conversation_id]

    def get_movie_id(self, conversation_id):
        """ un getter qui prend un id en input, pour retourner la valeur cherchée correspondante
        Args:
            line_id (str) : id de la conversation
        Returns:
            movie_id (str) : id de film
        Examples:
            >> conversation_id = 3
            >> get_movie_id(conversation_id)
            "m1"
        """
        merged_list = dict(zip(self.all_conversations_id, self.all_movies_id))
        return merged_list[conversation_id]

    def get_lines(self, conversation_id):
        """ un getter qui prend un id en input, pour retourner la valeur cherchée correspondante
        Args:
            line_id (str) : id de la conversation
        Returns:
            line_id ([str]) : liste d'id de lignes
        Examples:
            >> conversation_id = 3
            >> get_lines(conversation_id)
            "['L194' 'L195' 'L196' 'L197']"
        """
        merged_list = dict(zip(self.all_conversations_id, self.all_lines_id))
        return merged_list[conversation_id]

    # on crée des @property pour pouvoir accéder aux attributs
    @property
    def _all_characters_id(self):
        """
        permet de récupérer la liste de dictionnaires des id de personnages
        """
        return self.all_characters_id

    @property
    def _all_movies_id(self):
        """
        permet de récupérer la liste des id de film
        """
        return self.all_movies_id

    @property
    def _all_lines_id(self):
        """
        permet de récupérer la liste des id de lignes
        """
        return self.all_lines_id

    @property
    def _all_conversations_id(self):
        """
        permet de récupérer la liste des id de conversations
        """
        return self.all_conversations_id

    @classmethod
    def get_list_characters(cls, id_list):
        """ un getter qui prend une liste d'id en input, pour retourner une liste de valeurs correspondantes
        Args:
            id_list ([str]) : une liste d'ids de conversations
        Returns:
            list_characters ([str]) : liste d'ids de personnages
        Examples:
            >> id_list = [1,2,3]
            >> get_list_characters(id_list)
            [{1:"u1",2:"u2"},{1:"u3",2:"u4"},{1:"u5",2:"u6"}]
        """
        merged_list = dict(zip(Conversation.all_conversations_id, Conversation.all_characters_id))
        list_characters = []
        for ids in id_list:
            list_characters.append(merged_list[ids])
        return list_characters

    @classmethod
    def get_list_movie_ids(cls, id_list):
        """ un getter qui prend une liste d'id en input, pour retourner une liste de valeurs correspondantes
        Args:
            id_list ([str]) : une liste d'ids de conversations
        Returns:
            list_movies ([str]) : liste d'ids de films
        Examples:
            >> id_list = [1,2,3]
            >> get_list_movie_ids(id_list)
            ["m1,m2,m3"]
        """
        merged_list = dict(zip(Conversation.all_conversations_id, Conversation.all_movies_id))
        list_movies = []
        for ids in id_list:
            list_movies.append(merged_list[ids])
        return list_movies

    @classmethod
    def get_list_lines(cls, id_list):
        """ un getter qui prend une liste d'id en input, pour retourner une liste de valeurs correspondantes
        Args:
            id_list ([str]) : une liste d'ids de conversations
        Returns:
            list_lines ([str]) : liste d'ids de lignes
        Examples:
            >> id_list = [1,2,3]
            >> get_list_lines(id_list)
            ["L1,L2,L3"]
        """
        merged_list = dict(zip(Conversation.all_conversations_id, Conversation.all_lines_id))
        list_lines = []
        for ids in id_list:
            list_lines.append(merged_list[ids])
        return list_lines

    @staticmethod
    def create_conversation_dataset(provided_data):
        """lit les données du dataset et créé des objets Conversation
        Args:
            provided_data (str) : les données lues
        Returns:

        Examples:
            >> provided_data = "u0	u2	m0	['L194' 'L195' 'L196' 'L197']"
            >> Line.create_conversation_dataset(provided_data)
        """
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
