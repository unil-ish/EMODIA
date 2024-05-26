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
        merged_list = dict(zip(Line._all_lines_id, Line._all_characters_id))
        list_characters_id = []
        for ids in id_list:
            list_characters_id.append(merged_list[ids])
        return list_characters_id

    # pas nécessaire
    # @classmethod
    # def get_all_characters_id(cls):
    #     return cls.all_characters_id

    @classmethod
    def get_list_movies_id(cls, id_list):
        merged_list = dict(zip(Line._all_lines_id, Line._all_movies_id))
        list_movie_id = []
        for ids in id_list:
            list_movie_id.append(merged_list[ids])
        return list_movie_id

    @classmethod
    def get_list_contents_id(cls, id_list):
        merged_list = dict(zip(Line._all_lines_id, Line._all_lines_content))
        list_content = []
        for ids in id_list:
            list_content.append(merged_list[ids])
        return list_content

    # la création du dataframe qui demande une liste d'id de conversation et une autre liste
    @classmethod
    def create_dataframe(cls, list_ids, attribute_list, another_attribute_list):
        df = pandas.DataFrame(dict(zip(list_ids, attribute_list, another_attribute_list)))
        return df

    @staticmethod
    def create_line_dataset(provided_data):
        # fills Line class variables from read_data

        #print(provided_data)
        for line in provided_data.splitlines():
            #print(index, line)
            #line = str(line)
            parts = line.split('\t')
            #print(parts)

            #             line_obj = Line(parts[0], parts[2], parts[1], parts[4])
            #             list_line_id.append(parts[0])
            #             list_char_id.append(parts[1])
            #             list_content.append(parts[4])
            #         except:
            #             line_obj = Line("?", "?","?","?")
            #             list_line_id.append(parts[0])
            #             list_char_id.append(parts[1])
            #             list_content.append("")

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

        print(f'success! {len(Line.all_lines_objects)} objects created.')

        #print(Line.all_lines_id)

# ################### TOUT CECI DISPARAITRA AU FINAL #######################
# # le chemin vers movie_lines.tsv
# # tous les guillemets("") de movie_lines.tsv ont été supprimés
# tsv_file_path = 'movie_dialog/movie_lines.tsv'
#
# # On crée une liste pour stocker les Line, utile seulement pour l'affichage actuellement
# line_objects = []
# list_line_id =[]
# list_char_id =[]
# list_content = []
#
# idx = 0
#
# # Ouvre le tsv ligne par ligne en encodage utf8 comme movie_lines.tsv, un peu lent mais fonctionne
# with open(tsv_file_path, 'r', encoding="utf8") as tsvfile:
#     # on boucle sur chaque ligne du tsv
#     for line in tsvfile:
#
#         # Sépare les entrées grâce à la tabulation "\t"
#         parts = line.strip().split('\t')
#
#
#
#         # Crée un objet Line et lui attribue les données splitées
#         # la première ligne serait : L1045	u0	m0	BIANCA	They do not!
#         # S'il y a un problème, toute la ligne de données devient "?",
#         # par exemple, il manque le line_content à certains endroits, mais c'est un montant négligeable
#         try:
#             line_obj = Line(parts[0], parts[2], parts[1], parts[4])
#             list_line_id.append(parts[0])
#             list_char_id.append(parts[1])
#             list_content.append(parts[4])
#         except:
#             line_obj = Line("?", "?","?","?")
#             list_line_id.append(parts[0])
#             list_char_id.append(parts[1])
#             list_content.append("")
#
#         # on ajoute la ligne à la liste de lignes
#         line_objects.append(line_obj)
#
#         if idx == 100:
#             break
#         idx = idx+1
#
#         listtest = line_obj.all_lines_id
#
#         print(listtest)
#
# # line_objects contient toutes les instances de Line, pour tester si ça fonctionne
# # for line_obj in line_objects:
# #     print(line_obj.id, line_obj.character_id, line_obj.movie_id, line_obj.line_content)
#
#
#
# from process_file import ProcessFile
# from analysis_navier_stocker import SentimentDynamics
# from analysis_navier_stocker import SpeechAnalysis
# from keywords import get_keywords
#
# df = pandas.DataFrame({'title': list_line_id, 'speaker': list_char_id, 'speech': list_content})
# print (df)
#
# processed_df = ProcessFile(df,"data/senticnet.tsv").process_speeches()
#
# keywords = get_keywords()
# sentiment_dynamics = SentimentDynamics(keywords)
#
# speech_analysis = SpeechAnalysis(processed_df, sentiment_dynamics)
#
# all_s = speech_analysis.calculate_navier_stocker()
#
# # print(Line.get_character_id("L100"))
