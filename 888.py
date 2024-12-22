import logging

# Создаем логгер
logger = logging.getLogger("multi_file_logger")
logger.setLevel(logging.DEBUG)

# Создаем обработчик для debug_info.log
debug_info_handler = logging.FileHandler("debug_info.log")
debug_info_handler.setLevel(logging.DEBUG)

# Создаем обработчик для warnings_errors.log
warnings_errors_handler = logging.FileHandler("warnings_errors.log")
warnings_errors_handler.setLevel(logging.WARNING)

# Форматирование логов
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
debug_info_handler.setFormatter(formatter)
warnings_errors_handler.setFormatter(formatter)

# Добавляем обработчики к логгеру
logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

# Пример логирования
logger.debug("This is a DEBUG message.")
logger.info("This is an INFO message.")
logger.warning("This is a WARNING message.")
logger.error("This is an ERROR message.")
logger.critical("This is a CRITICAL message.")

_____________________________________________________

from datetime import datetime

# Получаем текущее время и дату
now = datetime.now()

# Форматируем дату и время в формате YYYY-MM-DD HH:MM:SS
formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

# Получаем день недели и номер недели в году
day_of_week = now.strftime("%A")  # День недели (например, Monday)
week_number = now.strftime("%U")  # Номер недели в году

# Выводим результат
print(f"Текущая дата и время: {formatted_datetime}")
print(f"День недели: {day_of_week}")
print(f"Номер недели в году: {week_number}")

___________________________________________

from datetime import datetime, timedelta

def get_future_date(days):
   """
   Функция принимает количество дней и возвращает дату через указанное количество дней.
   """
   # Текущая дата
   today = datetime.now()

   # Добавляем указанное количество дней
   future_date = today + timedelta(days=days)

   # Форматируем дату в формате YYYY-MM-DD
   formatted_date = future_date.strftime("%Y-%m-%d")

   return formatted_date

-_______________________________________
import argparse


def main():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(description="Скрипт принимает число и строку с опциями.")

    # Добавляем обязательные аргументы: число и строку
    parser.add_argument("number", type=int, help="Число для обработки.")
    parser.add_argument("string", type=str, help="Строка для вывода.")

    # Добавляем опции: --verbose и --repeat
    parser.add_argument("--verbose", action="store_true", help="Выводить дополнительную информацию.")
    parser.add_argument("--repeat", type=int, default=1, help="Сколько раз повторить строку.")

    # Парсим аргументы
    args = parser.parse_args()

    # Если установлен флаг --verbose
    if args.verbose:
        print(f"[DEBUG] Введено число: {args.number}")
        print(f"[DEBUG] Введена строка: {args.string}")
        print(f"[DEBUG] Повторить строку: {args.repeat} раз")

    # Повторяем строку указанное количество раз
    for _ in range(args.repeat):
        print(args.string)


# Запуск программы
if __name__ == "__main__":
    main()

    _____________________

import os
import logging
from collections import namedtuple
import argparse

# Настройка логирования
logging.basicConfig(
    filename="directory_info.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Определяем namedtuple для хранения информации
FileInfo = namedtuple("FileInfo", ["name", "extension", "is_dir", "parent"])


def collect_directory_info(directory_path):
    """
    Собирает информацию о содержимом директории.
    :param directory_path: Путь до директории
    :return: Список объектов FileInfo
    """
    directory_info = []

    for root, dirs, files in os.walk(directory_path):
        parent_dir = os.path.basename(root)  # Название родительского каталога

        # Обработка директорий
        for dir_name in dirs:
            info = FileInfo(name=dir_name, extension=None, is_dir=True, parent=parent_dir)
            directory_info.append(info)
            logging.info(f"Каталог: {info}")

        # Обработка файлов
        for file_name in files:
            name, extension = os.path.splitext(file_name)
            info = FileInfo(name=name, extension=extension if extension else None, is_dir=False, parent=parent_dir)
            directory_info.append(info)
            logging.info(f"Файл: {info}")

    return directory_info


def main():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(description="Сбор информации о содержимом директории.")
    parser.add_argument("directory", type=str, help="Путь до директории.")
    args = parser.parse_args()

    # Проверяем, существует ли директория
    if not os.path.isdir(args.directory):
        logging.error(f"Указанный путь не является директорией: {args.directory}")
        print(f"Ошибка: {args.directory} не является директорией.")
        return

    # Собираем информацию
    directory_info = collect_directory_info(args.directory)

    # Выводим результат
    print(f"Собрано {len(directory_info)} записей. Подробности в файле 'directory_info.log'.")


if __name__ == "__main__":
    main()