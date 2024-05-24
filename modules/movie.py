# code pour la classe Movie
import pandas as pd


class Movie:
    # attributs de classe
    all_movies_id = []  # une liste de tous les id de movie
    all_titles_id = []
    all_release_years_id = []
    all_ratings_id = []
    all_votes_id = []
    all_genres_id = []

    def __init__(self, movie_id, title_id, release_year_id, ratings_id, votes_id, genres_id):
        self.movie_id = movie_id  # id d'un movie en particulier
        self.title_id = title_id
        self.release_year_id = release_year_id
        self.ratings_id = ratings_id
        self.votes_id = votes_id
        self.genres_id = genres_id

    # méthodes getter, donner un title_id associé à un movie_id
    def get_title_id(self, movie_id):
        # mettre deux listes ensemble et mettre cette liste dans un dictionnaire
        merged_list = dict(zip(self.all_movies_id, self.all_titles_id))
        # cherche l'id movie donné et retourne l'id title associé
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

    # création de @property pour pouvoir accéder aux attributs de classe (avant __init__)
    @property
    def _all_titles_id(self):
        return self.all_titles_id

    @property
    def _all_release_years_id(self):
        return self.all_release_years_id

    @property
    def _all_ratings_id(self):
        return self.all_ratings_id

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
        # mettre ensemble listes all_movies_id et all_titles_id, créer un dictionnaire
        merged_list = dict(zip(Movie._all_movies_id, Movie._all_titles_id))  # dictionnaire qui met ensemble les
        # liste vide pour mettre les titres qui correspondent aux ids dans id_list
        list_all_titles = []
        for ids in id_list:
            # prendre titre associé à l'id et le met dans list_all_titles
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

    # création d'un dataframe df
    @classmethod
    def create_dataframe(cls, list_ids, attribute_list):
        df = pd.DataFrame(dict(zip(list_ids, attribute_list)))
        return df


class MovieHolder:
    # chercher le data de movie
    def get_movie(self):
        # appelle la méthode
        return self.movie_dataset()

    @staticmethod
    def movie_dataset():
        # vérifie si les listes sont remplies = True, sinon = False
        if (
            Movie.all_movies_id
            and Movie.all_titles_id
            and Movie.all_release_years_id
            and Movie.all_ratings_id
            and Movie.all_votes_id
            and Movie.all_genres_id
        ):
            return True
        else:
            return False

    """@staticmethod
    def create_movie_dataset(provided_data):
        # fills Conversation class variables from readdata
        movie_data = read_data(provided_data)

        # verifie si les clés "id", "title", etc sont présentes
        for movie in movie_data:
            if 'id' in movie:
                Movie.all_movies_id.append(movie['id'])
            if 'title' in movie:
                Movie.all_titles_id.append(movie['title'])
            if 'release_year' in movie:
                Movie.all_release_years_id.append(movie['release_year'])
            if 'rating' in movie:
                Movie.all_ratings_id.append(movie['rating'])
            if 'votes' in movie:
                Movie.all_votes_id.append(movie['votes'])
            if 'genres' in movie:
                Movie.all_genres_id.append(movie['genres'])

    def read_data(provided_data):
        return provided_data"""
