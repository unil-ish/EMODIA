from pathlib import Path
from multiprocessing import Pool, cpu_count
import spacy
import pandas as pd
import math
from tqdm import tqdm
from tqdm.contrib.concurrent import process_map


# tqdm -> progress bar
# spacy -> natural language processing

class ProcessFile:
    """
    Process speeches from a DataFrame using SenticNet data.
    Original by Davide Picca.
    Updated by Lorelei to use multiprocessing, average speed improvement of
    >2x on her MacBook Pro.

    ATTENTION: You have to map your data columns to the columns' names: 'title', 'speaker', 'speech' before using this class.

    Before using this class, you have to install the following packages:
    - spacy
    - pandas
    - tqdm

    You also have to download the English model for spaCy:
    python -m spacy download en_core_web_sm

    """

    categories = None
    senticnet_data = None
    df = None

    def __init__(self, df, senticnet_path):
        self.df = df
        self.senticnet_path = senticnet_path
        self.nlp = spacy.load("en_core_web_sm")
        self.df['speech_processed'] = df['speech'].apply(lambda x: self.nlp(x))
        self.process_status = None

    def process_speeches(self):
        """
        Process speeches from a DataFrame using SenticNet data.

        :return: DataFrame with processed speeches

        """
        # Caricare SenticNet data
        senticnet_data = pd.read_csv(self.senticnet_path, delimiter="\t")
        categories = ['INTROSPECTION', 'TEMPER', 'ATTITUDE', 'SENSITIVITY']

        self.senticnet_data = senticnet_data
        self.categories = categories
        #self.df = self.df

        # Preparare il DataFrame per i risultati
        results = []
        len_df = len(self.df)

        with Pool(processes=(cpu_count() - 1)) as pool:  # Create a pool with one slot fewer than amount of cpu cores.
            print()
            ProcessStatus.print_status()
            test_result = pool.map(self.process_func, range(len_df))
            ProcessStatus.done()
            print()

        # Using tqdm: worse performance than single process. So we don't.
        # test_result = process_map(self.process_func, range(len(self.df)), max_workers=8*cpu_count())
        for row in test_result:
            results.append(row)

        # drop columns with all 0
        results = pd.DataFrame(results).fillna(0)
        results = results.loc[:, (results != 0).any(axis=0)]
        #print(results)
        return results

    def process_func(self, x):
        row = self.df.iloc[x]
        senticnet_data = self.senticnet_data
        categories = self.categories
        speech_processed = row['speech_processed']
        speaker = row['speaker']
        speech = row['speech']
        title = row['title']

        # Accumulators for each category and emotion
        accumulators = {}
        polaritylist = []
        for sent in speech_processed.sents:
            for token in sent:
                token_text = token.text.lower()
                matching_row = senticnet_data[senticnet_data['CONCEPT'] == token_text]
                #logging.debug(f"Token: {token_text}, matching row: {matching_row}")

                if not matching_row.empty:
                    # Find max and min categories
                    max_category = matching_row[categories].astype(float).idxmax(axis=1).iloc[0]
                    min_category = matching_row[categories].astype(float).idxmin(axis=1).iloc[0]

                    primary_emotion = matching_row['PRIMARY EMOTION'].iloc[0]
                    secondary_emotion = matching_row['SECONDAY EMOTION'].iloc[0]

                    if pd.isna(primary_emotion):
                        max_emotion = max_category
                    else:
                        max_emotion = f"{max_category}{matching_row['PRIMARY EMOTION'].iloc[0]}"

                    if pd.isna(secondary_emotion):
                        min_emotion = min_category
                    else:
                        min_emotion = f"{min_category}{matching_row['SECONDAY EMOTION'].iloc[0]}"

                    if max_emotion not in accumulators:
                        accumulators[max_emotion] = []
                    if min_emotion not in accumulators:
                        accumulators[min_emotion] = []

                    accumulators[max_emotion].append(matching_row[max_category].iloc[0])
                    if max_emotion != min_emotion:
                        accumulators[min_emotion].append(matching_row[min_category].iloc[0])

                    polarity = matching_row["POLARITY INTENSITY"].astype(float).iloc[0]
                    #logging.debug(f"Token: {token_text}, polarity: {polarity}")
                    polaritylist.append(polarity)
                else:
                    #print(f"Token: {token_text}, no matching row found")
                    #logging.debug(f"Token: {token_text}, no matching row found")
                    pass

        # Calculate averages for each emotion category
        emotion_avg = {emotion: sum(values) / len(values) if values else 0 for emotion, values in accumulators.items()}

        # Calculate average polarity for the speech
        polarity_avg = {"POLARITY": sum(polaritylist) / len(polaritylist) if polaritylist else 0}

        result_row = {'title': title, "speaker": speaker, "speech": speech, **emotion_avg, **polarity_avg}
        ProcessStatus.print_status(x)
        return result_row


class ProcessStatus:
    """Spinner to show life during analysis."""
    line_up = '\033[F'

    @classmethod
    def print_status(cls, x=0):
        print(f'{cls.line_up}        ▚ analyse en cours..')
        if x % 2 == 1: print(f'{cls.line_up}        ▞ analyse en cours..')

    @classmethod
    def done(cls):
        print(f'{cls.line_up}        ✓ analyse terminée.')
