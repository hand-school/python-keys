class Level:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Logger:
    ERROR = Level("ERROR", 1)
    WARNING = Level("WARNING", 2)
    DEBUG = Level("DEBUG", 3)
    INFO = Level("INFO", 4)

    def __init__(self, logger_name):
        print("init")
        self.logger_name = logger_name

    def log(self, level: Level, msg):
        log_msg = f'<{self.logger_name}> [{level}]: {msg}'
        print(log_msg)

    def error(self, msg):
        self.log(self.Level.ERROR, msg)

    def warning(self, msg):
        self.log(self.Level.WARNING, msg)

    def debug(self, msg):
        self.log(self.Level.DEBUG, msg)

    def info(self, msg):
        self.log(Logger.INFO, msg)

    def print_logo (lvl):
        print()


Logger("name")