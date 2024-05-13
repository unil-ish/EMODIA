"""EMODIA: ÉMotions et DIalogues Analyse
L'objectif principal de ce projet est d'explorer et de quantifier la manière dont les émotions se développent et
 interagissent dans les dialogues des films, en utilisant une approche innovante inspirée des équations de
 Navier-Stokes. Le modèle vise à offrir une nouvelle lentille à travers laquelle examiner les dynamiques émotionnelles
 entre les personnages, permettant une compréhension plus profonde des stratégies narratives et des relations
 interpersonnelles au sein des films.

Le programme permet d'effectuer les tâches suivantes:

* 1
* 2
* 3
* 4
* 5
"""

import sys
import os
from pathlib import Path
import logging
import glob
import time
import random
import re
import json

# PROGRAM INFO
NAME = 'EMODIA'
VERSION: float = 0.1
MODULES_DIR = Path('moduless')
RESOURCES_DIR = Path('resources')
PUBLICATION_YEAR: int = 2024
LOGGER = []


class Ansi:
    CLINE = '\033[2K'
    ENDC = '\033[0m'

    RIGHT = '\033[C'
    UP = '\033[F'
    DOWN = '\033[E'

    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'

    FAIL = '\033[91m'
    WARN = '\033[93m'

    BR_GRE = '\033[92m'
    BR_RED = '\033[93m'
    BR_BLU = '\033[94m'
    BR_MAG = '\033[95m'
    BR_CYA = '\033[96m'

    BG_GRE = '\033[42m'
    BG_RED = '\033[41m'
    BG_BLU = '\033[44m'
    BG_MAG = '\033[45m'
    BG_CYA = '\033[46m'

    BG_BR_GRE = '\033[102m'
    BG_BR_RED = '\033[101m'
    BG_BR_BLU = '\033[104m'
    BG_BR_MAG = '\033[105m'
    BG_BR_CYA = '\033[106m'

    # Custom styles go here.
    HEADER = '\033[1m░   '  # Default header formatting
    LOGO_LINE = '\033[48;5;216m \033[48;0m   \033[1m\033[38;5;216m'  # Formatting for logo
    PATH = '\033[94m'  # File and directory path formatting
    SCSS = '\033[92m\033[1m'  # Success formatting
    NL = '\n'
    TAB = '    '  # Indent level. Default: 4 spaces.


