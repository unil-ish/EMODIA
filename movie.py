# code pour la classe Movie
import pandas as pd


class Movie:
    def __init__(self, id, title, release_year, rating, votes, genres):
        # id function: id()
        self.id = id
        self.title = title
        self.release_year = release_year
        self.rating = rating
        self.votes = votes
        # self.genres = [] ?
        self.genres = genres

        self.all_id = [] # get all movie id, inside class or outside?
        self.all_title = []
        self.get_all_release_year = []
        self.get_all_rating = []
        self.get_all_votes = []
        self.get_all_genres = []

    def get_title(self):
        title_list = []
        merged_list = dict(zip([id], title_list)) #id = movie id
        return merged_list

    def get_release_year(self):
        release_list = []
        merged_list = dict(zip([id], release_list))
        return merged_list

    def get_rating(self):
        rating_list = []
        merged_list = dict(zip([id], rating_list))
        return merged_list

    def get_votes(self):
        votes_list = []
        with open('movie_dialog/movie_titles_metadata.tsv', 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) >= 6:
                    #genres are in the 6th column
                    votes_str = parts[4]
                    #take away individual [], all votes go into one []
                    votes_str = votes_str.strip('[]')
                    for vote in votes_str.split(','):
                        votes_list.append(vote)
        return votes_list

        merged_list = dict(zip([id], votes_list))
        return merged_list

    def get_genres(self):
        genres_list = []
        #we don't use then?
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
        #or put movie_id in () method ?
        #pour faire une liste de dictionnaires?
        merged_list = dict(zip([id], genres_list))
        return merged_list

    # all properties, methode doesnt do an action, can access attributes
    @property
    def get_all_title(self):
        return self.get_all_title

    @property
    def get_all_release_year(self):
        return self.get_all_release_year

    @property
    def get_all_rating(self):
        return self.get_all_rating

    @property
    def get_all_votes(self):
        return self.get_all_votes

    @property
    def get_all_genres(self):
        return self.get_all_genres


movie_df = pd.read_csv('movie_dialog/movie_titles_metadata.tsv', sep='\t')
print(movie_df)

movie = Movie('m0', '10 things i hate about you', 1999, 6.90, 62847, [])
print(Movie.get_genres('movie_dialog/movie_titles_metadata.tsv'))
print(Movie.get_votes('movie_dialog/movie_titles_metadata.tsv'))