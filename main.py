import sys
import questionary
from loguru import logger

from config import check_config_files
from upload_levels import upload_levels
from upload_files import upload_files_to_source



logger.remove()
logger.add("log/error.log", level="ERROR")
logger.add(sys.stderr, format="<level>{level}</level>: <level>{message}</level>", colorize=True, level="DEBUG")


def main():
    if not check_config_files():
        return None
    
    choices=["Добавить задания с нуля", "Обновить существующие уровни", "Закачать файлы из гугл диска в движок", "Выйти из программы"]
    while True:
        try:
            action = questionary.select("Выберите действие:", choices=choices).ask()
            if action == choices[0]:
                upload_levels(True)
            if action == choices[1]:
                upload_levels(False)
            if action == choices[2]:
                upload_files_to_source()
            if action == choices[3]:
                break
        except Exception as err:
            logger.exception(err)
            questionary.text("Неизвестная ошибка\nНажми любую клавишу для выхода").ask()
            break
    
if __name__ == "__main__":
    main()
