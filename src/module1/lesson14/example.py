from src.module1.lesson14.logging import Logger

logger = Logger('Example')

# logger.log("Мое первое залоггированное сообщение")
logger.info("Мое первое ИНФОРМАЦИОННОЕ сообщение")
logger.log(logger.Level.DEBUG, "Мое первое ОТЛАДОЧНОЕ сообщение")
logger.debug("Debug message")


try:
    raise NameError("Ты че урод")
except NameError as e:
    logger.log(logger.Level.ERROR, f"Ошибка в имени! Сообщение '{str(e)}'")
