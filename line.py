# code de la classe line
class Line:
    # initialisation dans le même ordre que les données dans movie_line.tsv
    def __init__(self, line_id, movie_id, character_id, character_name, line_content):
        self.line_id = line_id
        self.movie_id = movie_id
        self.character_id = character_id
        self.character_name = character_name
        self.line_content = line_content


# le chemin vers movie_lines.tsv
# tous les guillemets("") de movie_lines.tsv ont été supprimés
tsv_file_path = 'movie_dialog/movie_lines.tsv'

# On crée une liste pour stocker les Line, utile seulement pour l'affichage actuellement
line_objects = []

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
            line_obj = Line(parts[0], parts[2], parts[1], parts[3], parts[4])
        except:
            line_obj = Line("?", "?","?","?","?")

        # on ajoute la ligne à la liste de lignes
        line_objects.append(line_obj)

# line_objects contient toutes les instances de Line, pour tester si ça fonctionne
# for line_obj in line_objects:
#     print(line_obj.line_id, line_obj.character_id, line_obj.movie_id, line_obj.character_name, line_obj.line_content)
