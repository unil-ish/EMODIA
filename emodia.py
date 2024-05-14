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
import logging  # For custom logs.
import json
import inspect  # To get function names in logs.
import importlib.util  # To import modules.

# Note that any module imported through the program's module importer function will behave as if
# added through the standard 'import module' formula.

# PROGRAM INFO
NAME = 'EMODIA'
VERSION: float = 0.1
MODULES_DIR = Path('modules')  # Directory where each 'module'.py is stored.
RESOURCES_DIR = Path('resources')  # Directory for resources such as authors, logo, etc.

# We use a global to store the custom logger.
# There can only be one object per log file, and we want every log in a single file -> a single, shared logger object.
LOGGER = object  # Any function can call this logger through the global.


class Ansi:
    """This class is used for formatting purposes.
    * It uses ANSI escape codes that have an impact on formatting when output to a console or terminal.
    * These codes can be entered in any string, typically by using a fstring such as:
        f'{Ansi.TAB}{Ansi.BR_GRE}This message will be printed in green!{Ansi.ENDC}'
    * It also implements an {Ansi.TAB} variable to ensure indents are consistent throughout the program."""
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
    Overrides the makeRecord function to allow for optional Type arg in logs.
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


class MainProgram(ABCProgram):
    """The main program, as a class.
        * Handles startup messages
        * Manages and imports modules
        * Gets user input as to what to do next."""

    def __init__(self):
        """Program initializer: setup logs and variables, then welcomes user."""
        super().__init__()
        self.logger.info('Starting Program.', extra={"Type": "✅"})

        # Prints welcome message.
        welcome = ProgramInfo()
        welcome.say_welcome()

        self.logger.info(f'Calling start_program().')
        self.start_program()

    def start_program(self):
        """Starts main program:
        * Gets the modules
        * Once done, calls the function handling user commands."""
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

        self.command_loop()

    def command_loop(self):
        print('Hi! We\'re all good, what would you like to do now?')


