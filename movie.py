import pandas as pd


class Movie:
    all_movie_id = [0, 1, 2] # examples to see the result and to try to understand
    all_titles = ["Movie 1", "Movie 2", "Movie 3"]
    all_ratings = ["3", "10", "2"]
    all_votes = ["2"]
    all_genres = []

    def __init__(self, movie_id, title, release_year, rating, votes, genres):
        self.movie_id = movie_id
        self.title = title
        self.release_year = release_year
        self.rating = rating
        self.votes = votes
        self.genres = genres

    @classmethod
    def get_all_titles(cls, id):
        merged_list = dict(zip(cls.all_movie_id, cls.all_titles)) # dict zipping lists all_movie_id and all_titles
        return merged_list.get(id) # getting title corresponding to ID from merged_list

    @classmethod
    def get_all_ratings(cls, id):
        merged_list = dict(zip(cls.all_movie_id, cls.all_ratings))  # dict zipping lists all_movie_id and all_titles
        return merged_list.get(id) # use ID to get what you want


title = Movie.get_all_titles(2) # retrieving title with ID 2 from all_titles list
print(f"Title:", title)
ratings = Movie.get_all_ratings(1)
print(f"Rating:", ratings)
