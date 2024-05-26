# code pour la classe Movie

# on importe Pandas afin de créer des DataFrames
import pandas as pd
# on importe des constants spécifiques du module string
# digits = nombres, ascii_lettres = alphabet en miniscule et majuscule
from string import digits, ascii_letters


class Movie:
    # attributs de classe
    all_movies_objects = []  # une liste d'un dictionnaire qui contient tous les objets de movie
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

    # méthodes getter, va chercher un title_id associé à un movie_id
    def get_title_id(self, movie_id):
        # mettre deux listes ensemble et mettre cette liste dans un dictionnaire
        merged_list = dict(zip(self.all_movies_id, self.all_titles_id))
        # cherche l'id movie donné et retourne l'id du title associé
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

    # création de @property pour pouvoir accéder
    # aux attributs de classe (avant __init__)
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
    # chaque méthode prend une liste ID and cherche les attributs associés
    # depuis les listes de classe
    @classmethod
    def get_all_titles(cls, id_list):
        # listes all_movies_id et all_titles_id ensemble dans un dictionnaire
        merged_list = dict(zip(Movie._all_movies_id, Movie._all_titles_id))
        # liste vide pour mettre les titres qui correspondent aux ids dans id_list
        list_all_titles = []
        for ids in id_list:
            # prendre titre associé à l'id et le mettre dans list_all_titles
            list_all_titles.append(merged_list[ids])
        return list_all_titles

    @classmethod
    def get_all_release_years(cls, id_list):
        merged_list = dict(zip(Movie._all_movies_id, Movie._all_release_years_id))
        list_all_release_years = []
        for ids in id_list:
            list_all_release_years.append(merged_list[ids])
        return list_all_release_years

    @classmethod
    def get_all_ratings(cls, id_list):
        merged_list = dict(zip(Movie._all_movies_id, Movie._all_ratings_id))
        list_all_ratings = []
        for ids in id_list:
            list_all_ratings.append(merged_list[ids])
        return list_all_ratings

    @classmethod
    def get_all_votes(cls, id_list):
        merged_list = dict(zip(Movie._all_movies_id, Movie._all_votes_id))
        list_all_votes = []
        for ids in id_list:
            list_all_votes.append(merged_list[ids])
        return list_all_votes

    @classmethod
    def get_all_genres(cls, id_list):
        merged_list = dict(zip(Movie._all_movies_id, Movie._all_genres_id))
        list_all_genres = []
        for ids in id_list:
            list_all_genres.append(merged_list[ids])
        return list_all_genres

    # création d'un DataFrame à partir des listes ID et attributs
    @classmethod
    def create_dataframe(cls, list_ids, attribute_list):
        df = pd.DataFrame(dict(zip(list_ids, attribute_list)))
        return df

    @classmethod
    def create_movie_dataset(cls, provided_data):
        # méthode remplie les attributs de la classe Movie depuis read_data

        for line in provided_data.splitlines():  # split provided_data en lignes
            # print(index, line):
            parts = line.split('\t')
            genres = parts[5].split(' ')  # genres divisés par espaces
            clean_genres = []  # instancie une liste vide
            for entry in genres:
                clean_genre = ''.join(l for l in entry if l in ascii_letters)  # garde seulement lettres ASCII
                clean_genres.append(clean_genre)
            #print(parts)
            # TODO: add proper type handling with try or smth like that
            entries = {
                # clé : valeur
                'movie_id': parts[0],
                'title_id': parts[1],
                'release_year_id': ''.join(d for d in parts[2] if d in digits),
                'ratings_id': float(parts[3]),
                'votes_id': int(parts[4]),
                'genres_id': clean_genres,
            }

            # ajoute le dictionnaire à la liste all_movie_objects
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

        print(f'success! {len(Movie.all_movies_id)} objects created.')


"""class MovieHolder:

    # @staticmethod car méthode peut être appelée sur la classe elle-même
    @staticmethod
    def create_movie_dataset(provided_data):
        # méthode remplie attributs de la classe Movie depuis read_data

        for line in provided_data.splitlines():
            # print(index, line): split le data en lignes
            parts = line.split('\t')
            genres = parts[5].split(' ')
            clean_genres = []  # instancie une liste vide
            for entry in genres:
                clean_genre = ''.join(l for l in entry if l in ascii_letters)  # garde seulement lettres ASCII
                clean_genres.append(clean_genre)
            #print(parts)
            # TODO: add proper type handling with try or smth like that
            entries = {
                'movie_id': parts[0],
                'title_id': parts[1],
                'release_year_id': ''.join(d for d in parts[2] if d in digits),
                'ratings_id': float(parts[3]),
                'votes_id': int(parts[4]),
                'genres_id': clean_genres,
            }

            # ajoute le dictionnaire à la liste all_movie_objects
            Movie.all_movies_objects.append(
                Movie(**entries)  # met le dictionnaire en mots-clés
            )

            # stock les listes individuelles
            Movie.all_movies_id.append(entries['movie_id'])
            Movie.all_titles_id.append(entries['title_id'])
            Movie.all_release_years_id.append(entries['release_year_id'])
            Movie.all_ratings_id.append(entries['ratings_id'])
            Movie.all_votes_id.append(entries['votes_id'])
            Movie.all_genres_id.append(entries['genres_id'])

        print(f'success! {len(Movie.all_movies_id)} objects created.')"""
