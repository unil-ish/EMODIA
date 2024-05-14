#code de sophie pour la classe Characters
import pandas as pd
class Character:
    def __init__(self, id, name, movie_id, gender, credits_position):
        self.id = id
        self.name = name
        self.movie_id = movie_id
        self.gender = gender
        self.credits_position = credits_position

        # do we not have to put them in __init__() ?
        # self.get_all_id = [] --> but can we do this if there is no method ?
        self.get_all_name = []
        self.get_all_movie_id = []
        self.get_all_gender = []
        self.get_all_credits_position = []

    def get_name(self):
        name_list = []
        merged_list = dict(zip([id], name_list))  # id = character id
        return merged_list

    def get_movie_id(self):
        movie_id_list = []
        merged_list = dict(zip([id], movie_id_list))
        return merged_list

    def get_gender(self):
        gender_list = []
        merged_list = dict(zip([id], gender_list))
        return merged_list

    def get_credits_position(self):
        credits_list = []
        merged_list = dict(zip([id], credits_list))
        return merged_list
        # [id] ?

    @property
    def get_all_names(self):
        return self.get_all_names

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