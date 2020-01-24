"""
For applications that use the OAuth 2.0 protocol to call Google APIs, you can use an OAuth 2.0 client ID
to generate an access token. The token contains a unique identifier.

For instructions on how to setup OAuth 2.0 got to
https://support.google.com/googleapi/answer/6158849
"""

import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pprint import pprint


def google_creds():
    """
       This function handles auth and service for google's access to admin sdk directory api.

       :return service: Rest API service object
       """
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/admin.directory.user',
              'https://www.googleapis.com/auth/admin.directory.group',
              'https://www.googleapis.com/auth/admin.directory.orgunit',
              'https://www.googleapis.com/auth/drive.file',
              'https://www.googleapis.com/auth/drive',
              'https://www.googleapis.com/auth/drive.activity'
              ]

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds