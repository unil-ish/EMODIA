# code de la classe conversation
import pandas as pd


class Conversation:
    def __init__(self,id,movie_id,character_id,lines):
        self.id = id
        self.movie_id = movie_id
        self.character_id = character_id
        self.lines = lines

    @classmethod
    def create_dataframe(cls):
        created_dataframe = pd.DataFrame()
        return created_dataframe

    @classmethod
    def sentiment_dynamics(cls,sentiment_data):
        raise NotImplementedError

    @classmethod
    def speech_analysis(cls):
        raise NotImplementedError


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
        except:
            conversation_obj = Conversation(conversation_id,"?","?","?")

        # pour tester
        # print(conversation_obj.id, conversation_obj.movie_id, conversation_obj.character_id, conversation_obj.lines)

        # on incrémente conversation_id de 1
        conversation_id = conversation_id+1