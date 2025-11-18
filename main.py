import os
import traceback

from upload_levels import upload_levels



if __name__ == "__main__":
    while(True):
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            inp = int(input("[1] Добавить задания с нуля\n[2] Обновить существующие уровни\n[3] Выйти из программы\n"))
            os.system('cls' if os.name == 'nt' else 'clear')
            match inp:
                case 1:
                    upload_levels(True)
                case 2:
                    upload_levels(False)
                case 3:
                    break
                case _:
                    continue
        except Exception as err:
            with open("log.log", "a", encoding="utf-8") as f:
                f.write(traceback.format_exc())
            input("Неизвестная ошибка\nНажми любую клавишу для выхода")
            break
    