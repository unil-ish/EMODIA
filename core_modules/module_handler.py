import sys
import time
import importlib


class ModuleHandler:
    """Checks that modules have been imported correctly."""

    def __init__(self, logger, messenger, module_list, module_dir):
        super().__init__()
        self.logger = logger
        self.module_list = module_list  # Simple list of modules used by the look functions.
        self.modules_dict = []  # Will become our list of modules as dicts for import.
        self.module_dir = module_dir
        self.msg = messenger
        self.msg.say("1_modules_check")

    @staticmethod
    def list_imported_modules():
        return sys.modules.keys()

    def list_modules_from_list(self):
        for module in self.module_list:
            self.msg.say("module_ui", import_status='✗', name=module)

    def compare_modules_routine(self):
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

    def compare_modules(self):
        for module in self.module_list:
            module_path = f'{self.module_dir}.{module}'
            status = '✓' if (module_path in self.imported_modules) else '✗'
            self.msg.log('log_compare_modules_ui', status=status, name=module)
            self.msg.say('compare_modules_ui', status=status, name=module)

    @staticmethod
    def reload_module(module):
        try:
            importlib.reload(module)
            return True
        except ModuleNotFoundError:
            return False
    def filtered_list_imported_modules(self):
        self.msg.say('filtered_list_imported_modules')
        for module in sys.modules.keys():
            location = f'{self.module_dir}.'
            name = module.replace(location, '')
            if module.startswith(location):
                self.msg.say("compare_modules_ui", status='·', name=name)
