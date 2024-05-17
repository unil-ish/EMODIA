import pandas as pd


class Character:
    def __init__(self, character_id, name, movie_id, gender, credits_position):
        self.character_id = character_id
        self.name = name
        self.movie_id = movie_id
        self.gender = gender
        self.credits_position = credits_position

    def get_name(self):
        return self.name

    def get_movie_id(self):
        return self.movie_id

    def get_gender(self):
        return self.gender

    def get_credits_position(self):
        return self.credits_position

    @classmethod
    def read_tsv(cls, file_path):
        data = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) >= 6:  # the file has at least 6 fields
                    data.append(parts)
        return data

    @classmethod
    def get_all_name(cls):
        data = cls.read_tsv(file_path)
        list_all_name = []
        for parts in data:
            name_str = parts[1]
            for name in name_str.split(','):  # check if I need this
                list_all_name.append(name)
        return list_all_name

    @classmethod
    def get_all_movie_id(cls):
        data = cls.read_tsv(file_path)
        list_all_movie_id = []
        for parts in data:
            movie_id_str = parts[2]
            for movie in movie_id_str.split(','):  # check if I need this
                list_all_movie_id.append(movie)
        return list_all_movie_id

    @classmethod
    def get_all_gender(cls):
        data = cls.read_tsv(file_path)
        list_all_gender = []
        for parts in data:
            gender_str = parts[4]
            for gender in gender_str.split(','):  # check if I need this
                list_all_gender.append(gender)
        return list_all_gender

    @classmethod
    def get_all_credits_position(cls):
        data = cls.read_tsv(file_path)
        list_all_credits_position = []
        for parts in data:
            credits_position_str = parts[5]
            for credit in credits_position_str.split(','):  # check if I need this
                list_all_credits_position.append(credit)
        return list_all_credits_position


file_path = 'movie_dialog/movie_characters_metadata.tsv'
Character.read_tsv(file_path)

# testing that it prints correctly
print(Character.get_all_name())
print(Character.get_all_movie_id())
print(Character.get_all_gender())
print(Character.get_all_credits_position())

# put them into variables to be able to call them easily in the DataFrame
all_names = Character.get_all_name()
all_movie_ids = Character.get_all_movie_id()
all_genders = Character.get_all_gender()
all_credits_positions = Character.get_all_credits_position()

character_df = pd.DataFrame(list(zip(all_names, all_movie_ids, all_genders, all_credits_positions)),
                            columns=['Name:', 'Movie ID:', 'Gender:', 'Credits Position:'])
print(character_df)
