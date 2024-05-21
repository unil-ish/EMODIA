import pandas as pd


def create_dataframe(data1, data2):
    return pd.DataFrame({'Data1': data1, 'Data2': data2})

#exemple d'utilisation pour créer le dataframe pour les années de sortie:

#df_release_year = pd.DataFrame({'Movie_title': title, 'Release_year': release_year})
