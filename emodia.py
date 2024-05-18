"""EMODIA: ÉMotions et DIalogues Analyse
L'objectif principal de ce projet est d'explorer et de quantifier la manière dont les émotions se développent et
 interagissent dans les dialogues des films, en utilisant une approche innovante inspirée des équations de
 Navier-Stokes. Le modèle vise à offrir une nouvelle lentille à travers laquelle examiner les dynamiques émotionnelles
 entre les personnages, permettant une compréhension plus profonde des stratégies narratives et des relations
 interpersonnelles au sein des films.
"""
import importlib.util  # To import modules.
import os
import sys
from pathlib import Path

import inspect  # To get function names in logs.
import json
import logging  # For custom logs.

# Note that any module imported through the program's module importer function will behave as if
# added through the standard 'import module' formula.

# PROGRAM INFO
NAME = 'EMODIA'
MODULES_DIR = Path('modules')
RESOURCES_DIR = Path('resources')

# Utilities
MODULE_IMPORT = bool  # Whether modules have been imported or not, as they must be imported only once.
TAB = '    '  # Defines text indent.

# We use a global to store the custom logger.
# There can only be one object per log file, and we want every log in a single file -> a single, shared logger object.
LOGGER = object


class Utils:
    """Utilities."""

    @staticmethod
    def get_resource(name, data_type):
        """Opens 'name'.'data_type' with either default read() or json.load(), returns contents."""
        with open(Path(f'{RESOURCES_DIR}/{name}.{data_type}'), 'r') as file:
            if data_type == 'json':
                return json.load(file)
            else:
                return file.read()

    @staticmethod
    def sort_dict(to_sort: dict, key: str):
        """Short function to sort dicts.
        As dicts can't be sorted, we create a list of dictionaries sorted by the 'key' key."""
        return sorted(to_sort, key=lambda d: d[key])


class Message:
    """Stores messages imported from messages.json."""
    styles = dict
    messages = dict

    @classmethod
    def set_msg_dict(cls):
        """Grabs messages from messages.json and stores them in messages dict."""
        cls.messages = {}
        cls.messages = Utils.get_resource('messages', 'json')

    @classmethod
    def set_styles_dict(cls):
        """Grabs styles from styles.json and stores them in styles dict after adding ANSI escape code in front."""
        cls.styles = None
        cls.styles = Utils.get_resource('styles', 'json')

        for key in cls.styles:
            cls.styles[key] = '\033[' + cls.styles[key]  # That's our ANSI escape code.
        cls.styles.update({'tab': TAB})

    @classmethod
    def get_msg(cls, msg_key):
        """Returns contents of message at msg_key within the messages dict."""
        return str(cls.messages[msg_key])

    @staticmethod
    def say(msg_key, **kwargs):
        """Takes in a message key and **kwargs, prints message at msg_key with vars replaced by **kwargs."""
        style_and_kwargs: dict = {**Message.styles, **kwargs}  # Fuses styles and kwargs for .format()
        print(Message.get_msg(msg_key).format(**style_and_kwargs))


