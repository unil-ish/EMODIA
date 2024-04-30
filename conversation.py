#code de la classe conversation par virgile
import pandas as pd
class Conversation:
    def __init__(self,id,movie_id,character_id,lines):
        self.id = id
        self.movie_id = movie_id
        self.character_id = character_id
        self.lines = lines()


        @classmethod
        def create_dataframe():
            created_dataframe = pd.DataFrame()
            return created_dataframe
