import logging
import numpy as np
import pandas as pd
from scipy.integrate import odeint
from tqdm.auto import tqdm

class SentimentDynamics:
    def __init__(self, keywords):
        self.keywords = keywords

    def calculate_sentiment_density(self, sentiment_scores):
        return np.sum(np.abs(sentiment_scores))

    def calculate_sentiment_pressure(self, score, text):
        pressure = 0
        if any(keyword.lower() in text.lower() for keyword in self.keywords):
            pressure += score
        return pressure

    def calculate_sentiment_viscosity(self, sentiment_scores):
        return np.std(sentiment_scores)

    @staticmethod
    def calculate_external_contextual_force(polarity):
        return polarity

    def navier_stokes_sentiment_flow(self, rho_sent, p_sent, nu_sent, g_context, s):
        if rho_sent == 0:
            pressure_term = np.zeros_like(s)
        else:
            pressure_term = -1 / rho_sent * np.gradient(p_sent)
        
        grad_s = np.gradient(s)
        laplacian_s = np.gradient(grad_s)
        
        if np.any(np.isnan(s)) or np.any(np.isinf(s)) or np.any(np.isnan(grad_s)) or np.any(np.isinf(grad_s)):
            logging.warning("Warning: NaN or inf detected in s or grad_s. Skipping this iteration.")
            return None

        convective_term = s * grad_s
        viscous_term = nu_sent * laplacian_s
        
        rhs = convective_term + pressure_term + viscous_term + g_context
        
        np.clip(rhs, -1e10, 1e10, out=rhs)
        
        if np.any(np.isnan(rhs)) or np.any(np.isinf(rhs)):
            logging.warning("Warning: NaN or inf detected in rhs. Skipping this iteration.")
            return None
        
        logging.debug(f"Sentiment flow: {rhs}")
        
        return rhs

class SpeechAnalysis:
    def __init__(self, data, sentiment_dynamics):
        self.data = data
        self.sentiment_dynamics = sentiment_dynamics

    @staticmethod
    def differential_equation(s, t, speech_info):
        rho_sent, p_sent, nu_sent, g_context = speech_info
        dsdt = SentimentDynamics.navier_stokes_sentiment_flow(rho_sent, p_sent, nu_sent, g_context, s)
        if dsdt is None:
            raise ValueError("Invalid sentiment flow calculation")
        return dsdt

    @staticmethod
    def remove_duplicates(all_results):
        unique_results = []
        seen_speeches = set()
        for sim_result, current_speech in all_results:
            if current_speech not in seen_speeches:
                seen_speeches.add(current_speech)
                unique_results.append((sim_result, current_speech))
        return unique_results

    def calculate_navier_stocker(self):
        all_s = {}
        sentiment_columns = self.data.columns.difference(['title','speaker', 'speech', 'POLARITY'])
        
        for speaker in tqdm(self.data['speaker'].unique(), desc="Processing speakers"):
            speaker_data = self.data[self.data['speaker'] == speaker]
            title = speaker_data.iloc[0]['title']
            logging.info(f"Processing speaker: {speaker}, number of speeches: {len(speaker_data)}")
            

        return all_s




#ATTENTION: You have to map your_df columns to the columns' names: 'title', 'speaker', 'speech' before using this class.


# Example use
# from process_file import ProcessFile
# from sentiment_dynamics import SentimentDynamics
# from analysis_navier_stocker import SpeechAnalysis
#
#processed_df = ProcessFile(your_df,"data/senticnet.tsv").process_speeches()

#keywords = positive_words + negative_words
#sentiment_dynamics = SentimentDynamics(keywords)

#speech_analysis = SpeechAnalysis(processed_df, sentiment_dynamics)

#all_s = speech_analysis.calculate_navier_stocker()
