import sys
import time
import importlib


class ModuleHandler:
    """Vérifie que les modules ont été importés correctement."""

    def __init__(self, logger, messenger, module_list, module_dir):
        """
        Initialise la classe ModuleHandler avec le logger, le messenger, la liste des modules et le répertoire des modules.

        Args:
            logger (logging.Logger): Logger pour enregistrer les messages.
            messenger (Messenger): Instance de Messenger pour l'impression et le log des messages.
            module_list (list): Liste simple des modules utilisés par les fonctions de vérification.
            module_dir (str): Répertoire des modules.
        """
        super().__init__()
        self.logger = logger
        self.module_list = module_list  # Liste simple des modules utilisés par les fonctions de vérification.
        self.modules_dict = []  # Deviendra notre liste de modules sous forme de dictionnaires pour l'import.
        self.module_dir = module_dir
        self.msg = messenger
        self.msg.say("1_modules_check")

    @staticmethod
    def list_imported_modules():
        """
        Liste les modules importés actuellement.

        Returns:
            list: Clés des modules importés.
        """
        return sys.modules.keys()

    def list_modules_from_list(self):
        """
        Affiche l'état de chaque module de la liste des modules.
        """
        for module in self.module_list:
            self.msg.say("module_ui", import_status='✗', name=module)

    def compare_modules_routine(self):
        """
        Routine de comparaison des modules.
        Affiche et enregistre le nombre de modules listés et importés, puis compare les modules listés avec les modules importés.
        """
        self.msg.say('1_1_compare_modules_routine')
        self.msg.log('log_1_1_compare_modules_routine')
        self.imported_modules = self.list_imported_modules()

        self.msg.say('listed_modules_nb', number=f'{len(self.module_list)}')
        self.msg.log('log_listed_modules_nb', number=f'{len(self.module_list)}')
        self.msg.say('imported_modules_nb', number=f'{len(self.imported_modules)}')
        self.msg.log('log_imported_modules_nb', number=f'{len(self.imported_modules)}')

        print()
        self.msg.say('1_2_compare_modules')
        self.msg.log('log_1_2_compare_modules')

        self.list_modules_from_list()
        for i in range(len(self.module_list)):
            self.msg.say('up')
        self.compare_modules()
        self.msg.say('1_module_check_ok')

    def compare_modules(self):
        """
        Compare les modules listés avec les modules importés et affiche/enregistre leur état.
        """
        for module in self.module_list:
            module_path = f'{self.module_dir}.{module}'
            status = '✓' if (module_path in self.imported_modules) else '✗'
            self.msg.log('log_compare_modules_ui', status=status, name=module)
            self.msg.say('compare_modules_ui', status=status, name=module)

    @staticmethod
    def reload_module(module):
        """
        Recharge un module spécifié.

        Args:
            module (module): Module à recharger.

        Returns:
            bool: True si le module a été rechargé avec succès, False sinon.
        """
        try:
            importlib.reload(module)
            return True
        except ModuleNotFoundError:
            return False

    def filtered_list_imported_modules(self):
        """
        Affiche une liste filtrée des modules importés commençant par le répertoire des modules.
        """
        self.msg.say('filtered_list_imported_modules')
        for module in sys.modules.keys():
            location = f'{self.module_dir}.'
            name = module.replace(location, '')
            if module.startswith(location):
                self.msg.say("compare_modules_ui", status='·', name=name)
