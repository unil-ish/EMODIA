"""
EMODIA is a command-line-interface data visualisation program.

It:
1   Gathers resources from a directory to provide a pleasant GUI.
2   Checks whether modules have been imported as expected.
3   Prompts the user for what to do next.

A note on some globals:
LOGGER  Points to a custom logging.Logger object so that it can be shared.
TAB     Holds the text indent used for the CLI and logs.
NAME    Program name, for welcome message.
MESSENGER     Custom print() alternative, shared.
MODULES_DIR   Dir for data processing modules. These must be valid .py files.
RESOURCES_DIR Where resources are located. Used for log messages, CLI, etc.

Main script by Lorelei Chevroulet, 2024
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
import pandas as pd
import numpy as np
from collections import Counter

import networkx as nx
import netgraph

# PROGRAM INFO
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
    Parent class for all modules. Allows them to share a single, custom logger
    and makes them log a message with their name when they are initialized.
    """

    def __init__(self):
        # Ensure children share the logger.
        self.logger = LOGGER
        self.msg = MESSENGER
        self.test = 'hi'

        # Logs any initialized child.
        name = self.__class__.__name__
        self.logger.info(f"Initializing {name}", extra={"Type": "🏗️"})


class MainProgram(ABCProgram):
    """The main program, as a class.

    * Handles startup messages
    * Manages and imports modules
    * Gets user input as to what to do next.
    """

    def __init__(self):
        super().__init__()
        self.program = self
        self.program_info = None
        self.module_handler = None

    def start_program(self):
        self.program_info = ProgramInfo()
        self.program_info.print_logo()

        module_list = utils.Utils.get_resource(RESOURCES_DIR, "module_list", data_type="json")
        # Looking for, then importing modules.
        self.module_handler = module_handler.ModuleHandler(self.logger, self.msg, module_list, MODULES_DIR)

        self.msg.log('log_1_modules_check')
        self.module_handler.compare_modules_routine()

        #self.msg.log('log_2_data_import')
        DataImport.create_dataset_routine(self.msg)

        # Entering program loop.
        self.program_loop()

    def program_loop(self):
        commands = Commands(self)
        while True:
            commands.command_dialog()


class ProgramInfo(ABCProgram):
    """
    Gets logo and author information from resources, formats and displays them.
    """

    def __init__(self):
        super().__init__()
        self.logo = utils.Utils.get_resource(RESOURCES_DIR, "logo", "txt")
        self.authors: dict = utils.Utils.get_resource(RESOURCES_DIR, "authors", "json")

    def print_logo(self):
        """Print logo."""
        for logo_line in self.logo.splitlines():
            self.msg.say("logo", text=logo_line)
        print()

    def print_authors(self):
        """
        Gets authors, sorts them under each category then
        formats and prints them.
        """
        for (
                key
        ) in (
                self.authors.keys()
        ):  # Each key being an entry like "authors", "supervisors", etc.
            self.authors.update(
                {
                    # Sorts authors by name under a 'key' category.
                    key: utils.Utils.sort_dict(self.authors[key], "name")
                }
            )

        # Print out all that formatted data.
        for category in self.authors.keys():
            self.msg.say(category)
            for person in self.authors[category]:
                # Formatting fullname because msg can't.
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
        msg.say('import_character')
        provided_data = read_data.read_data('movie_dialog.zip', path=REL_DATA_DIR,
                                            file_in_zip='movie_characters_metadata.tsv')
        character.Character.create_character_dataset(provided_data)
        msg.say('import_character_ok', number=len(character.Character.all_character_objects))

    @staticmethod
    def create_conversation(msg):
        msg.say('import_conversation')
        provided_data = read_data.read_data('movie_dialog.zip', path=REL_DATA_DIR,
                                            file_in_zip='movie_conversations.tsv')
        conversation.Conversation.create_conversation_dataset(provided_data)
        msg.say('import_conversation_ok', number=len(conversation.Conversation.all_conversations_objects))

    @staticmethod
    def create_movie(msg):
        msg.say('import_movie')
        provided_data = read_data.read_data('movie_dialog.zip', path=REL_DATA_DIR,
                                            file_in_zip='movie_titles_metadata.tsv')
        movie.Movie.create_movie_dataset(provided_data)
        msg.say('import_movie_ok', number=len(movie.Movie.all_movies_objects))

    @staticmethod
    def create_line(msg):
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
        Prints a list of available commands surrounded by a cute CLI GUI.
        Prompts for user input, and executes function located at user input
        key in dictionary.
        Extra bit of code to execute functions as either static methods or
        with self parameter.
        """
        self.msg.say("3_command_selection")
        self.command_dict = self.command_dict_holder()

        # That's the cute GUI part.
        self.msg.say('select_command')
        self.msg.say("command_list_art_1")
        self.msg.say("command_list_art_2")
        for entry, value in self.command_dict.items():
            name = getattr(PresetCommands, value).__doc__
            self.msg.say('command_list', number=f"{entry:>3}", name=name)
        print()

        # Gets user input to pick command.
        selection = self.command_selection()
        command = getattr(PresetCommands, selection)
        self.msg.log('log_selected_command_value', value=command.__name__)
        print()

        # Checks if command is static or needs self.
        if isinstance(inspect.getattr_static(PresetCommands, selection), staticmethod):
            command()
        else:
            command(self.program)

    def command_selection(self) -> str:
        """
        Checks user input and force attempts until conditions passed.
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
        """
        Setups a dict containing an index and a value pointing to a preset_command.
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
    Commands listed in the command selection prompt.

    To work properly, commands MUST:
    * start with 'preset_'
    * contain a short (<40 chars) docstring

    The docstring is paramount as it will provide a description of
    the command to the user.
    """

    def __init__(self):
        super().__init__(self.program)

    @staticmethod
    def select_retry():
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
            # Note the sys.modules[] to get an actual module object and not string.
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
        """Test create_graph with random data."""

        graph = create_graph.CreateGraph(title='Title', xlabel='x', ylabel='y')
        print(graph)
        exemple_pd = pd.DataFrame(np.random.randint(0, 100, size=(10, 2)), columns=['ID', 'Score'])
        print(exemple_pd)
        graph.create_graph(data=exemple_pd, graph_type='scatter', x='ID', y='Score')

    def preset_display_credits(self):
        """✎ Displays program credits."""
        self.program.program_info.print_authors()

    @staticmethod
    def _preset_test_modules():
        """Grabs a random entry in each dataset, and prints a linked value."""
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
        """Test release_year graph with placeholder data."""
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
        """⧉ Distribution Années de sortie."""
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
        """⧉ Distribution Genres de film."""
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
            xss = df_data_c1  # Flattening the list
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
        """⧉ Nombre notes × Score film."""
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
        """⧉ Position crédits × Genre personnage."""
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
        """⧉ Réseau de dialogues."""
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


def main():
    """Main function. Initializes program."""
    global LOGGER, MESSENGER  # We need the logger and module import status to be shared.
    LOGGER = custom_logger.CustomLogger("logger", log_name=NAME)  # Here's our shared, custom logger.
    MESSENGER = messenger.Messenger(RESOURCES_DIR, LOGGER, TAB)

    program = MainProgram()
    program.start_program()
    pass


if __name__ == "__main__":
    main()
