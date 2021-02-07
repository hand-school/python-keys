class Logger:
    class Level:
        ERROR = 1
        WARNING = 2
        DEBUG = 3
        INFO = 4

    Level = Level()

    levels = ("ERROR", "WARNING", "DEBUG", "INFO")

    def __init__(self, logger_name):
        self.logger_name = logger_name

    def log(self, level, msg):
        log_msg = f'<{self.logger_name}> [{self.levels[level - 1]}]: {msg}'
        print(log_msg)

    def error(self, msg):
        self.log(self.Level.ERROR, msg)

    def warning(self, msg):
        self.log(self.Level.WARNING, msg)

    def debug(self, msg):
        self.log(self.Level.DEBUG, msg)

    def info(self, msg):
        self.log(self.Level.INFO, msg)

    def print_logo (lvl):
        print()

