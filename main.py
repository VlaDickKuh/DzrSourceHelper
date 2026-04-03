import os
import sys
from datetime import datetime

import questionary
from loguru import logger

from config import check_config_files
from src.upload_levels import upload_levels
from src.upload_files import upload_files_to_source



run_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
info_log_file = f"log/info_{run_timestamp}.log"
error_log_file = f"log/error_{run_timestamp}.log"
logger.remove()
logger.add(error_log_file, level="ERROR")
logger.add(info_log_file, level="INFO", filter=lambda record: record["level"].name not in ("ERROR", "CRITICAL"))
logger.add(sys.stderr, format="<level>{level}</level>: <level>{message}</level>", colorize=True, level="DEBUG")


def main():
    if not check_config_files():
        return None
    
    choices=["Добавить задания с нуля", "Обновить существующие уровни", "Закачать файлы из гугл диска в движок", "Выйти из программы"]
    while True:
        try:
            action = questionary.select("Выберите действие:", choices=choices).ask()
            os.system("cls")
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
