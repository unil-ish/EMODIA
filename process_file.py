from pathlib import Path

import spacy
import pandas as pd
from tqdm import tqdm


class ProcessFile:

    """
    Process speeches from a DataFrame using SenticNet data.

    ATTENTION: You have to map your data columns to the columns' names: 'title', 'speaker', 'speech' before using this class.

    Before using this class, you have to install the following packages:
    - spacy
    - pandas
    - tqdm

    You also have to download the English model for spaCy:
    python -m spacy download en_core_web_sm

    """

    def __init__(self, df, senticnet_path):
        self.df = df
        self.senticnet_path = senticnet_path
        self.nlp = spacy.load("en_core_web_sm")
        self.df['speech_processed'] = df['speech'].apply(lambda x: self.nlp(x))


    def process_speeches(self):
        """
        Process speeches from a DataFrame using SenticNet data.

        :return: DataFrame with processed speeches

        """
        # Caricare SenticNet data
        senticnet_data = pd.read_csv(self.senticnet_path, delimiter="\t")
        categories = ['INTROSPECTION', 'TEMPER', 'ATTITUDE', 'SENSITIVITY']

        # Preparare il DataFrame per i risultati
        results = []

        for _, row in tqdm(self.df.iterrows(), total=self.df.shape[0]):
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
                        print(f"Token: {token_text}, no matching row found")
                        #logging.debug(f"Token: {token_text}, no matching row found")

            # Calculate averages for each emotion category
            emotion_avg = {emotion: sum(values) / len(values) if values else 0 for emotion, values in accumulators.items()}

            # Calculate average polarity for the speech
            polarity_avg = {"POLARITY": sum(polaritylist) / len(polaritylist) if polaritylist else 0}

            result_row = {'title': title, "speaker": speaker, "speech": speech, **emotion_avg, **polarity_avg}
            results.append(result_row)
        # drop columns with all 0
        results = pd.DataFrame(results).fillna(0)
        results = results.loc[:, (results != 0).any(axis=0)]

        # Verify that directory exists otherwise create it
        Path("results/speeches_processed.csv").parent.mkdir(parents=True, exist_ok=True)
        results.to_csv('results/speeches_processed.csv', index=False)
        return results

