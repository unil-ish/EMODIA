"""
EMODIA est un programme de visualisation de données en ligne de commande.

Il :
1 Rassemble les ressources d'un répertoire pour fournir une interface graphique agréable.
2 Vérifie que les modules ont été importés comme prévu.
3 Demande à l'utilisateur ce qu'il doit faire ensuite.

Quelques remarques sur certaines variables globales :
LOGGER Pointe vers un objet logging.Logger personnalisé afin qu'il puisse être partagé.
TAB Contient l'indentation du texte utilisée pour la CLI et les journaux.
NAME Nom du programme, pour le message de bienvenue.
MESSENGER Alternative print() personnalisée, partagée.
MODULES_DIR Dir pour les modules de traitement des données. Il doit s'agir de fichiers .py valides.
RESOURCES_DIR Emplacement des ressources. Utilisé pour les messages de log, le CLI, etc.

Script principal par Lorelei Chevroulet, 2024
"""

import importlib.util  # To import modules.
import os
import inspect
import sys
from pathlib import Path
from pathlib import PurePath
import math

from matplotlib import pyplot as plt

from core_modules import custom_logger
from core_modules import messenger
from core_modules import utils
from core_modules import module_handler
import random
from modules import read_data
from modules import conversation
from modules import create_graph
from modules import line
from modules import movie
from modules import character
from modules import analysis_navier_stocker
from modules import process_file_lei
from modules import keywords_module
import pandas as pd
import numpy as np
from collections import Counter

import networkx as nx
import netgraph

# INFO
NAME = "EMODIA"
MODULES_DIR = Path("modules")
RESOURCES_DIR = Path("resources")
DATA_DIR = Path("data")

# Utilities
TAB = "    "
LOGGER = object
MESSENGER = None
CWD = Path.cwd()
REL_DATA_DIR = PurePath.joinpath(CWD, DATA_DIR)


class ABCProgram:
    """
    Classe parent pour tous les modules. Permet de partager un logger unique et personnalisé
    et permet d'enregistrer un message avec leur nom lorsqu'ils sont initialisés.
    """

    def __init__(self):
        # Veille à ce que les childs partagent l'enregistreur.
        self.logger = LOGGER
        self.msg = MESSENGER
        self.test = 'hi'

        # Logs tout child initialisé.
        name = self.__class__.__name__
        self.logger.info(f"Initializing {name}", extra={"Type": "🏗️"})


class MainProgram(ABCProgram):
    """Le programme principal, en tant que classe.

    * Gère les messages de démarrage
    * Gère et importe les modules
    * Obtient les entrées utilisateur sur la prochaine action à effectuer.
    """

    def __init__(self):
        """Initialise la classe MainProgram."""
        super().__init__()
        self.program = self
        self.program_info = None
        self.module_handler = None

    def start_program(self):
        """Démarre le programme."""
        self.program_info = ProgramInfo()
        self.program_info.print_logo()

        # Obtenir la liste des modules et les importer.
        module_list = utils.Utils.get_resource(RESOURCES_DIR, "module_list", data_type="json")
        self.module_handler = module_handler.ModuleHandler(self.logger, self.msg, module_list, MODULES_DIR)

        self.msg.log('log_1_modules_check')
        self.module_handler.compare_modules_routine()

        # Importation des données.
        #self.msg.log('log_2_data_import')
        DataImport.create_dataset_routine(self.msg)

        # Entrer dans la boucle du programme.
        self.program_loop()

    def program_loop(self):
        """Boucle principale du programme."""
        commands = Commands(self)
        while True:
            commands.command_dialog()


