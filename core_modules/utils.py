from pathlib import Path
from pathlib import PurePath
import json


class Utils:
    """Utilities."""

    @staticmethod
    def get_resource(resource_dir, name, data_type="txt"):
        """
        Opens 'name'.'data_type' with either default read() or json.load(),
        returns contents.
        """
        # TODO: Reformat fullpath, as it is a bit unwieldy like that.
        # Implemented to handle paths correctly on Windows.
        fullpath = PurePath(resource_dir, (str(name) + '.' + str(data_type)))
        with open(Path(fullpath), "r", encoding='utf-8') as file:
            match data_type:
                case "json":
                    return json.load(file)
                case "txt":
                    return file.read()

    @staticmethod
    def sort_dict(to_sort: dict, key: str):
        """Sorts a list of dicts provided as to_sort, using key.
        As dicts can't be sorted, we create a list of dictionaries
        sorted by the 'key' key.
        """
        return sorted(to_sort, key=lambda d: d[key])


class SafeDict(dict):
    def __missing__(self, key):
        return "{" + key + "}"

