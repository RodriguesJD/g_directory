"""
Functions for interact with Google Drive

"""
from pathlib import Path
import pickle
import os.path
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from g_tool_box.google_credentials import google_creds


def drive_service():
    g_drive_service = build('drive', 'v3', credentials=google_creds())

    return g_drive_service


def upload_csv_to_drive(csv_path, csv_name, folder_id=None):
    if folder_id:
        csv_metadata = {'name': csv_name,
                        'parents': [folder_id]}
    else:
        csv_metadata = {'name': csv_name}

    media = MediaFileUpload(csv_path,
                            mimetype='text/csv')
    file = drive_service().files().create(body=csv_metadata,
                                          media_body=media,
                                          fields='id').execute()

    return file.get('id')


def create_folder_in_drive(folder_id, folder_name):
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [folder_id]
    }
    folder = drive_service().files().create(body=file_metadata,
                                        fields='id').execute()

    return folder.get('id')


