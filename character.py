# code pour la classe Characters
import pandas as pd


class Character:
    def __init__(self, id, name, movie_id, gender, credits_position):
        self.id = id
        self.name = name
        self.movie_id = movie_id
        self.gender = gender
        self.credits_position = credits_position

        # do we not have to put them in __init__() ?
        self.get_all_id = [] # --> but can we do this if there is no method ?
        self.get_all_name = []
        self.get_all_movie_id = []
        self.get_all_gender = []
        self.get_all_credits_position = []

    def get_name(self):
        merged_list = dict(zip(self.get_all_id, self.get_all_name))
        return merged_list[id]

    def get_movie_id(self):
        merged_list = dict(zip(self.get_all_id, self.get_all_movie_id))
        return merged_list[id]

    def get_gender(self):
        merged_list = dict(zip(self.get_all_id, self.get_all_gender))
        return merged_list[id]

    def get_credits_position(self):
        merged_list = dict(zip(self.get_all_id, self.get_all_list))
        return merged_list[id]

    @property
    def get_all_name(self):
        return self.get_all_name

    @property
    def get_all_movie_id(self):
        return self.get_all_movie_id

    @property
    def get_all_gender(self):
        return self.get_all_gender

    @property
    def get_all_credits_position(self):
        return self.get_all_credits_position

    @property
    def get_all_characters(self):
        return self.get_all_characters


character_df = pd.read_csv('movie_dialog/movie_characters_metadata.tsv', sep=',') # why works with ',' and not '\t' ?
print(character_df)