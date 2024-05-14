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
import math
import random
import re
import json
import inspect
import importlib.util

# Note that any module imported through the program's module importer function will behave as if
# added through the standard 'import module' formula.

# PROGRAM INFO
NAME = 'EMODIA'
VERSION: float = 0.1
MODULES_DIR = Path('modules')  # Directory where each 'module'.py is stored.
RESOURCES_DIR = Path('resources')  # Directory for resources such as authors, logo, etc.
PUBLICATION_YEAR: int = 2024
LOGGER = []  # That's where we will store an instance of the custom logger for use by any function


class Ansi:
    """This class is used for formatting purposes.
    * It uses ANSI escape codes that have an impact on formatting when output to a console or terminal.
    * These codes can be entered in any string, typically by using a fstring such as:
        f'{Ansi.TAB}{Ansi.BR_GRE}This message will be printed in green!{Ansi.ENDC}'
    * It also implements an Ansi.TAB variable to ensure indents are consistent throughout the program."""
    CLINE = '\033[2K'  # Clears line
    ENDC = '\033[0m'  # Remove any existing formatting beyond this point.

    # These codes move the cursor.
    RIGHT = '\033[C'
    UP = '\033[F'
    DOWN = '\033[E'

    # Emphasis effects.
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'

    # Vibes for the error messages.
    FAIL = '\033[91m'
    WARN = '\033[93m'

    # Bright text colors
    BR_GRE = '\033[92m'
    BR_RED = '\033[93m'
    BR_BLU = '\033[94m'
    BR_MAG = '\033[95m'
    BR_CYA = '\033[96m'

    # Background colors
    BG_GRE = '\033[42m'
    BG_RED = '\033[41m'
    BG_BLU = '\033[44m'
    BG_MAG = '\033[45m'
    BG_CYA = '\033[46m'

    # Bright background colors
    BG_BR_GRE = '\033[102m'
    BG_BR_RED = '\033[101m'
    BG_BR_BLU = '\033[104m'
    BG_BR_MAG = '\033[105m'
    BG_BR_CYA = '\033[106m'

    # Custom styles go here.
    HEADER = f'\033[1m░   '  # Default header formatting
    LOGO_LINE = '\033[48;5;216m \033[48;0m   \033[1m\033[38;5;216m'  # Formatting for logo
    PATH = '\033[94m'  # File and directory path formatting
    SCSS = '\033[92m\033[1m'  # Success formatting
    NL = '\n'  # Inserts newline. Identical to using chr(10).
    TAB = '    '  # Indent level. Default: 4 spaces.


class CustomLogger(logging.Logger):
    """A custom logger class.
    Overrides the makeRecord method to allow for optional Type arg in logs.
    In our case, we use it to add emojis at the end of log messages for easier human parsing.
    The following methods can be used:
    * .info(str, **extra={"Type":str})
    * .warning(str, **extra={"Type":str})
    * .error(str, **extra={"Type":str})
    """

    def __init__(self, name: str):
        """Initializes a custom logger as child of default python logger class.
        Has a custom log message format with additional 'Type' field.
        The logs are saved in a single file, named after the program's name."""
        super().__init__(name)  # Inherit from default python logger class
        self.propagate = False  # See Python logging docs

        formatter = logging.Formatter(  # Saves a custom format in a logging.Formatter scheme
            fmt='%(asctime)-19s | %(levelname)-7s | %(message)-50s | %(Type)s ',  # Note the extra 'Type' field.
            datefmt="%Y-%m-%d %H:%M:%S"  # Date format, removes the milliseconds that are usually added
        )
        handler = logging.FileHandler(  # Saves a custom handler in a logging.FileHandler scheme.
            filename=f'{os.path.splitext(__file__)[0]}.log',  # Names the log file after the program's name.
            mode='w',  # Overwrite log file if it exists, then appends logs messages to it.
            encoding='utf-8'
        )
        handler.setLevel("INFO")  # Tells our logger to look for any message of severity higher or equal to INFO.
        handler.setFormatter(formatter)  # Sets the logger's format to our custom format.

        self.addHandler(handler)  # Tells the logger to use our custom handler as output handler -> outputs to file.

        self.info('Custom logger initialized. Hi!', extra={"Type": '📝'})

    def makeRecord(self, *args, **kwargs):
        """Overrides the logger's makeRecord method to make extra arguments optional.
        makeRecord is called whenever we do logger.info(), warn(), or any other logger message function.
        This extra argument must be added as extra{"Type": string}. See log message at the end of __init__
        for an example."""
        rv = super(CustomLogger, self).makeRecord(*args, **kwargs)
        rv.__dict__["Type"] = rv.__dict__.get("Type", "  ")
        return rv


class ABCProgram:
    """Parent class for all modules. Allows them to share a single, custom logger and makes them print
    a log message with their name when they are initialized.
    For more info on logger, see the CustomLogger class."""

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
        welcome = ProgramInfo()
        welcome.say_welcome()

        self.logger.info(f'Calling start_program().')
        self.start_program()

    def start_program(self):
        """Handles program startup and user feedback."""
        self.logger.info('start_program called: Setting up program.')
        print(
            f'{Ansi.HEADER}Starting {NAME}... {Ansi.ENDC}'
        )
        # That's where we check for the necessary modules etc.
        modules_handler = ModulesHandler()
        # Looks for modules in the MODULES_DIR directory. Allows user to pick another dir if dir is empty.
        modules_handler.modules_checker()
        # Tries to import all the modules within the directory, with confirmation of import status.
        modules_handler.modules_importer()


