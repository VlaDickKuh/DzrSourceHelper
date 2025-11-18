import os
import io

from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload

from dotenv import load_dotenv
load_dotenv()



def authenticate():
    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = 'credentials.json'

    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('drive', 'v3', credentials=credentials)


def download_file(service, file_id, file_name, download_path):
    file_path = os.path.join(download_path, file_name)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    try:
        request = service.files().get_media(fileId=file_id)
        fh = io.FileIO(file_path, 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(f'Скачивание {file_name}: {int(status.progress() * 100)}%')
    except Exception as e:
        print(f'Ошибка при скачивании {file_name}: {e}')


def list_files_recursively(service, folder_id, local_base_path, current_path=""):
    results = service.files().list(
        q=f"'{folder_id}' in parents",
        fields="files(id, name, mimeType)"
    ).execute()
    items = results.get('files', [])
    
    for item in items:
        item_name = item['name']
        item_id = item['id']
        relative_path = os.path.join(current_path, item_name)
        full_local_path = os.path.join(local_base_path, relative_path)
        
        if item['mimeType'] == 'application/vnd.google-apps.folder':
            print(f'Обработка папки: {relative_path}')
            list_files_recursively(service, item_id, local_base_path, relative_path)
        else:
            print(f'Найден файл: {relative_path}')
            download_file(service, item_id, item_name, os.path.dirname(full_local_path))


def main():
    FOLDER_ID = os.getenv('FOLDER_ID') 
    LOCAL_DOWNLOAD_PATH = './downloads'
    
    service = authenticate()
    print('Аутентификация успешна. Начинается скачивание...')
    list_files_recursively(service, FOLDER_ID, LOCAL_DOWNLOAD_PATH)
    print('Процесс скачивания завершен.')


if __name__ == '__main__':
    main()