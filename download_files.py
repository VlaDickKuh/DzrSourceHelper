import io

from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload



def authenticate():
    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = 'credentials.json'

    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('drive', 'v3', credentials=credentials)


def get_files_from_drive(service, folder_id):
    results = service.files().list(
        q=f"'{folder_id}' in parents",
        fields="nextPageToken, files(id, name, mimeType)"
    ).execute()
    items = results.get('files', [])

    files_binaries = {}
    for item in items:
        item_name = item['name']
        item_id = item['id']

        if 'image' in item['mimeType']:
            print(f'Найден файл: {item_name}')
            with io.BytesIO() as file_stream:
                request = service.files().get_media(fileId=item_id)
                downloader = MediaIoBaseDownload(file_stream, request)
                done = False
                while done is False:
                    status, done = downloader.next_chunk()
                    print(f'Скачивание {item_name}: {int(status.progress() * 100)}%')
                files_binaries[item_name] = file_stream.getvalue()
                print(file_stream)
    
    return files_binaries