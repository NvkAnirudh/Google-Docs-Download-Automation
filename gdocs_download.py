import os
import io
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.errors import HttpError

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.readonly', 'https://www.googleapis.com/auth/documents.readonly']

def authenticate_google():
    """Authenticate and return the Google Drive API service."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def download_folder_as_pdf(folder_id, destination_folder):
    """Download all Google Docs in a folder as PDFs."""
    creds = authenticate_google()
    drive_service = build('drive', 'v3', credentials=creds)
    docs_service = build('docs', 'v1', credentials=creds)

    # Query to find all Google Docs in the folder
    query = f"'{folder_id}' in parents and mimeType='application/vnd.google-apps.document'"
    results = drive_service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No Google Docs found in the folder.')
    else:
        print('Downloading Google Docs as PDFs:')
        for item in items:
            doc_id = item['id']
            doc_name = item['name']
            print(f'Downloading {doc_name}...')

            # Export the Google Doc as PDF
            request = drive_service.files().export_media(fileId=doc_id, mimeType='application/pdf')
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()

            # Save the PDF to the local folder
            pdf_path = os.path.join(destination_folder, f'{doc_name}.pdf')
            with open(pdf_path, 'wb') as f:
                f.write(fh.getvalue())
            print(f'Saved {doc_name}.pdf to {destination_folder}')

if __name__ == '__main__':
    folder_id = '1kBNnxRFj6f-lUz1Cc0QUgNWzTfr5LIQm'  # Replace with your Google Drive folder ID
    destination_folder = '/Users/anirudhnuti/Documents/bootcamp_rag_assistant/data'  # Local folder to save PDFs

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    download_folder_as_pdf(folder_id, destination_folder)