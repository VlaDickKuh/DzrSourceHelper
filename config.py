import os

import requests

from dotenv import load_dotenv
load_dotenv()



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
