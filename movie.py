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

    def get_title(self, id):
        # title_list = []
        # merged_list = dict(zip([id], title_list)) #id = movie id
        # return merged_list

        # create a dict by zipping two lists together
        merged_list = dict(zip(self.get_all_id, self.get_all_title))
        return merged_list[id]

    def get_release_year(self, id):
        merged_list = dict(zip(self.get_all_id, self.get_all_release_year))
        return merged_list[id]

    def get_rating(self):
        # return self.rating --> *
        merged_list = dict(zip(self.get_all_id, self.get_all_rating))
        return merged_list[id]

    def get_votes(self):
        # votes_list = []
        # with open('movie_dialog/movie_titles_metadata.tsv', 'r', encoding='utf-8') as file:
        #    for line in file:
        #        parts = line.strip().split('\t')
        #        if len(parts) >= 6:
        #            #genres are in the 6th column
        #            votes_str = parts[4]
        #            #take away individual [], all votes go into one []
        #            votes_str = votes_str.strip('[]')
        #            for vote in votes_str.split(','):
        #                votes_list.append(vote)
        # return votes_list

        merged_list = dict(zip(self.get_all_id, self.get_all_votes))
        return merged_list[id]

    def get_genres(self):
        # genres_list = []
        # we don't use then?
        # with open('movie_dialog/movie_titles_metadata.tsv', 'r', encoding='utf-8') as file:
        #    for line in file:
        #        parts = line.strip().split('\t')
        #        if len(parts) >= 6:
                    #genres are in the 6th column
        #            genres_str = parts[5]
        #            #take away individual [], all genres go into one []
        #            genres_str = genres_str.strip('[]')
        #            for genre in genres_str.split(','):
        #                genres_list.append(genre)
        #return genres_list
        #or put movie_id in () method ?
        #pour faire une liste de dictionnaires?
        merged_list = dict(zip(self.get_all_id, self.get_all_genres))
        return merged_list[id]

    # all properties, method doesn't do an action, can access attributes
    # gives a list of all titles, all release years, etc.
    @property
    def _all_id(self):
        return self.all_id

    @property
    def _all_title(self):
        return self.get_all_title

    @property
    def _all_release_year(self):
        return self.get_all_release_year

    @property
    def _all_rating(self):
        return self.get_all_rating

    @property
    def _all_votes(self):
        return self.get_all_votes

    @property
    def _all_genres(self):
        return self.get_all_genres

    @classmethod
    def get_all_title(cls, id_list):
        merged_list = dict(zip(Movie._all_id, Movie._all_title))
        # pourquoi pas all_title = [] comme plus haut ?
        list_title = []
        for ids in id_list:
            list_title.append(merged_list[ids])
        return list_title

    @classmethod
    def get_all_release_year(cls, id_list):
        merged_list = dict(zip(Movie._all_id, Movie._all_release_year))
        list_release_year = []
        for ids in id_list:
            list_release_year.append(merged_list[ids])
        return list_release_year

    @classmethod
    def get_all_rating(cls, id_list):
        merged_list = dict(zip(Movie._all_id, Movie._all_rating))
        list_rating = []
        for ids in id_list:
            list_rating.append(merged_list[ids])
        return list_rating

    @classmethod
    def get_all_votes(cls, id_list):
        merged_list = dict(zip(Movie._all_id, Movie._all_votes))
        list_votes = []
        for ids in id_list:
            list_votes.append(merged_list[ids])
        return list_votes

    @classmethod
    def get_all_genre(cls, id_list):
        merged_list = dict(zip(Movie._all_id, Movie._all_genres))
        list_genres = []
        for ids in id_list:
            list_genres.append(merged_list[ids])
        return list_genres



movie_df = pd.read_csv('movie_dialog/movie_titles_metadata.tsv', sep='\t')
print(movie_df)

movie = Movie('m0', '10 things i hate about you', 1999, 6.90, 62847, [])
print(Movie.get_genres('movie_dialog/movie_titles_metadata.tsv'))
print(Movie.get_votes('movie_dialog/movie_titles_metadata.tsv'))