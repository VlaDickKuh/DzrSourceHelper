import json

from download_files import authenticate
from download_files import get_files_from_drive
from config import get_session
from config import FOLDER_ID
from config import S_URL
from config import FILES_UPLOAD_URL
from config import GAME_ID



def upload_files_to_source():
    service = authenticate()
    print('Аутентификация успешна. Начинается скачивание из гугл диска')
    drive_files = get_files_from_drive(service, FOLDER_ID)
    print('Процесс скачивания завершен.')

    session = get_session()
    resp_cook = session.get(S_URL)
    for file in drive_files:
        data = {
            "cmd":"fm.upload",
            "path": "{0}" + f"/games/{GAME_ID}",
            "domain": "",
            "name0": str(file).split(".")[0],
            "upload": "Загрузка"
        }
        files = {
            "file0": (file, drive_files.get(file), None)
        }
        resp = session.post(FILES_UPLOAD_URL, cookies=resp_cook.cookies, data=data, files=files)
        if "#message.upload_ok" in resp.text:
            print(f"Файл {file} загружен")
        elif "#error.file_exists" in resp.text:
           print(f"Файл {file} уже загружен") 
        else:
           print(f"Файл {file} не загружен")
           print(resp.text)


if __name__== "__main__":
    upload_files_to_source()