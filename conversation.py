# code de la classe conversation
import pandas
import pandas as pd


class Conversation:
    def __init__(self, id, characters_id, movie_id, lines):
        self.id = id
        self.characters_id = characters_id        #un dictionnaire qui se présente ainsi : {"character1":u1,"character2":u2}
        self.movie_id = movie_id
        self.lines = lines

        self.all_conversations_id = []      # une liste de tous les id
        self.all_characters_id = []            # une liste de dictionnaires de tous les id de characters
        self.all_movies_id = []                # une liste de tous les id de film
        self.all_lines_id = []                 # une liste de liste de tous les id de line

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
    # le _all ne veut pas dire que la methode retourne tout, mais c'est pour dire qu'on en prend une liste
    @classmethod
    def get_all_characters(cls,id_list):
        merged_list = dict(zip(Conversation._all_conversations_id, Conversation._all_characters_id))
        list_characters = []
        for ids in id_list:
            list_characters.append(merged_list[ids])
        return list_characters

    @classmethod
    def get_all_movie_ids(cls,id_list):
        merged_list = dict(zip(Conversation._all_conversations_id, Conversation._all_movies_id))
        list_all_movies = []
        for ids in id_list:
            list_all_movies.append(merged_list[ids])
        return list_all_movies

    @classmethod
    def get_all_lines(cls,id_list):
        merged_list = dict(zip(Conversation._all_conversations_id, Conversation._all_lines_id))
        list_all_lines = []
        for ids in id_list:
            list_all_lines.append(merged_list[ids])
        return list_all_lines

    # la création du dataframe qui demande une liste d'id de conversation et une autre liste
    @classmethod
    def create_dataframe(cls,list_ids,attribute_list):
        df = pandas.DataFrame(dict(zip(list_ids,attribute_list)))
        return df

################### TOUT CECI DISPARAITRA AU FINAL #######################
# le chemin vers movie_conversations.tsv
tsv_file_path = 'movie_dialog/movie_conversations.tsv'
# on crée un identifiant unique, car le tsv n'en contient pas
conversation_id = 0

# Ouvre le tsv ligne par ligne en encodage utf8 comme movie_conversations.tsv, un peu lent mais fonctionne
with open(tsv_file_path, 'r', encoding="utf8") as tsvfile:
    # on boucle sur chaque ligne du tsv
    for line in tsvfile:

        # pour tester le bon fonctionnement
        # print(line)

        # Sépare les entrées grâce à la tabulation "\t"
        parts = line.strip().split('\t')

        # Crée un objet Conversation et lui attribue les données splitées
        # la première conversation serait : u0	u2	m0	['L194' 'L195' 'L196' 'L197']
        # S'il y a un problème, toute la ligne de données devient "?",
        try:
            conversation_obj = Conversation(conversation_id, parts[2], {"character1":parts[0],"character2":parts[1]}, parts[3])

            # conversation_obj.all_conversations_id.append(conversation_id)
            # conversation_obj.all_characters.append(conversation_obj.characters_id)
        except:
            conversation_obj = Conversation(conversation_id,"?","?","?")

        # pour tester
        # print(conversation_obj.id, conversation_obj.movie_id, conversation_obj.character_id, conversation_obj.lines)

        # on incrémente conversation_id de 1
        conversation_id = conversation_id+1

        # print(conversation_obj.get_characters_id(conversation_obj.id))