class ProgramInfo(ABCProgram):
    """
    Obtient le logo et les informations sur l'auteur à partir des ressources, les formate et les affiche.
    """

    def __init__(self):
        """Initialise la classe ProgramInfo."""
        super().__init__()
        self.logo = utils.Utils.get_resource(RESOURCES_DIR, "logo", "txt")
        self.authors: dict = utils.Utils.get_resource(RESOURCES_DIR, "authors", "json")

    def print_logo(self):
        """Affiche le logo."""
        for logo_line in self.logo.splitlines():
            self.msg.say("logo", text=logo_line)
        print()

    def print_authors(self):
        """
        Obtient les contributrices et contributeurs, les trie dans chaque catégorie puis
        les formate et les affiche.
        """
        for (
                key
        ) in (
                self.authors.keys()
        ):  # Chaque clé représente une entrée comme "auteurs", "superviseurs", etc.
            self.authors.update(
                {
                    # Trie les auteurs par nom sous une catégorie 'clé'.
                    key: utils.Utils.sort_dict(self.authors[key], "name")
                }
            )

        # Affiche toutes ces données formatées.
        for category in self.authors.keys():
            self.msg.say(category)
            for person in self.authors[category]:
                # Formatage du nom complet car msg ne peut pas le faire.
                fullname = f"""{person["name"]} {person["surname"]}"""
                self.msg.say(
                    "person_list",
                    fullname=f"{fullname:22}",
                    institution=person["institution"],
                )
            print()


class DataImport(MainProgram):
    def __init__(self):
        super().__init__()

    @classmethod
    def create_dataset_routine(cls, msg):
        """
        Crée le jeu de données en routine.

        :param msg: Objet de messagerie pour l'affichage de messages.
        """
        msg.say('2_import_corpus')
        msg.say('2_1_import_corpus_steps')
        msg.say('corpus_list_art_1')
        msg.say('corpus_list_art_2')
        cls.create_character(msg)
        cls.create_conversation(msg)
        cls.create_movie(msg)
        cls.create_line(msg)
        pass

    @staticmethod
    def create_character(msg):
        """
        Importe les données des personnages.

        :param msg: Objet de messagerie pour l'affichage de messages.
        """
        msg.say('import_character')
        provided_data = read_data.read_data('movie_dialog.zip', path=REL_DATA_DIR,
                                            file_in_zip='movie_characters_metadata.tsv')
        character.Character.create_character_dataset(provided_data)
        msg.say('import_character_ok', number=len(character.Character.all_character_objects))

    @staticmethod
    def create_conversation(msg):
        """
        Importe les données des conversations.

        :param msg: Objet de messagerie pour l'affichage de messages.
        """
        msg.say('import_conversation')
        provided_data = read_data.read_data('movie_dialog.zip', path=REL_DATA_DIR,
                                            file_in_zip='movie_conversations.tsv')
        conversation.Conversation.create_conversation_dataset(provided_data)
        msg.say('import_conversation_ok', number=len(conversation.Conversation.all_conversations_objects))

    @staticmethod
    def create_movie(msg):
        """
        Importe les données des films.

        :param msg: Objet de messagerie pour l'affichage de messages.
        """
        msg.say('import_movie')
        provided_data = read_data.read_data('movie_dialog.zip', path=REL_DATA_DIR,
                                            file_in_zip='movie_titles_metadata.tsv')
        movie.Movie.create_movie_dataset(provided_data)
        msg.say('import_movie_ok', number=len(movie.Movie.all_movies_objects))

    @staticmethod
    def create_line(msg):
        """
        Importe les données des lignes de dialogue.

        :param msg: Objet de messagerie pour l'affichage de messages.
        """
        msg.say('import_line')
        provided_data = read_data.read_data('movie_dialog.zip', path=REL_DATA_DIR,
                                            file_in_zip='movie_lines.tsv')
        line.Line.create_line_dataset(provided_data)
        msg.say('import_line_ok', number=f'{len(line.Line.all_lines_objects):<8}')


