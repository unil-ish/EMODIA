from conversation import Conversation
from line import Line
import pandas

def main():
    #read the data

    # le chemin vers movie_lines.tsv
    # tous les guillemets("") de movie_lines.tsv ont été supprimés
    tsv_file_path = 'movie_dialog/movie_lines.tsv'

    # On crée une liste pour stocker les Line, utile seulement pour l'affichage actuellement
    line_objects = []       #la liste de tous les objets line
    list_line_id = []
    list_char_id = []
    list_content = []

    idx = 0

    # Ouvre le tsv ligne par ligne en encodage utf8 comme movie_lines.tsv, un peu lent mais fonctionne
    with open(tsv_file_path, 'r', encoding="utf8") as tsvfile:
        # on boucle sur chaque ligne du tsv
        for line in tsvfile:

            # Sépare les entrées grâce à la tabulation "\t"
            parts = line.strip().split('\t')

            # Crée un objet Line et lui attribue les données splitées
            # la première ligne serait : L1045	u0	m0	BIANCA	They do not!
            # S'il y a un problème, toute la ligne de données devient "?",
            # par exemple, il manque le line_content à certains endroits, mais c'est un montant négligeable
            try:
                line_obj = Line(parts[0], parts[2], parts[1], parts[4])
                list_line_id.append(parts[0])
                list_char_id.append(parts[1])
                list_content.append(parts[4])
            except:
                line_obj = Line("?", "?", "?", "?")
                list_line_id.append(parts[0])
                list_char_id.append(parts[1])
                list_content.append("")

            # on ajoute la ligne à la liste de lignes
            line_objects.append(line_obj)
            line_obj.all_lines_id.append(parts[0])
            line_obj.all_characters_id.append(parts[1])
            line_obj.all_lines_content.append(parts[4])

            # pour avoir un echantillon de 100 seulement
            if idx == 100:
                break

            idx = idx + 1

            # listtest = line_obj.all_lines_id

            # print(listtest)

    # line_objects contient toutes les instances de Line, pour tester si ça fonctionne
    # for line_obj in line_objects:
    #     print(line_obj.id, line_obj.character_id, line_obj.movie_id, line_obj.line_content)

    from process_file import ProcessFile
    from analysis_navier_stocker import SentimentDynamics
    from analysis_navier_stocker import SpeechAnalysis
    from keywords import get_keywords

    df = pandas.DataFrame({'title': list_line_id, 'speaker': list_char_id, 'speech': list_content})
    print(df)

    # processed_df = ProcessFile(df, "data/senticnet.tsv").process_speeches()

    # keywords = get_keywords()
    # sentiment_dynamics = SentimentDynamics(keywords)

    # speech_analysis = SpeechAnalysis(processed_df, sentiment_dynamics)

    # all_s = speech_analysis.calculate_navier_stocker()


    test = Line.all_characters_id
    print(test)






if __name__ == "__main__":
    main()