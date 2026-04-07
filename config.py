import os
from pathlib import Path

import requests
from loguru import logger

from dotenv import load_dotenv
load_dotenv("secrets/.env")



def check_config_files():
    env_path = Path("secrets/.env")
    if not env_path.exists():
        logger.error("Файл secrets/.env не найден")
        return False
    
    env_path = Path("secrets/credentials.json")
    if not env_path.exists():
        logger.error("Файл secrets/credentials.json не найден")
        return False
    
    return True


LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")

GAME_ID = os.getenv("GAME_ID")
CITY = os.getenv("CITY")
S_URL = f"https://classic.dzzzr.ru/{CITY}/admin/admin.php"
FILES_UPLOAD_URL = f"https://classic.dzzzr.ru/{CITY}/admin/tinymce/jscripts/tiny_mce/plugins/filemanager/stream/index.php"
DOCUMENT_ID = os.getenv("DOCUMENT_ID")
FOLDER_ID = os.getenv("FOLDER_ID")


def get_session():
    session = requests.Session()
    session.auth = (LOGIN, PASSWORD)

    return session
