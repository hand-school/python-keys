# Дописать оставшиеся функции, а так же сделать фильтрацию сообщений по уровню лога по минимальному
# и фильтрацию по определённым уровням логам.
# Проявить фантазию + задания по декораторам


class Logger:
    class Level:
        ERROR = 1
        WARNING = 2
        INFO = 3
        DEBUG = 4

    Level = Level()

    levels = ("ERROR", "WARNING", "INFO", "DEBUG")

    def __init__(self, logger_name):
        self.logger_name = logger_name

    def log(self, level, msg):
        log_msg = f'<{self.logger_name}> [{self.levels[level - 1]}]: {msg}'
        print(log_msg)

    def debug(self, msg):
        self.log(self.Level.DEBUG, msg)

    def info(self, msg):
        self.log(self.Level.INFO, msg)

    def warning(self, msg):
        self.log(self.Level.WARNING, msg)

    def error(self, msg):
        self.log(self.Level.ERROR, msg)

