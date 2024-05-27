# code pour la classe Movie
import pandas as pd
"""From string import digits, ascii_letters

    On importe des constants spécifiques du module string.
    digits est un string contenant des chiffres (0 à 9).
    ascii_letters est un string contenant des lettres en
    miniscule et en majuscule (abc...ABC...). 

"""
from string import digits, ascii_letters


class Movie:
    # attributs de classe
    all_movies_objects = []  # une liste qui contient tous les objets de movie
    all_movies_id = []  # une liste de tous les id de movie
    all_titles_id = []
    all_release_years_id = []
    all_ratings_id = []
    all_votes_id = []
    all_genres_id = []  # liste de listes de genres de chaque film

    def __init__(self, movie_id, title_id, release_year_id, ratings_id, votes_id, genres_id):
        self.movie_id = movie_id  # id d'un movie en particulier
        self.title_id = title_id
        self.release_year_id = release_year_id
        self.ratings_id = ratings_id
        self.votes_id = votes_id
        self.genres_id = genres_id

    def get_title_id(self, movie_id):
        """Retourne un ID de titre associé à un ID de movie

        Args :
            movie_id : un string qui contient l'ID de movie.

        Returns :
            Mettre ensemble all_movies_id et all_titles_id avec un zip. Ensuite,
            mettre ceci dans un dictionnaire nommé merged_list. Avec cela, on peut
            utiliser l'ID d'un movie pour chercher son titre correspondant.
        """
        merged_list = dict(zip(self.all_movies_id, self.all_titles_id))
        # cherche l'id movie donné et retourne l'id title associé
        return merged_list[movie_id]

    def get_release_year_id(self, movie_id):
        """Retourne un ID de l'année de sortie associée à un ID de movie"""
        merged_list = dict(zip(self.all_movies_id, self.all_release_years_id))
        return merged_list[movie_id]

    def get_ratings_id(self, movie_id):
        """Retourne un ID des notes associées à un ID de movie"""
        merged_list = dict(zip(self.all_movies_id, self.all_ratings_id))
        return merged_list[movie_id]

    def get_votes_id(self, movie_id):
        """Retourne un ID des votes associés à un ID de movie"""
        merged_list = dict(zip(self.all_movies_id, self.all_votes_id))
        return merged_list[movie_id]

    def get_genres_id(self, movie_id):
        """Retourne un ID des genres associés à un ID de movie"""
        merged_list = dict(zip(self.all_movies_id, self.all_genres_id))
        return merged_list[movie_id]

    @property
    def _all_titles_id(self):
        """Accéder à l'attribut de classe all_titles_id

            Returns :
            La création d'une méthode avec un @property permet d'accéder
            aux attributs de classe
        """
        return self.all_titles_id

    @property
    def _all_release_years_id(self):
        """Accéder à l'attribut de classe all_release_years_id"""
        return self.all_release_years_id

    @property
    def _all_ratings_id(self):
        """Accéder à l'attribut de classe all_ratings_id"""
        return self.all_ratings_id

    @property
    def _all_votes_id(self):
        """Accéder à l'attribut de classe all_votes_id"""
        return self.all_votes_id

    @property
    def _all_genres_id(self):
        """Accéder à l'attribut de classe all_genres_id"""
        return self.all_genres_id

    @property
    def _all_movies_id(self):
        """Accéder à l'attribut de classe all_movies_id"""
        return self.all_movies_id

    # création de @classmethod
    @classmethod
    def get_all_titles(cls, id_list):
        """Une liste d'ID de films pour une liste de titres

            Args :
            cls : @classmethod qui accède aux attributs de classe.
            id_list : une liste d'ID de films.

            Returns :
            merged_list contient un dictionnaire avec un zip contenant
            tous les ID de movie et tous les ID de titres. list_all_titles est
            une liste vide qui contiendra les titres qui correspondent aux IDs
            dans id_list (les ID de movie).
        """
        merged_list = dict(zip(Movie._all_movies_id, Movie._all_titles_id))
        list_all_titles = []
        for ids in id_list:
            # prendre titre associé à l'id et le met dans list_all_titles
            list_all_titles.append(merged_list[ids])
        return list_all_titles

    @classmethod
    def get_all_release_years(cls, id_list):
        """Une liste d'ID de films pour une liste d'années de sortie"""
        merged_list = dict(zip(Movie._all_movies_id, Movie._all_release_years_id))
        list_all_release_years_id = []
        for ids in id_list:
            list_all_release_years_id.append(merged_list[ids])
        return list_all_release_years_id

    @classmethod
    def get_all_ratings_id(cls, id_list):
        """Une liste d'ID de films pour une liste de notes"""
        merged_list = dict(zip(Movie._all_movies_id, Movie._all_ratings_id))
        list_all_ratings_id = []
        for ids in id_list:
            list_all_ratings_id.append(merged_list[ids])
        return list_all_ratings_id

    @classmethod
    def get_all_votes_id(cls, id_list):
        """Une liste d'ID de films pour une liste de votes"""
        merged_list = dict(zip(Movie._all_movies_id, Movie._all_votes_id))
        list_all_votes_id = []
        for ids in id_list:
            list_all_votes_id.append(merged_list[ids])
        return list_all_votes_id

    @classmethod
    def get_all_genres_id(cls, id_list):
        """Une liste d'ID de films pour une liste de genres"""
        merged_list = dict(zip(Movie._all_movies_id, Movie._all_genres_id))
        list_all_genres_id = []
        for ids in id_list:
            list_all_genres_id.append(merged_list[ids])
        return list_all_genres_id

    @staticmethod  #
    def create_movie_dataset(provided_data):
        """ Remplir les variables de la classe Movie depuis read_data

                Args :
                    provided_data : châine de caractères contenant des données
                    tabulées où chaque ligne représente un film.

                Returns :
                    La méthode sépare le string de provided_data en parties et
                    extrait les attributs individuels (movie_id, title_id,
                    release_year_id, ratings_id, votes_id et genres_id). Ensuite,
                    elle nettoie les genres afin qu'il n'y ait que des lettres.
                    La méthode instancie de nouveaux objets de Movie et les ajoutent
                    dans une liste nommée 'all_movie_objects'. Par cela, la méthode
                    met à jour les attributs en gardant des listes séparées pour
                    chaque attribut.
        """

        for line in provided_data.splitlines():  # split provided_data en lignes
            parts = line.split('\t')  # split chaque ligne en parties, chaque partie représente un attribut de movie
            genres = parts[5].split(' ')  # genres (partie 5) divisés par des espaces
            clean_genres = []  # instancie une liste vide
            for entry in genres:
                clean_genre = ''.join(l for l in entry if l in ascii_letters)  # garde seulement lettres ASCII
                clean_genres.append(clean_genre)
            # TODO: add proper type handling with try or smth like that
            entries = {
                # clé (attributs) : valeur
                'movie_id': parts[0],
                'title_id': parts[1],
                'release_year_id': ''.join(d for d in parts[2] if d in digits),
                'ratings_id': float(parts[3]),
                'votes_id': int(parts[4]),
                'genres_id': clean_genres,
            }

            Movie.all_movies_objects.append(
                # nouvelle instance de Movie avec valeurs du dictionnaire 'entries'
                Movie(**entries)  # ** décompacter le dictionnaire
            )

            # stock les listes respectives
            Movie.all_movies_id.append(entries['movie_id'])
            Movie.all_titles_id.append(entries['title_id'])
            Movie.all_release_years_id.append(entries['release_year_id'])
            Movie.all_ratings_id.append(entries['ratings_id'])
            Movie.all_votes_id.append(entries['votes_id'])
            Movie.all_genres_id.append(entries['genres_id'])
