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

    def genres(self):
        genres_list = []
        with open('movie_dialog/movie_titles_metadata.tsv', 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) >= 6:
                    #genres are in the 6th column
                    genres_str = parts[5]
                    #take away individual [], all genres go into one []
                    genres_str = genres_str.strip('[]')
                    for genre in genres_str.split(','):
                        genres_list.append(genre)
        return genres_list

    def release_year(self):
        pass

    def rating(self):
        pass

    def votes(self):
        pass



movie_df = pd.read_csv('movie_dialog/movie_titles_metadata.tsv', sep='\t')
print(movie_df)

movie = Movie('m0', '10 things i hate about you', 1999, 6.90, 62847, [])
print(Movie.genres('movie_dialog/movie_titles_metadata.tsv'))