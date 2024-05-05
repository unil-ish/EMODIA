#code de sophie pour la classe Movie
import pandas as pd
class Movie:
    def __init__(self, id, title, release_year, rating, votes, genres):
        #id function: id()
        self.id = id
        self.title = title
        self.release_year = release_year
        self.rating = rating
        self.votes = votes
        #self.genres = [] ?
        self.genres = genres

    def get_genres(self):
        genres = []
        with open('movie_dialog/movie_titles_metadata.tsv', 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) >= 6:
                    genres_str = parts[5]
                    genres_str = genres_str.strip('[]')
                    genres.extend(genres_str.split(','))
        return genres

    def release_year(self):
        pass

    def rating(self):
        pass

    def votes(self):
        pass



movie_df = pd.read_csv('movie_dialog/movie_titles_metadata.tsv', sep='\t')
print(movie_df)

movie = Movie('m0', '10 things i hate about you', 1999, 6.90, 62847, [])
print(Movie.get_genres('movie_dialog/movie_titles_metadata.tsv'))