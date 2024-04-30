##code de sophie pour la classe Characters
import pandas as pd
class Character:
    def __init__(self, character_id, name, movie_id, gender, credits_position):
        self.character_id = character_id
        self.name = name
        self.movie_id = movie_id
        self.gender = gender
        self.credits_position = credits_position


characters_df = pd.read_csv('movie_dialog/movie_characters_metadata.tsv', sep='\t')
print(characters_df)
