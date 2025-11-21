import traceback

from upload_levels import upload_levels
from upload_files import upload_files_to_source



if __name__ == "__main__":
    while(True):
        try:
            inp = int(input("[1] Добавить задания с нуля\n[2] Обновить существующие уровни\n[3] Закачать файлы из гугл диска в движок\n[4] Выйти из программы\n"))
            match inp:
                case 1:
                    upload_levels(True)
                case 2:
                    upload_levels(False)
                case 3:
                    upload_files_to_source()
                case 4:
                    break
                case _:
                    continue
        except Exception as err:
            with open("log.log", "a", encoding="utf-8") as f:
                f.write(traceback.format_exc())
            input("Неизвестная ошибка\nНажми любую клавишу для выхода")
            break
    