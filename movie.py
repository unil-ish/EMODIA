import pandas as pd


class Movie:
    all_movies_id = [] # une liste de tous les id movie
    all_titles_id = [] # une liste de tous les id titles
    all_release_years_id = [] #
    all_ratings_id = [] #
    all_votes_id = [] #
    all_genres_id = [] #

    def __init__(self, movie_id, title_id, release_year_id, ratings_id, votes_id, genres_id):
        self.movie_id = movie_id # liste de tous les id
        self.title_id = title_id
        self.release_year_id = release_year_id
        self.ratings_id = ratings_id
        self.votes_id = votes_id
        self.genres_id = genres_id

    def get_title_id(self, movie_id):
        merged_list = dict(zip(self.all_movies_id, self.all_titles_id))
        return merged_list[movie_id]

    def get_release_year_id(self, movie_id):
        merged_list = dict(zip(self.all_movies_id, self.all_release_years_id))
        return merged_list[movie_id]

    def get_ratings_id(self, movie_id):
        merged_list = dict(zip(self.all_movies_id, self.all_ratings_id))
        return merged_list[movie_id]

    def get_votes_id(self, movie_id):
        merged_list = dict(zip(self.all_movies_id, self.all_votes_id))
        return merged_list[movie_id]

    def get_genres_id(self, movie_id):
        merged_list = dict(zip(self.all_movies_id, self.all_genres_id))
        return merged_list[movie_id]

    # création de @property pour pouvoir accéder aux attributs (avant __init__)
    @property
    def _all_titles_id(self):
        return self.all_titles_id

    @property
    def _all_release_years_id(self):
        return self.all_release_years_id

    @property
    def _all_ratings_id(self):
        return self._all_ratings_id

    @property
    def _all_votes_id(self):
        return self.all_votes_id

    @property
    def _all_genres_id(self):
        return self.all_genres_id

    @property
    def _all_movies_id(self):  # liste all_movies_id
        return self.all_movies_id

    # création de @classmethod
    @classmethod
    def get_all_titles(cls, id_list):
        merged_list = dict(zip(Movie._all_movies_id, Movie._all_titles_id)) # dictionnaire qui met ensemble les
        # listes all_movie_id and all_titles
        list_all_titles = []
        for ids in id_list:
            list_all_titles.append(merged_list[ids])
        return list_all_titles

    @classmethod
    def get_all_release_years(cls, id_list):
        merged_list = dict(zip(Movie._all_movies_id, Movie._all_release_years_id))
        list_all_release_years_id = []
        for ids in id_list:
            list_all_release_years_id.append(merged_list[ids])
        return list_all_release_years_id

    @classmethod
    def get_all_ratings_id(cls, id_list):
        merged_list = dict(zip(Movie._all_movies_id, Movie._all_ratings_id))
        list_all_ratings_id = []
        for ids in id_list:
            list_all_ratings_id.append(merged_list[ids])
        return list_all_ratings_id

    @classmethod
    def get_all_votes_id(cls, id_list):
        merged_list = dict(zip(Movie._all_movies_id, Movie._all_votes_id))
        list_all_votes_id = []
        for ids in id_list:
            list_all_votes_id.append(merged_list[ids])
        return list_all_votes_id

    @classmethod
    def get_all_genres_id(cls, id_list):
        merged_list = dict(zip(Movie._all_movies_id, Movie._all_genres_id))
        list_all_genres_id = []
        for ids in id_list:
            list_all_genres_id.append(merged_list[ids])
        return list_all_genres_id

    def create_movie_dataset(self, provided_data):
        return


"""title = Movie.get_all_titles(2) # retrieving title with ID 2 from all_titles list
print(f"Title:", title)
ratings = Movie.get_all_ratings(1)
print(f"Rating:", ratings)"""
