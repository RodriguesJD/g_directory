"""
Functions for interact with Google Drive

"""
from pathlib import Path
from typing import Optional, Union
import pickle
import os.path
from pprint import pprint
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import errors

from g_tool_box.google_credentials import google_creds


def drive_service() -> object:
    """
    This function negotiates access to Google Drive.

    Returns:
        object: Drive API service instance.

    """
    g_drive_service = build('drive', 'v3', credentials=google_creds())

    return g_drive_service


def list_folders() -> list:
    """
    Creates a list of all the folders that api Oauth user has access to.

    Returns:
        list: List of folders. Each folder returns a dict of data.

    """
    page_token = None
    getting_files = True
    my_folders = []  # all the folders i have access to

    while getting_files:
        if not page_token:
            response = drive_service().files().list(q="mimeType = 'application/vnd.google-apps.folder'",
                                                    spaces='drive').execute()
        else:
            response = drive_service().files().list(q="mimeType = 'application/vnd.google-apps.folder'",
                                                    spaces='drive',
                                                    pageToken=page_token).execute()

        key_list = list(response.keys())
        if "nextPageToken" not in key_list:
            getting_files = False
        else:
            page_token = response["nextPageToken"]

        folders = response['files']  # Drive api refers to files and folders as files.
        for folder in folders:
            my_folders.append(folder)

    return my_folders


def find_folder_by_name(folder_name: str) -> Union[bool, dict]:
    """
    Search through all the folders that the Oauth user has access to. If the folder_name is found it returns a dict of 
    data about the folder.

    Args:
        folder_name: Name of the Google Drive folder.

    Returns:
        bool, dict: If folder_name is found it returns a dict. If the folder name is not found it returns False.
        
    """
    page_token = None
    getting_files = True
    folder_data = False

    while getting_files:
        if not page_token:
            response = drive_service().files().list(q="mimeType = 'application/vnd.google-apps.folder'",
                                                    spaces='drive').execute()
        else:
            response = drive_service().files().list(q="mimeType = 'application/vnd.google-apps.folder'", spaces='drive',
                                                    pageToken=page_token).execute()

        key_list = list(response.keys())
        if "nextPageToken" not in key_list:
            getting_files = False
        else:
            page_token = response["nextPageToken"]

        folders = response['files']  # Drive api refers to files and folders as files.
        for folder in folders:
            if folder_name == folder["name"]:
                folder_data = folder
                getting_files = False

    return folder_data


def find_file_by_name(file_name: str) -> Union[bool, dict]:
    """
    Search through all the files that the Oauth user has access to. If the file_name is found it returns a dict of
    data about the file.

    Args:
        file_name: Name of the Google Drive file.

    Returns:
        bool, dict: If filde_name is found it returns a dict. If the filde name is not found it returns False.

    """
    page_token = None
    getting_files = True
    file_data = False

    while getting_files:
        if not page_token:
            response = drive_service().files().list(q="mimeType != 'application/vnd.google-apps.folder'",
                                                    spaces='drive').execute()
        else:
            response = drive_service().files().list(q="mimeType != 'application/vnd.google-apps.folder'", spaces='drive',
                                                    pageToken=page_token).execute()

        key_list = list(response.keys())
        if "nextPageToken" not in key_list:
            getting_files = False
        else:
            page_token = response["nextPageToken"]

        folders = response['files']
        for folder in folders:
            if file_name == folder["name"]:
                file_data = folder
                getting_files = False

    return file_data


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

    csv_file = Path(f"{csv_path}/{csv_name}")
    media = MediaFileUpload(csv_file,
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


def delete_file_or_folder(file_id: str) -> bool:
    """
    Permanently delete a file, skipping the trash.

    Args:
        file_id: ID of the file to delete.
    Returns:
        bool: If the file is deleted then it returns True. If its not deleted then it returns False.

    """

    try:
        drive_service().files().delete(fileId=file_id).execute()
        file_deleted_status = True

    except errors.HttpError:
        file_deleted_status = False

    return file_deleted_status


def empty_trash():
    """
    This will empty the Oauth user's trash bin.

    Returns:
        True: I have no way of testing this that i can think of so im just returning true. HACKY i know.
    """
    drive_service().files().emptyTrash().execute()

    return True




