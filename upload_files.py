import os

import requests

from download_files import authenticate
from download_files import get_files_from_drive
from config import get_session
from config import FOLDER_ID
from config import S_URL
from config import FILES_UPLOAD_URL


def upload_files_to_source():
    service = authenticate()
    print('Аутентификация успешна. Начинается скачивание...')
    files = get_files_from_drive(service, FOLDER_ID)
    print('Процесс скачивания завершен.')

    for file in files:
        session = get_session()
        resp_cook = session.get(S_URL)
        data = {
            "cmd":"fm.upload",
            "path": "{0}/games/1549",
            "domain": "",
            "name0": str(file).split(".")[0],
            "upload": "Загрузка"
        }
        file = {
            "file0": (file, files.get(file), None)
        }
        resp = session.post(FILES_UPLOAD_URL, cookies=resp_cook.cookies, data=data, files=file)
        print(resp.text)
        


if __name__== "__main__":
    upload_files_to_source()