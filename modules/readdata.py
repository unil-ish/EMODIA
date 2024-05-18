"""Simple module that takes (1) a Path() or path, (2) a logging.Logger() and (3) optional name of a file within a zip.
If optional name is given, it looks for it (3) within the zipped file provided at (1).
It returns the contents of the file as string."""
import zipfile
from pathlib import Path


def read_data(path, **kwargs):
    """Needs a path or Path(), logging.Logger, left-padding as string in tab, and an optional file name
    to get within the zip.
    Returns contents of Path() / file within zipped Path() as string.
    """

    if not isinstance(path, Path):  # If not Path(), make it so.
        path = Path(path)

    # Setting defaults if not provided when calling read_data()
    if "logger" in kwargs:
        logger = kwargs["logger"]  # Logger provided, we'll use it.
    else:
        logger = None  # We'll handle that in logger_handler().
    if "tab" in kwargs:
        tab = kwargs["tab"]  # Tab provided, let's use it.
    else:
        tab = '    '  # Tab not provided, setting sane default.
    error = f'{tab * 2}ERROR: '

    logger_handler(logger, f'{tab * 3}Accessing {path.name}...')  # Logging using logger_handler
    if '.zip' in path.name:  # Is it a zip?
        if not kwargs["zip_name"]:  # If we're not told what to get inside the zip, error.
            print('Please select a zip file.')
            return
        zip_name = kwargs['zip_name']  # Else, get what was asked
        print(f'{tab * 2}Accessing {zip_name}..')
        try:
            with zipfile.ZipFile(path, 'r') as my_zip:  # Using ZipFile to access file contents.
                with my_zip.open(zip_name) as data:
                    return_data = data.read()
            return return_data
        except:
            print(f'{error}Unzip error.')
            logger_handler(logger, f'{tab * 2}Error unzipping {path.name}')

    else:
        try:
            with path.open('r') as file:  # Basic file access.
                data = file.read()
                return data
        except FileNotFoundError or NotADirectoryError:
            logger_handler(logger, f'{tab * 2}Error accessing {path.name}')
            print(f'{error}Path does not exist.')
        except PermissionError:
            print(f'{error}File exists but permission error.')


def logger_handler(logger, msg):
    """Provide logger if transmitted to main function through kwargs, otherwise disable the function."""
    try:
        logger.info(msg)
    except:
        pass
