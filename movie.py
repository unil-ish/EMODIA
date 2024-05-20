import pandas as pd
# property method / class method


class Movie:
    def __init__(self, movie_id, title, release_year, rating, votes, genres):
        self.movie_id = movie_id
        self.title = title
        self.release_year = release_year
        self.rating = rating
        self.votes = votes
        self.genres = genres

    def get_movie_id(self):
        return self.movie_id

    def get_title(self):
        return self.title

    def get_release_year(self):
        return self.release_year

    def get_rating(self):
        return self.rating

    def get_votes(self):
        return self.votes

    def get_genres(self):
        return self.genres

    # property
    """@property
    def _all_titles_id(self):
        return [(movie.id,movie.title) for movie in Movie.movies] # return list of tuples containing 'id' and 'title'
        # for all movies"""

    # added a method but not sure - just to be able to see the results for now
    @classmethod
    def read_tsv(cls, file_path):
        """Read the TSV file and return its contents as a list."""
        data = [] # holds all the information of the file
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) >= 6:  # the file has at least 6 fields
                    data.append(parts)
        return data

    @classmethod
    def get_all_title(cls):
        data = cls.read_tsv(file_path)
        titles = [] # changé du schéma UML pour être plus lisible
        for parts in data:
            title_str = parts[1] # column numbers
            for title in title_str.split(','): # check if I need this
                titles.append(title)
        return titles

    @classmethod
    def get_all_release_year(cls):
        data = cls.read_tsv(file_path)
        release_years = []
        for parts in data:
            release_year_str = parts[2]
            for release_year in release_year_str.split(','):
                release_years.append(release_year)
        return release_years

    @classmethod
    def get_all_rating(cls):
        data = cls.read_tsv(file_path)
        ratings = []
        for parts in data:
            rating_str = parts[3]
            for rating in rating_str.split(','):
                ratings.append(rating)
        return ratings

    @classmethod
    def get_all_votes(cls):
        data = cls.read_tsv(file_path)
        votes = []
        for parts in data:
            votes_str = parts[4]
            for vote in votes_str.split(','):
                votes.append(vote)
        return votes

    @classmethod
    def get_all_genres(cls):
        data = cls.read_tsv(file_path)
        genres = []
        for parts in data:
            genres_str = parts[5]
            genres_str = genres_str.strip('[]')
            for genre in genres_str.split(','):
                genres.append(genre)
        return genres


# with open('movie_dialog/movie_titles_metadata.tsv', 'r', encoding='utf-8') as file:
#    print(Movie.get_all_title())

file_path = 'movie_dialog/movie_titles_metadata.tsv'
# Ensure data is read into memory
Movie.read_tsv(file_path)

# check it works
# print(Movie.get_all_title())
# print(Movie.get_all_release_year())
# print(Movie.get_all_rating())
# print(Movie.get_all_votes())
# print(Movie.get_all_genres())

all_titles = Movie.get_all_title()
all_release_years = Movie.get_all_release_year()
all_ratings = Movie.get_all_rating()
all_votes = Movie.get_all_votes()
all_genres = Movie.get_all_genres()

test_df = pd.DataFrame(list(zip(all_titles, all_release_years, all_ratings,
                                all_votes, all_genres)),
                       columns=['Title:', 'Release year:', 'Rating:', 'Vote:', 'Genre:'])
print(test_df)
