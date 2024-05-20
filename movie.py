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
    @property
    def _all_titles_id(self):
        return [(movie.id,movie.title) for movie in Movie.movies] # return list of tuples containing 'id' and 'title'
        # for all movies

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
        """data = cls.read_tsv(file_path)
        list_all_title = []
        for parts in data:
            title_str = parts[1]
            for title in title_str.split(','): # check if I need this
                list_all_title.append(title)
        return list_all_title"""

    @classmethod
    def get_all_release_year(cls):
        data = cls.read_tsv(file_path)
        list_all_release_year = []
        for parts in data:
            release_year_str = parts[2]
            for release_year in release_year_str.split(','):
                list_all_release_year.append(release_year)
        return list_all_release_year

    @classmethod
    def get_all_rating(cls):
        data = cls.read_tsv(file_path)
        list_all_rating = []
        for parts in data:
            rating_str = parts[3]
            for rating in rating_str.split(','):
                list_all_rating.append(rating)
        return list_all_rating

    @classmethod
    def get_all_votes(cls):
        data = cls.read_tsv(file_path)
        list_all_votes = []
        for parts in data:
            votes_str = parts[4]
            for votes in votes_str.split(','):
                list_all_votes.append(votes)
        return list_all_votes

    @classmethod
    def get_all_genres(cls):
        data = cls.read_tsv(file_path)
        list_all_genres = []
        for parts in data:
            genres_str = parts[5]
            genres_str = genres_str.strip('[]')
            for genres in genres_str.split(','):
                list_all_genres.append(genres)
        return list_all_genres


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
                       columns=['Title:', 'Release year:', 'Rating:', 'Votes:', 'Genres:'])
print(test_df)