class CustomLogger(logging.Logger):
    """A custom logger class.
    Overrides the makeRecord function to allow for optional Type arg in logs.
    In our case, we use it to add emojis at the end of log messages for easier human parsing.
    The following methods can be used, with 'extra' being optional:
    * .info(str, extra={"Type":str})
    * .warning(str, extra={"Type":str})
    * .error(str, extra={"Type":str})
    """

    def __init__(self, name: str):
        """Initializes a custom logger as child of default python logger class.
        Has a custom log message format with additional 'Type' field.
        The logs are saved in a single file, named after the program's name."""
        super().__init__(name)
        self.propagate = False

        # Using a custom format to have (1) an extra 'Type' field and (2) not have milliseconds.
        formatter = logging.Formatter(
            fmt='%(asctime)-19s | %(levelname)-7s | %(message)-50s | %(Type)s ',
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        # Names the log file after the program's name.
        handler = logging.FileHandler(
            filename=f'{os.path.splitext(__file__)[0]}.log', mode='w', encoding='utf-8'
        )

        # Tells our logger to look for any message of severity higher or equal to INFO.
        handler.setLevel("INFO")
        handler.setFormatter(formatter)

        # Tells the logger to use our custom handler as output handler -> outputs to file.
        self.addHandler(handler)

        self.info('Custom logger initialized. Hi!', extra={"Type": '📝'})

    def makeRecord(self, *args, **kwargs):
        """Overrides the logger's makeRecord method to make extra arguments optional.
        makeRecord is called whenever we do logger.info(), warn(), or any other logger message function.
        This extra argument must be added as extra={"Type": string}.
        """
        rv = super(CustomLogger, self).makeRecord(*args, **kwargs)
        rv.__dict__["Type"] = rv.__dict__.get("Type", "  ")
        return rv


class ABCProgram:
    """Parent class for all modules. Allows them to share a single, custom logger and makes them print
    a log message with their name when they are initialized.
    """

    def __init__(self):
        # Ensure children share the logger.
        self.logger = LOGGER

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
        self.modules_handler = None

    def start_program(self):
        # Setting up message handler.
        Message.set_msg_dict()
        Message.set_styles_dict()
        welcome = ProgramInfo()

        welcome.print_logo()

        # Looking for, then importing modules.
        self.modules_handler = ModulesHandler()
        self.modules_handler.look_for_modules()
        self.modules_handler.modules_importer()


class ProgramInfo(ABCProgram):
    """Gets logo and author information from resources, formats and displays them."""

    def __init__(self):
        super().__init__()
        self.logo = Utils.get_resource('logo', 'txt')
        self.authors: dict = Utils.get_resource('authors', 'json')

    def print_logo(self):
        """Print logo."""
        for line in self.logo.splitlines():
            Message.say('logo', text=line)
        print()

    def print_authors(self):
        """Gets authors, sorts them under each category then formats and prints them."""
        for key in self.authors.keys():  # Each key being an entry like "authors", "supervisors", etc.
            self.authors.update(
                {
                    # Sorts authors by name under a 'key' category.
                    key: Utils.sort_dict(self.authors[key], "name")
                }
            )

        # Print out all that formatted data.
        for category in self.authors.keys():
            Message.say(category)
            for person in self.authors[category]:
                Message.say('person_list', fullname=person["name"] + ' ' + person["surname"],
                            institution=person["institution"])
            print()


class ModulesHandler(ABCProgram):
    """Finds and imports modules."""

    def __init__(self):
        super().__init__()
        self.module_list = []  # Simple list of modules used by the look functions.
        self.modules_dict = []  # Will become our list of modules as dicts for import.
        self.module_dir = MODULES_DIR

        # Prompt used by our functions if there's a path error.
        self.prompt = (
            f'\n{TAB * 2}Enter modules directory to try again:'
            f'\n{TAB}   >'
        )

    def look_for_modules(self):
        """Looks for modules within a directory, first checking if the dir is valid then the modules.
        We're not putting that in the __init__ because it's doing a lot, and we don't want it accidentally called.
        """
        self.logger.info(f'Starting {inspect.currentframe().f_code.co_name}')  # The {code} returns: function name.
        self.logger.info(f'{TAB}Looking for modules in {self.module_dir}.')
        Message.say('1', name=NAME)
        Message.say('looking_for_modules', path=self.module_dir)

        while True:
            try:
                if self.module_dir.exists() and self.module_dir.is_dir():
                    Message.say('directory_found')
                else:
                    self.logger.error(f'{TAB * 2}Error: Directory not found.', extra={"Type": "❗"})
                    Message.say('directory_not_found')
                    raise NotADirectoryError

                self.module_list = list(self.module_dir.glob('*.py'))
                module_number = len(self.module_list)
                if module_number > 0:
                    self.logger.info(f'{TAB}{module_number} module(s) found.')
                    Message.say('modules_found', number=module_number)
                    print()
                    break
                else:
                    self.logger.error(f'{TAB * 2}Error: Directory empty.', extra={"Type": "❗"})
                    Message.say('modules_not_found')
                    raise FileNotFoundError

            except NotADirectoryError or FileNotFoundError:
                self.module_dir = Path(input(self.prompt))

    def modules_importer(self):
        """Import modules."""
        global MODULE_IMPORT

        self.logger.info(f'Starting {inspect.currentframe().f_code.co_name}')  # The {code} returns: function name.
        self.logger.info(f'{TAB}Importing from dir: {self.module_dir}.')
        Message.say('importing_modules', path=self.module_dir)

        # We're checking if modules have already been imported. If yes, skip.
        if MODULE_IMPORT:
            self.logger.info(f'{TAB * 2}Modules already imported. Skipping')
            print(f'{TAB * 2}Modules already imported. Skipping.')
            return
        # Else, mark that we're importing them and not to import again.
        MODULE_IMPORT = True

        # Using the list of modules to create a list of 1 dict = 1 module.
        for module in self.module_list:
            self.logger.info(f'{TAB * 2}Getting {module.name}')
            self.modules_dict.append(
                {
                    'module': module,  # Module's full name.
                    'name': module.name,  # Its name with file extension.
                    'path': module,  # Module's import path.
                    'f_name': f'{module.name}',  # Print-friendly name.
                    'f_import': f'✗',  # Print-friendly status.
                }
            )
            self.logger.info(f'{TAB * 3}Module obtained.', extra={"Type": "📦"})

        # Gets a first UI up with the before-import variables.
        self.module_import_ui()

        self.logger.info(f'{TAB}All modules registered. Ready to import.')
        for module in self.modules_dict:
            self.logger.info(f'{TAB * 2}Importing {module["name"]}.')
            # We're passing the full dict entry to the importer so it can update it.
            self.import_module(module)
            self.module_import_ui()
        # Moving the cursor down when done.
        print(f'{(len(self.modules_dict) + 1) * str(Message.styles["cursor_down"])}')

    def module_import_ui(self):
        """Prints a fancy report for modules, and updates it whenever called by writing over old lines."""
        for module in self.modules_dict:
            Message.say('module_ui', import_status=module['f_import'], module_name=module['f_name'])

        # Moves cursor up with ANSI codes to prepare refresh.
        print(f'{(len(self.modules_dict) + 1) * str(Message.styles["cursor_up"])}')

    @staticmethod
    def import_module(module):
        """This uses some dirty workarounds to load modules dynamically.
        1. Gets the name without file extension. hello_world.py -> hello_world
        2. Imports the module as 'mod'.
        3. Executes the module.
        4. Links 'mod' with a global var named after the 'name' variable.
        5. Marks the module as correctly imported :)"""
        try:
            # Removes file extension from file name.
            name = module["name"].split('.', 1)[0]

            # Import mod using the 'spec' spec. See importlib.
            spec = importlib.util.spec_from_file_location("module.name", os.path.realpath(module["path"]))
            mod = importlib.util.module_from_spec(spec)

            # Add module reference to the list of modules.
            sys.modules["module.name"] = mod

            # Executes module to finish import.
            spec.loader.exec_module(mod)

            # Makes the variable global to allow normal module behavior.
            globals()['%s' % name] = mod
            # Updates module dict with formatted name.
            module['f_name'] = f'{module["name"]}'
            # Updates module dict with formatted import status.
            module['f_import'] = f'✓'

            LOGGER.info(f'{TAB * 3}Imported {module["name"]}.', extra={"Type": "🧩"})

        except ModuleNotFoundError:
            LOGGER.error(f'{TAB * 3}Import failed.', extra={"Type": "❗"})


def main():
    """Main function. Initializes program."""
    global LOGGER, MODULE_IMPORT  # We need the logger and module import status to be shared.
    LOGGER = CustomLogger("logger")  # Here's our shared, custom logger.
    MODULE_IMPORT = False  # No modules imported yet. Yet >:)

    LOGGER.info('Starting Program.', extra={"Type": "✅"})
    program = MainProgram()
    program.start_program()


if __name__ == '__main__':
    main()
