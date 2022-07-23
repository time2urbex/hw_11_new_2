import logging

# Создаем или получаем новый логгер
logger_one = logging.getLogger("one")

# Cоздаем ему обработчик
console_handler = logging.StreamHandler()

# Создаем новое форматирование (объект класса Formatter)
formatter_one = logging.Formatter("%(asctime)s : %(message)s : %(levelname)s : %(funcName)s : %(pathname)s")
# Применяем форматирование к обработчику
console_handler.setFormatter(formatter_one)

# Добавлякем обработчик к журналу
logger_one.addHandler(console_handler)

logger_one.warning("Логгер первый работает")

name = "Алиса"
logging.info(f"Пользователь {name} пытается войти")
logging.warning(f"Пользователь {name} проблемы с оплатой")
logging.critical(f"Пользователь {name} все сломал")