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
        pass

    def release_year(self):
        pass

    def rating(self):
        pass

    def votes(self):
        pass



movie_df = pd.read_csv('movie_dialog/movie_titles_metadata.tsv', sep='\t')
print(movie_df)