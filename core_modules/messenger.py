from . import utils


class Messenger:
    """
    Messenger outputs formatted predefined messages in print and/or log.

    The goal is centralisation of messages in a single file, allowing easier
    standardisation.

    It carries messages imported from messages.json in the provided resource
    directory, and applies formatting from styles.json on them.

    * say('key')    Prints the message stored at 'key' in messages.json.
    * log('key', **kwargs)  Logs the message stored at 'key' in messages.json.
    """

    def __init__(self, resource_dir='', logger=object, tab=str):
        self.logger = logger
        self.resource_dir = resource_dir
        self.styles = self.set_styles_dict(tab)
        self.messages = self.set_msg_dict()

    def set_msg_dict(self):
        """
        Grabs messages from messages.json and stores them in messages dict.
        """
        return utils.Utils.get_resource(self.resource_dir, "messages", "json")

    def set_styles_dict(self, tab):
        """
        Grabs styles from styles.json and stores them in styles dict after
        adding ANSI escape code in front.
        """
        styles = utils.Utils.get_resource(self.resource_dir, "styles", "json")

        for key in styles:
            styles[key] = "\033[" + styles[key]  # \033[ -> ANSI
        styles.update({"tab": tab, "new_line": chr(10)})  # Adding TAB to our styles.

        return styles

    def get_message(self, msg_key):
        """Returns contents of message at msg_key within the messages dict."""
        try:
            msg = str(self.messages[msg_key])
        except KeyError:
            msg = f"ERROR: line {msg_key} not found."
        return msg

    def format_message(self, msg, **kwargs):
        """
        Formats msg in two rounds, leaving missing keys untouched.
        1. applies self.styles as format_map.
        2. applies **kwargs to msg as format_map.
        """
        msg = msg.format_map(utils.SafeDict(self.styles))
        msg = msg.format_map(utils.SafeDict(**kwargs))
        return msg

    def say(self, msg_key, **kwargs):
        """
        Takes in a message key and **kwargs, prints message at msg_key with
        vars replaced by **kwargs and style.
        """
        msg = self.get_message(msg_key)
        print(self.format_message(msg, **kwargs))

    def log(self, msg_key, level="info", extra="", **kwargs):
        msg = self.get_message(msg_key)
        msg = self.format_message(msg, **kwargs)
        match level:
            case "info":
                self.logger.info(msg, extra={"Type": extra})
            case "error":
                self.logger.error(msg, extra={"Type": '❗'})