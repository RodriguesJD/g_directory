"""
Functions for interact with Google Drive

"""
from pathlib import Path
from typing import Optional
import pickle
import os.path
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from g_tool_box.google_credentials import google_creds


def drive_service() -> object:
    """
    This function negotiates access to Google Drive.

    Returns:
        object: Rest API service object for Google Drive.

    """
    g_drive_service = build('drive', 'v3', credentials=google_creds())

    return g_drive_service

# TODO create docsting
#  TODO typehinting for the funcs below
# TODO create testing for create add delete for functional testing


def upload_csv_to_drive(csv_path: str, csv_name: str, folder_id: Optional[str] = None) -> str:
    """
    Upload csv files to Google Drive. If no folder_id is passed to the function then it will upload the csv
    to the users root of the G drive.

    Args:
        csv_path (str): Local path of the csv you wish to upload to google drive.
        csv_name (str): File name fo the local csv you wish to upload to google drive.
        folder_id (str): If you want to drop the file somewhere other than the root add the folder id.

    Returns:
        str: The google drive file id for the uploaded csv file.

    """
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


def create_folder_in_drive(folder_name: str, folder_id: Optional[str] = None) -> str:
    """
    This creates a folder in Google Drive. If no folder_id is passed to the function then it will create the
    folder in the root of the G Drive.

    Args:
        folder_name (str): Name of the folder that is going to be created.
        folder_id (str): Google drive's folder id you with to create the new folder in.
    Returns:
        str: Returns the google drive folder id of the newly created g drive folder.

    """
    if folder_id:
        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [folder_id]
        }
    else:
        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
    folder = drive_service().files().create(body=file_metadata,
                                            fields='id').execute()

    return folder.get('id')


