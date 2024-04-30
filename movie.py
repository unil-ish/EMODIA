#code de sophie pour la classe Movie
import pandas as pd
class Movie:
    def __init__(self, id, title, release_year, rating, votes):
        #id function: id()
        self.id = id
        self.title = title
        self.release_year = release_year
        self.rating = rating
        self.votes = votes
        self.genres = []


movie_df = pd.read_csv('movie_titles_metadata.tsv', sep='\t')
print(movie_df)