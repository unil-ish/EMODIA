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
import glob
import time
import random
import re


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
    LOGO_LINE = '\033[48;5;216m \033[48;0m   '
    PATH = '\033[94m'
    SCSS = '\033[92m\033[1m'


class Program:
    """Class handling the general program startup and functions."""

    NAME = 'EMODIA'
    VERSION: int = 0.1
    MODULES_DIR = Path('modules')
    AUTHORS = {
        # Dictionary containing authors: institution.
        'Lorelei C.': 'Université de Lausanne.',
        'A A': 'Université de Lausanne.'
    }

    RESEARCH_AUTHORS = {
        'Davide Picca': 'Université de Lausanne.'
    }

    SUPERVISORS = {
        'Davide Picca': 'Université de Lausanne.',
        'Johan Cuda': 'Université de Lausanne.'
    }

    PUBLICATION_YEAR: int = 2024

    CREDITS = (
        f'    This program was created by:\n'  # Alphabetical list of authors
        f'{'\n'.join(sorted(f'        {key + ',':18} {value}' for key, value in AUTHORS.items()))}\n'
        f'\n    Based on research by:\n'
        f'{'\n'.join(sorted(f'        {key + ',':18} {value}' for key, value in RESEARCH_AUTHORS.items()))}\n'
        f'\n    Under the supervision of:\n'
        f'{'\n'.join(sorted(f'        {key + ',':18} {value}' for key, value in SUPERVISORS.items()))}\n'
    )

    LOGO = (
        '8888888888 888b     d888  .d88888b.  8888888b. 8888888        d8888 ',
        '888        8888b   d8888 d88P" "Y88b 888  "Y88b  888         d88888 ',
        '888        88888b.d88888 888     888 888    888  888        d88P888 ',
        '8888888    888Y88888P888 888     888 888    888  888       d88P 888 ',
        '888        888 Y888P 888 888     888 888    888  888      d88P  888 ',
        '888        888  Y8P  888 888     888 888    888  888     d88P   888 ',
        '888        888   "   888 Y88b. .d88P 888  .d88P  888    d8888888888 ',
        '8888888888 888       888  "Y88888P"  8888888P" 8888888 d88P     888 '
    )
    FORMATTED_LOGO = f'\n{'\n'.join(f'{Ansi.LOGO_LINE}{line}' for line in LOGO)}\n'

    def __init__(self):
        """Saves startup time for further calculations and debugging."""
        self.start_time = time.time()
        self.welcome_message()
        self.init_program()

    @property
    def get_time(self):
        """Returns EPOCH time of program start. """
        return self.start_time

    @classmethod
    def welcome_message(cls):
        """Displays logo, welcome message and credits."""
        print(
            f'{Ansi.BOLD}\033[38;5;208m{Program.FORMATTED_LOGO}\033[0;00m'
        )
        print(
            f'{Ansi.HEADER}Welcome to {Program.NAME}.{Ansi.ENDC}'
        )
        print(Program.CREDITS)

    @classmethod
    def init_program(cls):
        """Handles program initialization and user feedback."""
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
        module_dir = cls.MODULES_DIR
        prompt = (
            f'\n       Enter modules directory to try again:'
            f'\n      >'
        )
        print(f'    1. Looking for modules in \'{Ansi.PATH}/{module_dir}{Ansi.ENDC}\'...')
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

        print(f'       {Ansi.SCSS}{len(list(module_dir.glob('*')))} module(s) found{Ansi.ENDC}.\n')




def main():
    """Main function. Initializes program."""
    program = Program()


if __name__ == '__main__':
    main()
