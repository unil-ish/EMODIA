"""
read_data() takes in:
    1. The name of a file (test.txt)
    ** 'path' -> Path from the parent directory for files not in the same directory as read_data.
                  e.g. ('/EMODIA/data/movie_dialog')
    ** 'file_in_zip' -> Name of the file we want from the zip if (1) is a zipped file.
    ** 'logger' -> A logger, not implemented right now: ignore
    ** 'tab' -> not implemented either, ignore.
    Returns contents of Path() / file within zipped Path() as string.
"""
import zipfile
from pathlib import Path
from pathlib import PurePath


def hello_world():
    print('Hello World!')


def read_data(file, **kwargs):
    """
    Takes in:
    1. The name of a file (test.txt)
    ** 'path' -> Path from the parent directory for files not in the same directory as read_data.
                  e.g. ('/EMODIA/data/movie_dialog')
    ** 'file_in_zip' -> Name of the file we want from the zip if (1) is a zipped file.
    ** 'logger' -> A logger, not implemented right now: ignore
    ** 'tab' -> not implemented either, ignore.
    Returns contents of Path() / file within zipped Path() as string.
    """
    try:
        path = PurePath.joinpath(kwargs.get('path'), file)
    # If the user hasn't specified a path, use 'file' as path.
    except KeyError:
        path = file

    # print(path)
    if not isinstance(path, Path):
        print(f'not path :({chr(10)}')
        path = Path(path)  # If not Path(), make it so.
        # print(path)

    # Setting defaults if not provided when calling read_data()
    tab = kwargs.get('tab') or '    '
    logger = kwargs.get('logger') or None

    error = f'{tab * 2}ERROR: '

    #logger_handler(logger, f'{tab * 3}Accessing {path.name}...')  # Logging using logger_handler
    if '.zip' in path.name:  # Is it a zip?
        #print('its a zip!')
        if not kwargs["file_in_zip"]:  # If we're not told what to get inside the zip, error.
            print(f'Please select a zip file.{chr(10)}')
            return
        file_in_zip = kwargs['file_in_zip']  # Else, get what was asked
        #print(file_in_zip)
        #print(f'{tab * 2}Accessing {file_in_zip}..')
        try:
            #zip = zipfile.ZipFile(path)
            #print(zip.namelist())
            with zipfile.ZipFile(path, 'r') as my_zip:  # Using ZipFile to access file contents.
                # Note the use of zipfile.Path() to access data as string and not bytes.
                data = zipfile.Path(my_zip, file_in_zip)
                zipped_data = data.read_text()
                #with my_zip.open(file_in_zip) as data:
                    #zipped_data = data.read_text()
                #print(f'data type: {type(zipped_data)}')
                return_data = zipped_data
            return return_data
        except zipfile.BadZipFile:
            print(f'{error}Unzip error.{chr(10)}')
            #logger_handler(logger, f'{tab * 2}Error unzipping {path.name}')

    else:
        try:
            with path.open('r') as file:  # Basic file access.
                data = file.read()
                return data
        except FileNotFoundError or NotADirectoryError:
            #logger_handler(logger, f'{tab * 2}Error accessing {path.name}')
            print(f'{error}Path does not exist.{chr(10)}')
        except PermissionError:
            print(f'{error}File exists but permission error.{chr(10)}')


def logger_handler(logger, msg):
    """Provide logger if transmitted to main function through kwargs, otherwise disable the function."""
    try:
        logger.info(msg)
    except:
        pass
