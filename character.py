#code de sophie pour la classe Characters
import pandas as pd
class Character:
    def __init__(self, id, name, movie_id, gender, credits_position):
        self.id = id
        self.name = name
        self.movie_id = movie_id
        self.gender = gender
        self.credits_position = credits_position

    def gender(self):
        pass

    def credits_position(self):
        pass

character_df = pd.read_csv('movie_dialog/movie_characters_metadata.tsv', sep=',') #why works with ',' and not '\t' ?
print(character_df)