class ProgramInfo(ABCProgram):
    """Handles welcome message.
    * Stores some variables within ProgramInfo for easy access if any modules ends up needing them. It's nicer
        to only do the file opening and content formatting once and be able to recall it at will instead of redoing
        it every time someone may want to see the credits (which is hopefully often :)).
    """

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

        self._formatted_welcome = str
        self.formatted_welcome = self._formatted_welcome

    def say_welcome(self):
        self.logger.info(f'{Ansi.TAB}Displaying logo and welcome message.')
        print(self.formatted_welcome)

    @property
    def formatted_welcome(self):
        return self._formatted_welcome

    @formatted_welcome.setter
    def formatted_welcome(self, value):
        self.logger.info(f'{Ansi.TAB}Preparing logo and welcome message.')
        self._formatted_welcome = (
            f'{Ansi.BOLD}\033[38;5;208m{self.formatted_logo}\033[0;00m\n'
            f'{Ansi.HEADER}Welcome to {NAME} version {VERSION}.{Ansi.ENDC}\n'
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
        self.modules_dict = []
        self.module_dir = MODULES_DIR
        self.prompt = (
            f'\n{Ansi.TAB * 2}Enter modules directory to try again:'
            f'\n{Ansi.TAB}   >'
        )
        self.module_list = []

    def modules_checker(self):
        """Looks for modules."""
        self.logger.info(f'Starting {inspect.currentframe().f_code.co_name}')
        self.logger.info(f'{Ansi.TAB}Looking for modules in {self.module_dir}.')

        print(f'{Ansi.TAB}1.  Looking for modules in \'{Ansi.PATH}/{self.module_dir}{Ansi.ENDC}\'...')
        self.lookfor_directory()
        self.lookfor_modules()

    def modules_importer(self):
        """Import modules."""
        self.logger.info(f'Starting {inspect.currentframe().f_code.co_name}')
        self.logger.info(f'{Ansi.TAB}Preparing to import modules from {self.module_dir}.')

        print(f'{Ansi.TAB}2.  Importing modules from \'{Ansi.PATH}/{self.module_dir}{Ansi.ENDC}\'...')

        for module in self.module_list:
            self.modules_dict.append(
                {
                    'module': module,
                    'name': module.name,
                    'path': module,
                    'import': 'False',
                    'tested': 'False',
                    'f_name': f'{Ansi.DIM}{module.name}{Ansi.ENDC}',
                    'f_import': f'{Ansi.DIM}False{Ansi.ENDC}',
                    'f_tested': f'{Ansi.DIM}False{Ansi.ENDC}',
                }
            )
        self.import_ui()

        for module in self.modules_dict:
            self.import_module(module)
            self.import_ui()
        print(f'{Ansi.DOWN * (len(self.modules_dict) + 1)}')

    def path_error(self):
        """Returns path error with directory name."""
        return (
            f'{Ansi.TAB * 2}{Ansi.FAIL}ERROR: \'{Ansi.PATH}/{self.module_dir}{Ansi.FAIL}\' '
        )

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
                self.logger.error(f'{Ansi.TAB * 2}Error: Directory not found.', extra={"Type": "❗"})
                print(f'{self.path_error()} {error_type}{Ansi.ENDC}.')
                self.module_dir = Path(input(self.prompt))
                print()

    def lookfor_modules(self):
        while True:
            try:
                self.module_list = list(self.module_dir.glob('*.py'))
                if not len(self.module_list) > 0:
                    self.logger.error(f'{Ansi.TAB * 2}Error: Directory empty.', extra={"Type": "❗"})
                    raise Exception("Directory empty.")
                self.logger.info(f'{Ansi.TAB * 2}{len(self.module_list)} module(s) found.')
                print(f'{Ansi.TAB * 2}{Ansi.SCSS}{len(self.module_list)} module(s) found{Ansi.ENDC}.\n')
                break
            except:
                error_type = 'directory is empty'
                print(f'{self.path_error()} {error_type}{Ansi.ENDC}.')
                self.module_dir = Path(input(self.prompt))
                print()

    def import_ui(self):
        print(f'{Ansi.TAB * 3}{"module name":32} {"imported?":10} {"tested?":10}')
        for module in self.modules_dict:
            print(
                f'{Ansi.CLINE}{Ansi.TAB * 3}'
                f"{module['f_name']:40} {module['f_import']:18} {module['f_tested']:10}"
                f'{Ansi.ENDC}'
            )
        print(f'{Ansi.UP * (len(self.modules_dict) + 2)}')

    def import_module(self, module):
        """This uses some dirty workarounds to load modules dynamically.
        1. Gets the name without file extension. hello_world.py -> hello_world
        2. Imports the module as 'mod'.
        3. Executes the module.
        4. Links 'mod' with a global var named after the 'name' variable.
        5. Marks the module as correctly imported :)"""
        try:
            name = module["name"].split('.', 1)[0]
            spec = importlib.util.spec_from_file_location("module.name", os.path.realpath(module["path"]))
            mod = importlib.util.module_from_spec(spec)
            sys.modules["module.name"] = mod
            spec.loader.exec_module(mod)
            globals()['%s' % name] = mod
            module["import"] = "True"
            module['f_name'] = f'{Ansi.ENDC}{module["name"]}{Ansi.ENDC}'
            module['f_import'] = f'{Ansi.ENDC} ✓ {Ansi.ENDC}'
        except:
            pass

        # module['f_tested'] = f'{Ansi.ENDC} ✓ {Ansi.ENDC}'


def main():
    """Main function. Initializes program."""
    global LOGGER
    LOGGER = CustomLogger("logger")
    program = StartProgram()
    print()


if __name__ == '__main__':
    main()
