import os
import io
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Области доступа. Для полного доступа к файлам на Диске используется scope 'drive'
SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    """Аутентификация в Google Drive API"""
    creds = None
    # Файл token.json сохраняет токены доступа и обновления
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # Если нет действительных учетных данных, пользователь проходит аутентификацию
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Сохраняем учетные данные для следующего запуска
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('drive', 'v3', credentials=creds)

def download_file(service, file_id, file_name, download_path):
    """Скачивает файл по его ID"""
    file_path = os.path.join(download_path, file_name)
    # Создаем папки, если они не существуют
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
    """
    Рекурсивно получает список всех файлов в папке и ее подпапках,
    и скачивает их, сохраняя структуру каталогов.
    """
    # Запрос на получение всех файлов и папок внутри текущей папки
    results = service.files().list(
        q=f"'{folder_id}' in parents",
        fields="files(id, name, mimeType)"
    ).execute()
    items = results.get('files', [])
    
    for item in items:
        item_name = item['name']
        item_id = item['id']
        # Формируем относительный путь к файлу/папке внутри структуры
        relative_path = os.path.join(current_path, item_name)
        full_local_path = os.path.join(local_base_path, relative_path)
        
        if item['mimeType'] == 'application/vnd.google-apps.folder':
            # Если это папка, рекурсивно обрабатываем ее содержимое
            print(f'Обработка папки: {relative_path}')
            list_files_recursively(service, item_id, local_base_path, relative_path)
        else:
            # Если это файл, скачиваем его
            print(f'Найден файл: {relative_path}')
            download_file(service, item_id, item_name, os.path.dirname(full_local_path))

def main():
    # ID папки на Google Drive, из которой нужно скачать файлы
    # Найти ID можно из URL папки: https://drive.google.com/drive/folders/ВАШ_FOLDER_ID
    FOLDER_ID = '1PI-0wFa7EH0b2McS_1fiSR0APinSLMxm'
    # Локальная папка для сохранения файлов
    LOCAL_DOWNLOAD_PATH = './downloads'
    
    service = authenticate()
    print('Аутентификация успешна. Начинается скачивание...')
    list_files_recursively(service, FOLDER_ID, LOCAL_DOWNLOAD_PATH)
    print('Процесс скачивания завершен.')

if __name__ == '__main__':
    main()