from . import utils


class Messenger:
    """
    Messenger genères des messages prédéfinis formatés en impression et/ou en log.

    L'objectif est la centralisation des messages dans un fichier unique, permettant une standardisation plus facile.

    Il contient des messages importés depuis messages.json dans le répertoire de ressources fourni, et applique des formats provenant de styles.json sur ceux-ci.

    *say('key') Imprime le message stocké à la clé 'key' dans messages.json.
    *log('key', **kwargs) Enregistre dans le log le message stocké à la clé 'key' dans messages.json.
    """

    def __init__(self, resource_dir='', logger=object, tab=str):
        """
        Initialise la classe Messenger avec le répertoire de ressources, un logger et une tabulation.

        Args:
            resource_dir (str): Le répertoire de ressources contenant les fichiers JSON pour les messages et les styles.
            logger (logging.Logger): Logger pour enregistrer les messages.
            tab (str): Caractère de tabulation utilisé dans les styles.
        """
        self.logger = logger
        self.resource_dir = resource_dir
        self.styles = self.set_styles_dict(tab)
        self.messages = self.set_msg_dict()

    def set_msg_dict(self):
        """
        Récupère les messages depuis messages.json et les stocke dans le dictionnaire messages.

        Returns:
            dict: Dictionnaire contenant les messages.
        """
        return utils.Utils.get_resource(self.resource_dir, "messages", "json")

    def set_styles_dict(self, tab):
        """
        Récupère les styles depuis styles.json et les stocke dans le dictionnaire styles après avoir ajouté un code d'échappement ANSI au début.

         Args:
            tab (str): Caractère de tabulation utilisé dans les styles.

        Returns:
            dict: Dictionnaire contenant les styles avec codes d'échappement ANSI.
        """
        styles = utils.Utils.get_resource(self.resource_dir, "styles", "json")

        for key in styles:
            styles[key] = "\033[" + styles[key]  # \033[ -> ANSI
        styles.update({"tab": tab, "new_line": chr(10)})  # Ajout de TAB à nos styles.

        return styles

    def get_message(self, msg_key):
        """
        envoie le contenu du message à la clé msg_key dans le dict de messages.

        Args:
            msg_key (str): Clé du message à récupérer.

        Returns:
            str: Message correspondant à la clé, ou message d'erreur si la clé n'existe pas.
        """
        try:
            msg = str(self.messages[msg_key])
        except KeyError:
            msg = f"ERROR: line {msg_key} not found."
        return msg

    def format_message(self, msg, **kwargs):
        """
        Formate msg en deux fois, en laissant les clés manquantes intactes.
        1. applique self.styles comme format_map.
        2. applique **kwargs à msg comme format_map.

        Args:
            msg (str): Message à formater.
            **kwargs: Variables à insérer dans le message.

        Returns:
            str: Message formaté.
        """
        msg = msg.format_map(utils.SafeDict(self.styles))
        msg = msg.format_map(utils.SafeDict(**kwargs))
        return msg

    def say(self, msg_key, **kwargs):
        """
        Prend en compte une clé de message et **kwargs, imprime le message à msg_key avec vars remplacées par **kwargs et le style.

        Args:
            msg_key (str): Clé du message à imprimer.
            **kwargs: Variables à insérer dans le message.
        """
        msg = self.get_message(msg_key)
        print(self.format_message(msg, **kwargs))

    def log(self, msg_key, level="info", extra="", **kwargs):
        """
        Enregistre dans le log le message à msg_key avec le niveau et les variables fournies.

        Args:
            msg_key (str): Clé du message à enregistrer dans le log.
            level (str): Niveau du log (ex. "info", "error").
            extra (str): Information supplémentaire à ajouter dans le log.
            **kwargs: Variables à insérer dans le message.
        """
        msg = self.get_message(msg_key)
        msg = self.format_message(msg, **kwargs)
        match level:
            case "info":
                self.logger.info(msg, extra={"Type": extra})
            case "error":
                self.logger.error(msg, extra={"Type": '❗'})