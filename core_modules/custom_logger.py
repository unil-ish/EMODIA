import logging
import inspect


class CustomLogger(logging.Logger):
    """Classe logger personnalisée.
    Ignore la fonction makeRecord pour permettre l'utilisation d'un Type arg optionnel dans les logs.
    Dans notre cas, nous l'utilisons pour ajouter des émojis à la fin des messages pour faciliter l'utilisation humaine.
     Les méthodes suivantes peuvent être utilisées, 'extra' étant facultatif :
    * .info(str, extra={"Type":str})
    * .warning(str, extra={"Type":str})
    * .error(str, extra={"Type":str})
    """

    def __init__(self, name: str, log_name=''):
        """
        Initinlisation d'un logger personnalisé en tant que child de la class logger python par défaut.
        A un format de message personnalisé avec un champ 'Type' supplémentaire.
        Les logs sont sauvegardés dans un seul fichier, nommé d'après le nom du programme.

        Args:
            name (str): Nom du logger
            log_name (str): Nom du fichier log, vide par défaut
        """
        super().__init__(name)
        self.propagate = False

        # Format personnalisé ajoutant un champt 'Type' supplémentaires et supprimant les millisecondes.
        formatter = logging.Formatter(
            fmt="%(asctime)-19s | %(levelname)-7s | %(message)-50s | %(Type)s ",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        # Nom le fichier log d'après le nom du programme
        handler = logging.FileHandler(
            filename=f"{log_name}.log", mode="w", encoding="utf-8"
        )

        # Recherche tout message d'avertissement  >= to INFO.
        handler.setLevel("INFO")
        handler.setFormatter(formatter)

        # Utilise notre gestionnaire personnalisé comme gestionnaire de sortie -> outputs to file.
        self.addHandler(handler)

        self.info("Custom logger initialized. Hi!", extra={"Type": "📝"})

    def makeRecord(self, *args, **kwargs):
        """
        Ignore la méthode makeRecord du logger pour rendre les arguments supplémentaires optionnels.
        makeRecord est appelée à chaque fois que nous faisons logger.info(), warn(), ou toute autre fonction de message du logger.
        Cet argument supplémentaire doit être ajouté sous la forme extra={« Type » : string}.

        Args:
            *args: Arguments positionnels pour makeRecord
            **kwargs: Arguments nommés pour makeRecord
        """
        rv = super(CustomLogger, self).makeRecord(*args, **kwargs)
        rv.__dict__["Type"] = rv.__dict__.get("Type", "  ")
        return rv

    def log_call(self):
        """Produit une entrée de log entry avec le nom de la fonction appelante."""
        self.info("Calling: " + inspect.currentframe().f_back.f_code.co_name)
