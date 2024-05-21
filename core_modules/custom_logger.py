import logging
import inspect


class CustomLogger(logging.Logger):
    """A custom logger class.
    Overrides the makeRecord function to allow for optional Type arg in logs.
    In our case, we use it to add emojis at the end of log messages for easier
    human parsing.
    The following methods can be used, with 'extra' being optional:
    * .info(str, extra={"Type":str})
    * .warning(str, extra={"Type":str})
    * .error(str, extra={"Type":str})
    """

    def __init__(self, name: str, log_name=''):
        """
        Initializes a custom logger as child of default python logger class.
        Has a custom log message format with additional 'Type' field.
        The logs are saved in a single file, named after the program's name.
        """
        super().__init__(name)
        self.propagate = False

        # Custom format adding an extra 'Type' field and removing milliseconds.
        formatter = logging.Formatter(
            fmt="%(asctime)-19s | %(levelname)-7s | %(message)-50s | %(Type)s ",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        # Names the log file after the program's name.
        handler = logging.FileHandler(
            filename=f"{log_name}.log", mode="w", encoding="utf-8"
        )

        # Look for any message of severity >= to INFO.
        handler.setLevel("INFO")
        handler.setFormatter(formatter)

        # Use our custom handler as output handler -> outputs to file.
        self.addHandler(handler)

        self.info("Custom logger initialized. Hi!", extra={"Type": "📝"})

    def makeRecord(self, *args, **kwargs):
        """
        Overrides the logger's makeRecord method to make extra arguments optional.
        makeRecord is called whenever we do logger.info(), warn(), or any other
        logger message function.
        This extra argument must be added as extra={"Type": string}.
        """
        rv = super(CustomLogger, self).makeRecord(*args, **kwargs)
        rv.__dict__["Type"] = rv.__dict__.get("Type", "  ")
        return rv

    def log_call(self):
        """Produces log entry with name of caller function."""
        self.info("Calling: " + inspect.currentframe().f_back.f_code.co_name)