class Commands(MainProgram):
    def __init__(self, program):
        super().__init__()
        self.command_dict = {}
        self.program = program

    def command_dialog(self):
        """
        Affiche une liste de commandes disponibles entourée d'une interface utilisateur en ligne de commande.
        Demande une saisie utilisateur et exécute la fonction située à la clé de saisie utilisateur
        dans le dictionnaire.

        Un peu de code supplémentaire pour exécuter les fonctions en tant que méthodes statiques ou
        avec le paramètre self.
        """
        self.msg.say("3_command_selection")
        self.command_dict = self.command_dict_holder()

        # C'est la partie mimi de l'interface utilisateurice en ligne de commande.
        self.msg.say('select_command')
        self.msg.say("command_list_art_1")
        self.msg.say("command_list_art_2")
        for entry, value in self.command_dict.items():
            name = getattr(PresetCommands, value).__doc__
            self.msg.say('command_list', number=f"{entry:>3}", name=name)
        print()

        # Obtient la saisie de l'utilisateurice pour choisir la commande.
        selection = self.command_selection()
        command = getattr(PresetCommands, selection)
        self.msg.log('log_selected_command_value', value=command.__name__)
        print()

        # Vérifie si la commande est statique ou nécessite self.
        if isinstance(inspect.getattr_static(PresetCommands, selection), staticmethod):
            command()
        else:
            command(self.program)

    def command_selection(self) -> str:
        """
        Vérifie la saisie utilisateur et effectue des tentatives forcées jusqu'à ce que les conditions soient remplies.
        """
        selected_command = None
        while not selected_command:
            user_input = input(f"{TAB}{TAB}> ")
            try:
                selected_number = int(user_input)
                self.msg.log('log_selected_command', number=selected_number)
                selected_command = self.command_dict.get(selected_number) or None
                if not selected_command:
                    self.msg.say('invalid_command', name=user_input)

            except ValueError:
                self.msg.say('invalid_number', name=user_input)

        return selected_command

    @staticmethod
    def command_dict_holder() -> dict:
        """"
        Configure un dictionnaire contenant un index et une valeur pointant vers une commande prédéfinie.
        """
        method_list = []
        method_dict = {}

        # Only grab functions starting with "preset_".
        for entry in dir(PresetCommands):
            if not entry.startswith('__'):
                if entry.startswith('preset_'):
                    method_list.append(entry)

        # Using enumerate to have index keys.
        for index, entry in enumerate(method_list):
            method_dict.update({index: entry})
        return method_dict