class ProgramInfo(ABCProgram):
    """Handles welcome message.
    * Stores some variables within ProgramInfo for easy access if any modules ends up needing them. It's nicer
        to only do the file opening and content formatting once and be able to recall it at will instead of redoing
        it every time someone may want to see the credits (which is hopefully often :)).
    * Gathers the data from files located in RESOURCES_DIR, extracts it and formats it.
    * Instances have the following properties:
        - authors: list of dicts containing author data.
        - formatted_authors: formatted author data, ready for printing.
        - formatted_logo: formatted logo, ready for printing.
        - formatted_welcome: formatted welcome message with logo and authors, ready for printing.
    """

    def __init__(self):
        super().__init__()  # Getting inheritance.

        self.logger.info(f'{Ansi.TAB}Gathering author information...', extra={"Type": "🚚"})
        self.authors = "authors"  # str is the name of the json file holding author data.
        self.formatted_authors = self.authors  # provides the contents of the files to the formatter
        self.logger.info(f'{Ansi.TAB * 2}Gathered author information.')

        self.logger.info(f'{Ansi.TAB}Gathering logo ASCII art...', extra={"Type": "🚚"})
        self._formatted_logo = "logo"  # str is the name of the file holding logo data.
        self.formatted_logo = self._formatted_logo  # provides the contents of the files to the formatter
        self.logger.info(f'{Ansi.TAB * 2}Gathered logo ASCII art.')

    def say_welcome(self):
        """Function that prints out the formatted welcome message while making a log entry."""
        self.logger.info(f'{Ansi.TAB}Displaying logo and welcome message.')
        print(self.formatted_welcome)

    @property
    def formatted_welcome(self):
        """Prepares a formatted welcome message. 'value' is a placeholder."""
        self.logger.info(f'{Ansi.TAB}Preparing logo and welcome message.')
        return (
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
        """Gets the raw data from the file at 'value'.
            However, this data isn't sorted. As dictionaries can't be sorted, we create a new dictionary and fill it
            with data returned by the sort.dict() function, using the "name" key as key to be sorted alphabetically.
            sort.dict() takes care of the sorting."""
        self._authors = {}
        raw_authors: dict = self.get_resources(value, "json")  # Gets the raw json content.
        for key in raw_authors.keys():  # Each key being an entry like "authors", "supervisors", etc.
            self._authors.update(  # Add to dictionary
                {
                    key:
                        self.sort_dict(  # Returns a sorted dict
                            raw_authors[key],  # Uses the key from raw_authors as key for the new dict.
                            "name"  # And sort using the "name" key from raw_authors.
                        )
                }
            )

    @property
    def formatted_authors(self):
        return self._formatted_authors

    @formatted_authors.setter
    def formatted_authors(self, authors):
        """Formats authors data to be used in the welcome message."""
        self._formatted_authors = []
        for type_key in authors:  # type_key being something like "authors", "supervisors", etc.
            self._formatted_authors.append(
                chr(10).join(
                    f'{Ansi.TAB * 2}{key["name"] + " " + key["surname"]:22}  {key["institution"]}'
                    for key in authors[type_key]  # Iterates through each dict within authors.
                )
            )

    @property
    def formatted_logo(self):
        return self._formatted_logo

    @formatted_logo.setter
    def formatted_logo(self, value):
        """Formats the logo by getting the resource from LOGO_DIR, then wrapping each line with formatting."""
        logo = self.get_resources(value, "txt")
        self._formatted_logo = f'\n{chr(10).join(f"{Ansi.LOGO_LINE}{line}" for line in logo.splitlines())}\n'

    @classmethod
    def sort_dict(cls, to_sort: dict, key: str):
        """Short function to sort dicts.
        As dicts can't be sorted, we create a list of dictionaries sorted by the 'key' key."""
        return sorted(to_sort, key=lambda d: d[key])

    @classmethod
    def get_resources(cls, resource, data_type):
        """Returns data from a specified resource within the RESOURCES_DIR. Handles both json and txt."""
        with open(Path(f'{RESOURCES_DIR}/{resource}.{data_type}'), 'r') as file:
            if data_type == 'json':
                data = json.load(file)  # Using json loader for json files.
            else:
                data = file.read()  # Using normal file loader for text files.
            return data


class ModulesHandler(ABCProgram):
    """Handles modules:
        * modules_checker provides text feedback to the user while looking first for the dir, then the modules
        * lookfor_directory() checks if the MODULES_DIR exists and provides options to fix an erroneous path.
        * lookfor_modules() looks for modules within the dir, providing options to fix an erroneous path."""

    def __init__(self):
        super().__init__()  # Get the inheritance.
        self.module_list = []  # Simple list of modules used by the look functions.
        self.modules_dict = []  # Will become our list of modules as dicts for import.
        self.module_dir = MODULES_DIR
        self.prompt = (  # Prompt used by our functions if there's a path error.
            f'\n{Ansi.TAB * 2}Enter modules directory to try again:'
            f'\n{Ansi.TAB}   >'  # Here's where the user will be able to type
        )

    def modules_checker(self):
        """Looks for modules within a directory, first checking if the dir is valid then the modules.
        We're not putting that in the __init__ because it's doing a lot, and we don't want it accidentally called."""
        self.logger.info(f'Starting {inspect.currentframe().f_code.co_name}')  # The {code} returns: function name.
        self.logger.info(f'{Ansi.TAB}Looking for modules in {self.module_dir}.')

        print(f'{Ansi.TAB}1.  Looking for modules in \'{Ansi.PATH}/{self.module_dir}{Ansi.ENDC}\'...')
        self.lookfor_directory()  # Delegates the directory checking to a dedicated function.
        self.lookfor_modules()  # Same for the modules listing.

    def modules_importer(self):
        """Import modules."""
        self.logger.info(f'Starting {inspect.currentframe().f_code.co_name}')  # The {code} returns: function name.
        self.logger.info(f'{Ansi.TAB}Importing from dir: {self.module_dir}.')

        print(f'{Ansi.TAB}2.  Importing modules from \'{Ansi.PATH}/{self.module_dir}{Ansi.ENDC}\'...')

        for module in self.module_list:  # Using the list of modules to create a list of 1 dict = 1 module.
            self.logger.info(f'{Ansi.TAB * 2}Getting {module.name}')
            self.modules_dict.append(
                {
                    'module': module,  # Module's full name.
                    'name': module.name,  # Its name with file extension.
                    'path': module,  # Module's import path.
                    'import': 'False',  # Has the module been imported? At this point, not yet.
                    'f_name': f'{Ansi.DIM}{module.name}{Ansi.ENDC}',  # Print-friendly name, dimmed for now.
                    'f_import': f'{Ansi.DIM} ✗ {Ansi.ENDC}',  # Print-friendly status, dimmed as well.
                }
            )
            self.logger.info(f'{Ansi.TAB * 3}Module obtained.', extra={"Type": "📦"})
        self.import_ui()  # Gets a first UI up with the before-import variables.

        self.logger.info(f'{Ansi.TAB}All modules registered. Ready to import.')
        for module in self.modules_dict:  # And now import the modules, updating the ui with each one.
            self.logger.info(f'{Ansi.TAB * 2}Importing {module["name"]}.')
            self.import_module(module)  # We're passing the full dict entry to the importer so it can update it.
            self.import_ui()
        print(f'{Ansi.DOWN * (len(self.modules_dict) + 1)}')  # Moving the cursor down when done.

    def path_error(self):
        """Returns path error with directory name."""
        return (
            f'{Ansi.TAB * 2}{Ansi.FAIL}ERROR: \'{Ansi.PATH}/{self.module_dir}{Ansi.FAIL}\' '
        )

    def lookfor_directory(self):
        """Looks for the modules directory, with logs and user prompt if directory issue.
        TODO: Shares a lot of code with lookfor_modules(), may want to refactor these functions."""
        while True:  # Try until suitable directory is found.
            try:
                if not self.module_dir.exists():  # Does it exist?
                    raise FileExistsError('directory not found')  # Raise error if not.
                self.logger.info(f'{Ansi.TAB * 2}Directory found.')
                print(f'{Ansi.TAB * 2}{Ansi.SCSS}Directory found{Ansi.ENDC}.')
                break  # Breaks out of the loop once suitable directory is found so we can move to the next step.
            except:  # If there's anything wrong with the directory, warn the user and ask for new directory.
                error_type = 'directory not found'
                self.logger.error(f'{Ansi.TAB * 2}Error: Directory not found.', extra={"Type": "❗"})
                print(f'{self.path_error()} {error_type}{Ansi.ENDC}.')
                self.module_dir = Path(input(self.prompt))  # Update module_dir based on user input.
                print()

    def lookfor_modules(self):
        """Looks for module within the modules directory, with logs and user prompt if content issue."""
        while True:  # Try until modules are found.
            try:
                self.module_list = list(self.module_dir.glob('*.py'))  # Can we get a list of modules in the directory?
                if not len(self.module_list) > 0:  # If the list is empty, raise exception and log it.
                    self.logger.error(f'{Ansi.TAB * 2}Error: Directory empty.', extra={"Type": "❗"})
                    raise Exception("Directory empty.")
                self.logger.info(f'{Ansi.TAB * 2}{len(self.module_list)} module(s) found.')
                print(f'{Ansi.TAB * 2}{Ansi.SCSS}{len(self.module_list)} module(s) found{Ansi.ENDC}.\n')
                break  # If we've got our modules, we can break out and go back.
            except:  # If there's an exception, warn the user and ask them for another directory.
                error_type = 'directory is empty'
                print(f'{self.path_error()} {error_type}{Ansi.ENDC}.')
                self.module_dir = Path(input(self.prompt))  # Update module_dir based on user input.
                print()

    def import_ui(self):
        """Prints a fancy report for modules, and updates it whenever called by writing over old lines."""
        print(f'{Ansi.TAB * 3}{"module name":32} {"imported?":10}')  # Prints headers.
        for module in self.modules_dict:
            print(
                f'{Ansi.CLINE}{Ansi.TAB * 3}'  # Important to CLINE, otherwise text may overlap on update.
                f"{module['f_name']:40} {module['f_import']:18}"
                f'{Ansi.ENDC}'
            )
        print(f'{Ansi.UP * (len(self.modules_dict) + 2)}')  # Moves cursor up with ANSI codes to prepare refresh.

    @staticmethod
    def import_module(module):
        """This uses some dirty workarounds to load modules dynamically.
        1. Gets the name without file extension. hello_world.py -> hello_world
        2. Imports the module as 'mod'.
        3. Executes the module.
        4. Links 'mod' with a global var named after the 'name' variable.
        5. Marks the module as correctly imported :)"""
        try:
            name = module["name"].split('.', 1)[0]  # Removes file extension from file name.
            spec = importlib.util.spec_from_file_location("module.name", os.path.realpath(module["path"]))
            mod = importlib.util.module_from_spec(spec)  # Import mod using the 'spec' spec. See importlib.
            sys.modules["module.name"] = mod  # Add module reference to the list of modules.
            spec.loader.exec_module(mod)  # Executes module to finish import
            globals()['%s' % name] = mod  # Makes the variable global to allow normal module behavior.
            module["import"] = "True"  # Updates module dict to confirm import.
            module['f_name'] = f'{Ansi.ENDC}{module["name"]}{Ansi.ENDC}'  # Updates module dict with formatted name.
            module['f_import'] = f'{Ansi.ENDC} ✓ {Ansi.ENDC}'  # Updates module dict with formatted import status.
            LOGGER.info(f'{Ansi.TAB * 3}Imported {module["name"]}.', extra={"Type": "🧩"})
        except:
            LOGGER.error(f'{Ansi.TAB * 3}Import failed.', extra={"Type": "❗"})


def main():
    """Main function. Initializes program."""
    global LOGGER  # We need the logger to be shared.
    LOGGER = CustomLogger("logger")
    program = MainProgram()
    print()


if __name__ == '__main__':
    main()
