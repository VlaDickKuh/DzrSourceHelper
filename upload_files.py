from loguru import logger

from download_files import authenticate
from download_files import get_files_from_drive
from config import get_session
from config import FOLDER_ID
from config import S_URL
from config import FILES_UPLOAD_URL
from config import GAME_ID



def upload_files_to_source():
    service = authenticate()
    logger.success('Аутентификация успешна. Начинается скачивание из гугл диска')
    drive_files = get_files_from_drive(service, FOLDER_ID)
    logger.success('Процесс скачивания завершен.')

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
            logger.success(f"Файл {file} загружен")
        elif "#error.file_exists" in resp.text:
           logger.warning(f"Файл {file} уже загружен") 
        else:
            logger.warning(f"Файл {file} не загружен")
            if "401" in resp.text:
               logger.warning(f"Код ошибки 401")
            else:
               logger.warning(resp.text)


if __name__== "__main__":
    upload_files_to_source()