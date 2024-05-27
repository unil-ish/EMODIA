from pathlib import Path
from pathlib import PurePath
import json


class Utils:
    """Utilities."""

    @staticmethod
    def get_resource(resource_dir, name, data_type="txt"):
        """
        Ouvre 'name'.'data_type' avec soit la méthode read() par défaut, soit json.load(),
        et retourne le contenu.

        Args:
            resource_dir (str): Répertoire des ressources.
            name (str): Nom du fichier sans extension.
            data_type (str): Type de fichier, par défaut "txt".

        Returns:
            str or dict: Contenu du fichier.
        """
        # TODO: Reformater fullpath, car il est un peu encombrant ainsi.
        # Implémenté pour gérer correctement les chemins sous Windows.
        fullpath = PurePath(resource_dir, (str(name) + '.' + str(data_type)))
        with open(Path(fullpath), "r", encoding='utf-8') as file:
            match data_type:
                case "json":
                    return json.load(file)
                case "txt":
                    return file.read()

    @staticmethod
    def sort_dict(to_sort: dict, key: str):
        """"
        Trie une liste de dictionnaires fournie sous la forme to_sort, en utilisant key.
        Les dictionnaires ne pouvant être triés directement, nous créons une liste
        de dictionnaires triée par la clé 'key'.

        Args:
            to_sort (dict): Liste de dictionnaires à trier.
            key (str): Clé à utiliser pour le tri.

        Returns:
            list: Liste de dictionnaires triée.
        """
        return sorted(to_sort, key=lambda d: d[key])


class SafeDict(dict):
    """
    Dictionnaire sécurisé qui retourne la clé entre accolades si la clé est manquante.
    """
    def __missing__(self, key):
    """
    Retourne la clé entre accolades si elle est manquante dans le dictionnaire.

    Args:
        key (str): Clé manquante.

    Returns:
        str: Clé entre accolades.
    """
        return "{" + key + "}"