class PresetCommands(Commands):
    """
    Commandes répertoriées dans la boîte de sélection de commandes.

    Pour fonctionner correctement, les commandes DOIVENT :
    * commencer par 'preset_'
    * contenir une courte docstring (<40 caractères)

    La docstring est primordiale car elle fournira une description de
    la commande à l'utilisateur.
    """

    def __init__(self):
        super().__init__(self.program)

    @staticmethod
    def select_retry():
        """Retiens la sélection de la commande."""
        print('command does not exist :( Try again.')

    @staticmethod
    def preset_stop_program():
        """⏻ Arrêter le programme."""
        sys.exit(0)

    def preset_reload_module(self):
        """↻ Recharger un module."""
        self.module_handler.filtered_list_imported_modules()
        self.msg.say("which_module_reload")
        target_module = input(f"{TAB}>")

        try:
            # Notez que sys.modules[] permet d'obtenir un objet module réel et non une chaîne de caractères.
            status = module_handler.ModuleHandler.reload_module(sys.modules[f'{MODULES_DIR}.{target_module}'])
        except KeyError:
            status = False

        if status:
            self.msg.log('log_reloaded_module', name=target_module)
            self.msg.say('reloaded_module', name=target_module)
        else:
            self.msg.log('log_reloaded_module_error')
            self.msg.say('reloaded_module_error')

    @staticmethod
    def _preset_test_create_graph():
        """Teste create_graph avec des données aléatoires."""

        graph = create_graph.CreateGraph(title='Title', xlabel='x', ylabel='y')
        print(graph)
        exemple_pd = pd.DataFrame(np.random.randint(0, 100, size=(10, 2)), columns=['ID', 'Score'])
        print(exemple_pd)
        graph.create_graph(data=exemple_pd, graph_type='scatter', x='ID', y='Score')

    def preset_display_credits(self):
        """✎ Affiche les crédits du programme."""
        self.program.program_info.print_authors()

    @staticmethod
    def _preset_test_modules():
        """Teste les modules."""
        a = random.choice(movie.Movie.all_movies_id)
        movie_title = movie.Movie.get_title_id(movie.Movie.all_movies_objects[0], a)
        print(f'Movie: {a}, {movie_title}')

        b = random.choice(line.Line.all_lines_id)
        line_content = line.Line.get_line_content(line.Line.all_lines_objects[0], b)
        print(f'Line: {b}, {line_content}')

        c = random.choice(character.Character.all_characters_id)
        character_name = character.Character.get_name_id(character.Character.all_character_objects[0], c)
        print(f'Character: {c}, {character_name}')

        d = random.choice(conversation.Conversation.all_conversations_id)
        conversation_characters = conversation.Conversation.get_characters_id(
            conversation.Conversation.all_conversations_objects[0], d
        )
        print(f'Conversation: {d}, {conversation_characters}')

        extra = []
        for character_id in conversation_characters.values():
            extra.append(character.Character.get_name_id(character.Character.all_character_objects[0], character_id))
        print(f'Conversation Characters: {extra}')

    @staticmethod
    def _preset_test_graph_release_year():
        """Teste le graphique release_year avec des données fictives."""
        df_data_c1 = [2001, 2002, 2003, 2004]
        df_data_c2 = ['11', '12', '13', '14']
        df_data_total = {'Release_year': df_data_c1,
                         'Movie_ID': df_data_c2}
        print(f'data: {df_data_total}')

        df_release_year = pd.DataFrame(data=df_data_total, columns=['Release_year', 'Movie_ID'])
        print(f'dataframe: {df_release_year}')

        graph = create_graph.CreateGraph(title='Analyse temporelle des films', xlabel='Année de sortie',
                                         ylabel='Nb de films')
        print(graph)
        graph.create_graph(data=df_release_year, graph_type='histogram', column='Release_year')

    def preset_graph_release_year(self):
        """⧉ Exécute le graphique des années de sortie."""
        title = 'Distribution Années de sortie.'

        self.msg.say('4_graph_creation', name=title)
        self.msg.say('4_1_graph_access_data')

        self.msg.say('graph_get_data')
        try:
            df_data_c2 = movie.Movie.all_movies_id
            df_data_c1 = movie.Movie.all_release_years_id
            df_data_c1 = list(map(int, df_data_c1))
            self.msg.say('graph_get_data_ok')
        except Exception as e:
            print(e)
            return

        self.msg.say('graph_compute_data')
        try:

            df_data_total = {'Release_year': df_data_c1,
                             'Movie_ID': df_data_c2}
            self.msg.say('graph_compute_data_ok')
        except Exception as e:
            print(e)
            return

        self.msg.say('graph_dataframe_data')
        try:
            df_release_year = pd.DataFrame(data=df_data_total, columns=['Release_year', 'Movie_ID'])
            self.msg.say('graph_dataframe_data_ok')
        except Exception as e:
            print(e)
            return

        self.msg.say('4_2_graph_create')
        try:
            graph = create_graph.CreateGraph(title='Répartition temporelle des films', xlabel='Année de sortie',
                                             ylabel='Nb de films')
            graph.create_graph(data=df_release_year, graph_type='histogram', column='Release_year', bins=2)
            self.msg.say('4_3_success')
        except Exception as e:
            print(e)
            return

    def preset_graph_genres(self):
        """⧉ Exécute le graphique de la distribution Genres de film."""
        title = 'Distribution Genres de film.'

        self.msg.say('4_graph_creation', name=title)
        self.msg.say('4_1_graph_access_data')

        self.msg.say('graph_get_data')
        try:
            df_data_c1 = movie.Movie.all_genres_id
            self.msg.say('graph_get_data_ok')
        except Exception as e:
            print(e)
            return

        self.msg.say('graph_compute_data')
        try:
            xss = df_data_c1  # aplatis la liste
            flat_list = [
                x
                for xs in xss
                for x in xs
            ]

            counted_genres = Counter(flat_list)
            counted_genres['undefined'] = counted_genres.pop('')
            self.msg.say('graph_compute_data_ok')
        except Exception as e:
            print(e)
            return

        self.msg.say('graph_dataframe_data')
        try:
            df_data_total = {'Genres': counted_genres.keys(),
                             'Count': list(map(int, counted_genres.values()))}
            df_genres = pd.DataFrame(data=df_data_total, columns=['Genres', 'Count'])
            df_genres = df_genres.sort_values(['Count']).reset_index(drop=True)
            self.msg.say('graph_dataframe_data_ok')
        except Exception as e:
            print(e)
            return

        self.msg.say('4_2_graph_create')
        try:
            graph = create_graph.CreateGraph(title='Répartition des genres de films', ylabel='Genre',
                                             xlabel='Nombre de films')
            graph.create_graph(data=df_genres, graph_type='bar_chart', y='Genres', x='Count', orient='h', color='coral')
            self.msg.say('4_3_success')
        except Exception as e:
            print(e)
            return

    def preset_graph_rating(self):
        """⧉ Exécute le graphique du nombre notes × Score film."""
        title = 'Nombre notes × Score film'

        self.msg.say('4_graph_creation', name=title)
        self.msg.say('4_1_graph_access_data')

        self.msg.say('graph_get_data')
        try:
            df_data_c1 = movie.Movie.all_votes_id
            df_data_c2 = movie.Movie.all_ratings_id
            df_data_c3 = movie.Movie.all_movies_id
            self.msg.say('graph_get_data_ok')
        except Exception as e:
            print(e)
            return

        self.msg.say('graph_compute_data')
        try:
            df_data_total = {
                'Votes': df_data_c1,
                'Ratings': df_data_c2,
                'Movie': df_data_c3,
            }
            self.msg.say('graph_compute_data_ok')
        except Exception as e:
            print(e)
            return

        self.msg.say('graph_dataframe_data')
        try:
            df_ratings_votes = pd.DataFrame(data=df_data_total, columns=['Votes', 'Ratings'])
            self.msg.say('graph_dataframe_data_ok')
        except Exception as e:
            print(e)
            return

        self.msg.say('4_2_graph_create')
        try:
            graph = create_graph.CreateGraph(title='Distribution Votes x Note', xlabel='Note', ylabel='Votes')
            graph.create_graph(x='Ratings', y='Votes', data=df_ratings_votes, graph_type='scatter', color='coral')
            self.msg.say('4_3_success')
        except Exception as e:
            print(e)
            return

    def preset_graph_credits(self):
        """⧉ Exécute le graphique de position crédits × Genre personnage."""
        title = 'Position crédits × Genre f/m'

        self.msg.say('4_graph_creation', name=title)
        self.msg.say('4_1_graph_access_data')

        self.msg.say('graph_get_data')
        try:
            df_data_c1 = character.Character.all_credits_positions_id
            df_data_c2 = character.Character.all_genders_id
            df_data_c3 = character.Character.all_characters_id
            self.msg.say('graph_get_data_ok')
        except Exception as e:
            print(e)
            return

        self.msg.say('graph_compute_data')
        try:
            df_data_total = {
                'Position': df_data_c1,
                'Gender': df_data_c2,
                'Character_ID': df_data_c3,
            }
            self.msg.say('graph_compute_data_ok')
        except Exception as e:
            print(e)
            return

        self.msg.say('graph_dataframe_data')
        try:
            df = pd.DataFrame(data=df_data_total, columns=['Position', 'Gender', 'Character_ID'])
            mask = df['Position'] == '?'
            df = df[~mask]
            self.msg.say('graph_dataframe_data_ok')
        except Exception as e:
            print(e)
            return

        self.msg.say('4_2_graph_create')
        try:
            graph = create_graph.CreateGraph(title=title, xlabel='Position')
            graph.create_graph(x='Position', data=df, graph_type='box', hue='Gender')
            self.msg.say('4_3_success')
        except Exception as e:
            print(e)
            return

    def preset_graph_dialog_network(self):
        """⧉ Exécute le graphique en réseau des dialogues."""
        title = 'Réseau de dialogues'

        self.msg.say('4_graph_creation', name=title)
        self.msg.say('4_1_graph_access_data')

        self.msg.say('graph_get_data')
        try:
            df_data_c1 = random.sample(movie.Movie.all_movies_objects, 1)
            df_data_c2 = conversation.Conversation.all_conversations_objects
            self.msg.say('graph_get_data_ok')
        except Exception as e:
            print(e)
            return

        self.msg.say('graph_compute_data')
        try:
            movie_id = df_data_c1[0].movie_id
            conversation_list = []
            for entry in df_data_c2:
                if entry.movie_id == movie_id:
                    a = entry.characters_id['character_1']
                    b = entry.characters_id['character_2']

                    a = character.Character.get_name_id(character.Character.all_character_objects[0], a)
                    b = character.Character.get_name_id(character.Character.all_character_objects[0], b)

                    conversation_list.append((a, b))

            c = Counter(map(tuple, conversation_list))
            self.msg.say('graph_compute_data_ok')
        except Exception as e:
            print(e)
            return

        self.msg.say('4_2_graph_create')
        try:
            graph = create_graph.CreateGraph(title=title)
            graph.create_graph(data=c, graph_type='network')
            self.msg.say('4_3_success')
        except Exception as e:
            print(e)
            return

    def preset_graph_sentiment_analysis(self):
        """⧉ Analyse Sentiment dans le temps."""
        title = 'Sentiment × Temps'

        self.msg.say('4_graph_creation', name=title)
        self.msg.say('4_1_graph_access_data')

        self.msg.say('graph_get_data')
        try:
            one_movie = random.sample(movie.Movie.all_movies_objects, 1)[0]
            all_lines = line.Line.all_lines_objects
            self.msg.say('graph_get_data_ok')
        except Exception as e:
            print(e)
            return

        self.msg.say('graph_compute_data')
        try:
            movie_id = one_movie.movie_id

            speaker_list = []
            speech_list = []
            for entry in all_lines:
                if entry.movie_id == movie_id:
                    speaker = entry.character_id  # Get character ID for this line
                    speech = entry.line_content  # Get line content for this line

                    # Get full character name from their ID
                    speaker = character.Character.get_name_id(character.Character.all_character_objects[0], speaker)
                    #b = character.Character.get_name_id(character.Character.all_character_objects[0], b)

                    speaker_list.append(speaker)
                    speech_list.append(speech)

            df_sentiment = {
                'title': None,
                'speaker': speaker_list,
                'speech': speech_list
            }

            df = pd.DataFrame(data=df_sentiment, columns=['title', 'speaker', 'speech'])
            df['title'] = movie_id
            self.msg.say('graph_compute_data_ok')
            senticnet_path = PurePath.joinpath(REL_DATA_DIR, 'senticnet.tsv')
            sent_analysis = process_file_lei.ProcessFile(df, senticnet_path)
            results = sent_analysis.process_speeches()
            try:
                df = results[['ATTITUDE', 'ATTITUDE#anger', 'ATTITUDE#pleasantness', 'POLARITY']].copy()
            except KeyError:
                print(f'{TAB}{TAB}Certaines émotions ne sont pas présentes dans le passage;')
                print(f'{TAB}{TAB}Passage en mode toutes émotions.')
                df = results

        except Exception as e:
            print(e)
            return

        self.msg.say('4_2_graph_create')


        #print(results)
        try:
            graph = create_graph.CreateGraph(title=title, xlabel='Temps', ylabel='Intensité')
            graph.create_graph(data=df, color='coral', graph_type='line')
            self.msg.say('4_3_success')
        except Exception as e:
            print(e)
            return

    def preset_graph_sentiment_analysis_polarity(self):
        """⧉ Analyse Polarité sentiment dans le temps."""
        title = 'Polarité sentiment × Temps'

        self.msg.say('4_graph_creation', name=title)
        self.msg.say('4_1_graph_access_data')

        self.msg.say('graph_get_data')
        try:
            one_movie = random.sample(movie.Movie.all_movies_objects, 1)[0]
            all_lines = line.Line.all_lines_objects
            self.msg.say('graph_get_data_ok')
        except Exception as e:
            print(e)
            return

        self.msg.say('graph_compute_data')
        try:
            movie_id = one_movie.movie_id

            speaker_list = []
            speech_list = []
            for entry in all_lines:
                if entry.movie_id == movie_id:
                    speaker = entry.character_id  # Get character ID for this line
                    speech = entry.line_content  # Get line content for this line

                    # Get full character name from their ID
                    speaker = character.Character.get_name_id(character.Character.all_character_objects[0], speaker)
                    #b = character.Character.get_name_id(character.Character.all_character_objects[0], b)

                    speaker_list.append(speaker)
                    speech_list.append(speech)

            df_sentiment = {
                'title': None,
                'speaker': speaker_list,
                'speech': speech_list
            }

            df = pd.DataFrame(data=df_sentiment, columns=['title', 'speaker', 'speech'])
            df['title'] = movie_id
            self.msg.say('graph_compute_data_ok')
            senticnet_path = PurePath.joinpath(REL_DATA_DIR, 'senticnet.tsv')
            sent_analysis = process_file_lei.ProcessFile(df, senticnet_path)
            results = sent_analysis.process_speeches()

        except Exception as e:
            print(e)
            return

        self.msg.say('4_2_graph_create')

        #print(results)
        try:
            graph = create_graph.CreateGraph(title=title, xlabel='Temps', ylabel='Polarité')
            graph.create_graph(x=results.index, y='POLARITY', data=results, color='coral', graph_type='line')
            self.msg.say('4_3_success')
        except Exception as e:
            print(e)
            return

    def preset_emodia(self):
        """⧉ Analyse via Navier Stocker."""
        title = 'Flux Émotionnels × Temps'

        self.msg.say('4_graph_creation', name=title)
        self.msg.say('4_1_graph_access_data')

        self.msg.say('graph_get_data')
        try:
            one_movie = random.sample(movie.Movie.all_movies_objects, 1)[0]
            all_lines = line.Line.all_lines_objects
            self.msg.say('graph_get_data_ok')
        except Exception as e:
            print(e)
            return

        self.msg.say('graph_compute_data')
        try:
            movie_id = one_movie.movie_id

            speaker_list = []
            speech_list = []
            for entry in all_lines:
                if entry.movie_id == movie_id:
                    speaker = entry.character_id  # Get character ID for this line
                    speech = entry.line_content  # Get line content for this line

                    # Get full character name from their ID
                    speaker = character.Character.get_name_id(character.Character.all_character_objects[0], speaker)
                    #b = character.Character.get_name_id(character.Character.all_character_objects[0], b)

                    speaker_list.append(speaker)
                    speech_list.append(speech)

            df_sentiment = {
                'title': None,
                'speaker': speaker_list,
                'speech': speech_list
            }

            df = pd.DataFrame(data=df_sentiment, columns=['title', 'speaker', 'speech'])
            df['title'] = movie_id
            self.msg.say('graph_compute_data_ok')
            senticnet_path = PurePath.joinpath(REL_DATA_DIR, 'senticnet.tsv')
            sent_analysis = process_file_lei.ProcessFile(df, senticnet_path)
            results = sent_analysis.process_speeches()

            keywords = keywords_module.get_keywords()
            sentiment_dynamics = analysis_navier_stocker.SentimentDynamics(keywords)
            speech_analysis = analysis_navier_stocker.SpeechAnalysis(results, sentiment_dynamics)
            all_s = speech_analysis.calculate_navier_stocker()
            print()

        except Exception as e:
            print(e)
            return

        self.msg.say('4_2_graph_create')

        #print(results)
        try:
            graph = create_graph.CreateGraph(title=title, xlabel='Temps', ylabel='Polarité')
            graph.create_graph(x=results.index, y='POLARITY', data=results, color='coral', graph_type='line')
            self.msg.say('4_3_success')
        except Exception as e:
            print(e)
            return



def main():
    """Fonction principale. Initialise le programme."""
    global LOGGER, MESSENGER  # Il faut que l'état du log et de l'importation des modules soient partagés.
    LOGGER = custom_logger.CustomLogger("logger", log_name=NAME)  # Log partagé et personnalisé
    MESSENGER = messenger.Messenger(RESOURCES_DIR, LOGGER, TAB)

    program = MainProgram()
    program.start_program()
    pass


if __name__ == "__main__":
    main()
