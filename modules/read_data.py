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
    """
        Affiche 'Hello World!' à la console.
        """
    print('Hello World!')


def read_data(file, **kwargs):
    """
    Lit le contenu d'un fichier spécifié et retourne son contenu en tant que chaîne de caractères.

    Args:
        file (str): Le nom du fichier (ex. 'test.txt').
        **kwargs: Arguments supplémentaires optionnels :
            - 'path' (str) : Chemin à partir du répertoire parent pour les fichiers non présents dans le même répertoire que read_data.
                             Ex. ('/EMODIA/data/movie_dialog')
            - 'file_in_zip' (str) : Nom du fichier à extraire du zip si (file) est un fichier zippé.
            - 'logger' (logging.Logger) : Logger, non implémenté actuellement : à ignorer.
            - 'tab' (str) : Non implémenté actuellement : à ignorer.

    Returns:
        str: Contenu du fichier ou du fichier à l'intérieur du zip sous forme de chaîne de caractères.

    Raises:
        FileNotFoundError: Si le fichier spécifié n'existe pas.
        NotADirectoryError: Si le chemin spécifié n'est pas un répertoire.
        PermissionError: Si le fichier existe mais les permissions sont insuffisantes.
    """
    try:
        path = PurePath.joinpath(kwargs.get('path'), file)
    # Si l'utilisateurice n'a pas spécifié de chemin d'accès, utiliser 'file' comme chemin d'accès.
    except KeyError:
        path = file

    # print(path)
    if not isinstance(path, Path):
        print(f'not path :({chr(10)}')
        path = Path(path)  # Si pas Path(), le faire.
        # print(path)

    # Définition des valeurs par défaut si elles ne sont pas fournies lors de l'appel à read_data()
    tab = kwargs.get('tab') or '    '
    logger = kwargs.get('logger') or None

    error = f'{tab * 2}ERROR: '

    #logger_handler(logger, f'{tab * 3}Accessing {path.name}...')  # Logging using logger_handler
    if '.zip' in path.name:  # Est-ce que c'est un zip?
        #print('its a zip!')
        if not kwargs["file_in_zip"]:  # Si pas dans le zip: erreur.
            print(f'Please select a zip file.{chr(10)}')
            return
        file_in_zip = kwargs['file_in_zip']  # Sinon, obtenir ce qui a été demandé
        #print(file_in_zip)
        #print(f'{tab * 2}Accessing {file_in_zip}..')
        try:
            #zip = zipfile.ZipFile(path)
            #print(zip.namelist())
            with zipfile.ZipFile(path, 'r') as my_zip:  # Utilisation de ZipFile pour accéder au contenu d'un fichier.
                # Notez l'utilisation de zipfile.Path() pour accéder aux données sous forme de chaîne de caractères et non d'octets.
                data = zipfile.Path(my_zip, file_in_zip)
                # Nous spécifions le type d'encodage pour nous assurer que Windows n'essaie pas de le lire de manière erronée.
                zipped_data = data.read_text(encoding='utf-8')
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
            with path.open('r') as file:  # Accès de base aux fichiers.
                data = file.read()
                return data
        except FileNotFoundError or NotADirectoryError:
            #logger_handler(logger, f'{tab * 2}Error accessing {path.name}')
            print(f'{error}Path does not exist.{chr(10)}')
        except PermissionError:
            print(f'{error}File exists but permission error.{chr(10)}')


def logger_handler(logger, msg):
    """
    Utilise le logger pour enregistrer un message si un logger est fourni.

    Args:
        logger (logging.Logger): Logger pour enregistrer les messages.
        msg (str): Message à enregistrer.

    """
    try:
        logger.info(msg)
    except:
        pass