class CustomLogger(logging.Logger):
    """Override the makeRecord method to allow for optional Type arg in logs."""

    def __init__(self, name: str):
        # Starting a logger with the file name without extension.
        super().__init__(name)
        self.propagate = False
        formatter = logging.Formatter(  # Custom formatting
            fmt='%(asctime)-19s | %(levelname)-8s | %(message)-50s | %(Type)s ',
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler = logging.FileHandler(  # Tells logger to use a file named after the program.
            filename=f'{os.path.splitext(__file__)[0]}.log',
            mode='w',
            encoding='utf-8'
        )
        handler.setLevel("INFO")
        handler.setFormatter(formatter)
        self.addHandler(handler)

        self.info('Custom logger initialized. Hi!', extra={"Type": '📝'})

    def makeRecord(self, *args, **kwargs):
        rv = super(CustomLogger, self).makeRecord(*args, **kwargs)
        rv.__dict__["Type"] = rv.__dict__.get("Type", "  ")
        return rv


class ABCProgram:
    """Parent class for all modules."""

    def __init__(self):
        # Ensure children share the logger.
        self.logger = LOGGER

        # Logs any initialized child.
        self.logger.info(f"Initializing {self.__class__.__name__}", extra={"Type": "🏗️"})


class StartProgram(ABCProgram):
    """Class handling the general program startup."""

    def __init__(self):
        """Program initializer: setup logs and variables, then welcomes user and imports modules."""
        super().__init__()
        self.logger.info('Starting Program.', extra={"Type": "✅"})

        # Prints welcome message.
        welcome = WelcomeMessage()
        welcome.welcome_message(welcome)

        self.logger.info(f'Calling start_program().')
        self.start_program()

    @classmethod
    def start_program(cls):
        """Handles program startup and user feedback."""
        LOGGER.info('start_program called: Setting up program.')
        print(
            f'{Ansi.HEADER}Starting {NAME}... {Ansi.ENDC}'
        )
        # That's where we check for the necessary modules etc.
        modules_handler = ModulesHandler()
        modules_handler.check_modules(modules_handler)


class WelcomeMessage(ABCProgram):
    """Handles welcome message."""
    def __init__(self):
        super().__init__()

        self.logger.info(f'{Ansi.TAB}Gathering author information...', extra={"Type": "🚚"})
        self.authors = "authors"
        self.formatted_authors = self.authors
        self.logger.info(f'{Ansi.TAB * 2}Gathered author information.')

        self.logger.info(f'{Ansi.TAB}Gathering logo ASCII art...', extra={"Type": "🚚"})
        self._formatted_logo = "logo"
        self.formatted_logo = self._formatted_logo
        self.logger.info(f'{Ansi.TAB * 2}Gathered logo ASCII art.')

    @classmethod
    def welcome_message(cls, self):
        """Displays logo, welcome message and credits."""
        self.logger.info(f'{Ansi.TAB}Displaying logo and welcome message.')
        print(
            f'{Ansi.BOLD}\033[38;5;208m{self.formatted_logo}\033[0;00m'
        )
        print(
            f'{Ansi.HEADER}Welcome to {NAME} version {VERSION}.{Ansi.ENDC}'
        )
        print(
            f'{Ansi.TAB}This program was created by:\n'
            f'{self.formatted_authors[0]}{2 * chr(10)}'
            f'{Ansi.TAB}Based on research by:\n'
            f'{self.formatted_authors[1]}{2 * chr(10)}'
            f'{Ansi.TAB}Under the supervision of:\n'
            f'{self.formatted_authors[2]}{2 * chr(10)}'
        )

    @property
    def authors(self):
        return self._authors

    @authors.setter
    def authors(self, value):
        self._authors = {}
        raw_authors = self.get_resources(value, "json")
        for key in raw_authors.keys():
            self._authors.update(
                {
                    key:
                        self.sort_dict(
                            raw_authors[key],
                            "name"
                        )
                }
            )

    @property
    def formatted_authors(self):
        return self._formatted_authors

    @formatted_authors.setter
    def formatted_authors(self, authors):
        self._formatted_authors = []
        for type_key in authors:
            self._formatted_authors.append(
                chr(10).join(
                    f'{Ansi.TAB * 2}{key["name"] + " " + key["surname"]:22}  {key["institution"]}'
                    for key in authors[type_key]
                )
            )

    @property
    def formatted_logo(self):
        return self._formatted_logo

    @formatted_logo.setter
    def formatted_logo(self, value):
        logo = self.get_resources(value, "txt")
        self._formatted_logo = f'\n{chr(10).join(f"{Ansi.LOGO_LINE}{line}" for line in logo.splitlines())}\n'

    @classmethod
    def sort_dict(cls, to_sort: dict, key: str):
        return sorted(to_sort, key=lambda d: d[key])

    @classmethod
    def get_resources(cls, resource, data_type):
        with open(Path(f'{RESOURCES_DIR}/{resource}.{data_type}'), 'r') as file:
            if data_type == 'json':
                data = json.load(file)
            else:
                data = file.read()
            return data


class ModulesHandler(ABCProgram):
    """Handles modules."""
    def __init__(self):
        super().__init__()
        self.module_dir = MODULES_DIR
        self.prompt = (
            f'\n{Ansi.TAB * 2}Enter modules directory to try again:'
            f'\n{Ansi.TAB}   >'
        )

    @classmethod
    def path_error(cls, directory):
        """Returns path error with directory name."""
        return (
            f'{Ansi.TAB * 2}{Ansi.FAIL}ERROR: \'{Ansi.PATH}/{directory}{Ansi.FAIL}\' '
        )

    @classmethod
    def check_modules(cls, self):
        """Looks for modules."""
        self.logger.info('Starting check_modules()')

        self.logger.info(f'{Ansi.TAB}Looking for modules in {self.module_dir}.')

        print(f'{Ansi.TAB}1.  Looking for modules in \'{Ansi.PATH}/{self.module_dir}{Ansi.ENDC}\'...')
        self.lookfor_directory()
        self.lookfor_modules()

        print(f'{Ansi.TAB * 2}{Ansi.SCSS}{len(list(self.module_dir.glob("*")))} module(s) found{Ansi.ENDC}.\n')

    def lookfor_directory(self):
        while True:
            try:
                if not self.module_dir.exists():
                    raise FileExistsError('directory not found')
                self.logger.info(f'{Ansi.TAB * 2}Directory found.')
                print(f'{Ansi.TAB * 2}{Ansi.SCSS}Directory found{Ansi.ENDC}.')
                break
            except:
                error_type = 'directory not found'
                self.logger.info(f'{Ansi.TAB * 2}Error: Directory not found.', extra={"Type": "❗"})
                print(f'{self.path_error(self.module_dir)} {error_type}{Ansi.ENDC}.')
                self.module_dir = Path(input(self.prompt))
                print()

    def lookfor_modules(self):
        while True:
            try:
                if not len(list(self.module_dir.glob('*'))) > 0:
                    self.logger.info(f'{Ansi.TAB * 2}Error: Directory empty.', extra={"Type": "❗"})
                    raise Exception("Directory empty.")
                self.logger.info(f'{Ansi.TAB * 2}Modules found.')
                break
            except:
                error_type = 'directory is empty'
                print(f'{cls.path_error(self.module_dir)} {error_type}{Ansi.ENDC}.')
                self.module_dir = Path(input(self.prompt))
                print()

def main():
    """Main function. Initializes program."""
    global LOGGER
    LOGGER = CustomLogger("logger")
    program = StartProgram()


if __name__ == '__main__':
    main()
