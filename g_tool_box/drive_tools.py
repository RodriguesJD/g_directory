"""
Interact with Google Drive

"""
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from g_tool_box.google_credentials import google_creds


def drive_service():
    g_drive_service = build('drive', 'v3', credentials=google_creds())

    return g_drive_service

def main():

    results = drive_service().files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))


