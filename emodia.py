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
    HEADER = '\033[1m░   '
    LOGO_LINE = '\033[48;5;216m \033[48;0m   \033[1m\033[38;5;216m'
    PATH = '\033[94m'
    SCSS = '\033[92m\033[1m'
    NL = '\n'


class Program:
    """Class handling the general program startup."""

    # PROGRAM INFO
    NAME = 'EMODIA'
    VERSION: int = 0.1
    MODULES_DIR = Path('modules')
    PUBLICATION_YEAR: int = 2024

    def __init__(self):
        """Saves startup time for further calculations and debugging."""
        self.start_logger()
        logging.info('Instancing Program.')

        self.start_time = time.time()
        logging.info(f'Starting time: {self.start_time}')

        self.authors = "authors"
        self.formatted_authors = self.authors
        self._formatted_logo = "logo"
        self.formatted_logo = self._formatted_logo

        self.welcome_message(self.formatted_logo, self.formatted_authors)
        self.init_program()

    @property
    def get_time(self):
        """Returns EPOCH time of program start. """
        return self.start_time

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
                    f'        {key["name"] + " " + key["surname"]:22}  {key["institution"]}'
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
    def start_logger(cls):
        # Starting a logger with the file name without extension.
        logger = logging.getLogger(cls.__name__)
        logging.basicConfig(
            filename=f'{os.path.splitext(__file__)[0]}.log',
            encoding='utf-8',
            filemode='w',
            level=logging.DEBUG,
            format='%(asctime)s | %(levelname)-8s | %(message)s',
        )

    @classmethod
    def sort_dict(cls, to_sort: dict, key: str):
        return sorted(to_sort, key=lambda d: d[key])

    @classmethod
    def get_resources(cls, resource, data_type):
        with open(Path(f'resources/{resource}.{data_type}'), 'r') as file:
            if data_type == 'json':
                data = json.load(file)
            else:
                data = file.read()
            return data

    @classmethod
    def welcome_message(cls, formatted_logo, formatted_authors):
        """Displays logo, welcome message and credits."""
        logging.info('Displaying logo and welcome message.')
        print(
            f'{Ansi.BOLD}\033[38;5;208m{formatted_logo}\033[0;00m'
        )
        print(
            f'{Ansi.HEADER}Welcome to {Program.NAME}.{Ansi.ENDC}'
        )
        print(
            f'    This program was created by:\n'
            f'{formatted_authors[0]}{2 * chr(10)}' 
            f'    Based on research by:\n'
            f'{formatted_authors[1]}{2 * chr(10)}'
            f'    Under the supervision of:\n'
            f'{formatted_authors[2]}{2 * chr(10)}'
        )

    @classmethod
    def init_program(cls):
        """Handles program initialization and user feedback."""
        logging.info('init_program called: Initializing program.')
        print(
            f'{Ansi.HEADER}Initializing {Program.NAME} version {Program.VERSION}.{Ansi.ENDC}'
        )
        # That's where we check for the necessary modules etc.
        cls.check_modules()

    @classmethod
    def path_error(cls, directory):
        """Returns path error with directory name."""
        return (
            f'       {Ansi.FAIL}ERROR: \'{Ansi.PATH}/{directory}{Ansi.FAIL}\' '
        )

    @classmethod
    def check_modules(cls):
        """Looks for modules."""
        logging.info('Checking for modules...')
        module_dir = cls.MODULES_DIR
        prompt = (
            f'\n       Enter modules directory to try again:'
            f'\n      >'
        )
        print(f'    1.  Looking for modules in \'{Ansi.PATH}/{module_dir}{Ansi.ENDC}\'...')
        while True:
            try:
                if not module_dir.exists():
                    raise FileExistsError('directory not found')
                print(f'       {Ansi.SCSS}Directory found{Ansi.ENDC}.')
                break
            except:
                error_type = 'directory not found'
                print(f'{cls.path_error(module_dir)} {error_type}{Ansi.ENDC}.')
                module_dir = Path(input(prompt))
                print()
        while True:
            try:
                if not len(list(module_dir.glob('*'))) > 0:
                    raise Exception("Directory empty.")
                break
            except:
                error_type = 'directory is empty'
                print(f'{cls.path_error(module_dir)} {error_type}{Ansi.ENDC}.')
                module_dir = Path(input(prompt))
                print()

        print(f'       {Ansi.SCSS}{len(list(module_dir.glob("*")))} module(s) found{Ansi.ENDC}.\n')


class ModulesHandler:
    """Handles modules."""


def main():
    """Main function. Initializes program."""
    program = Program()


if __name__ == '__main__':
    main()
