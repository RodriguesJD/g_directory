import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pprint import pprint


def dir_service() -> object:
    """
    This function handles auth and service for google's access to admin sdk directory api.

    :return service: Rest API service object
    """
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/admin.directory.user',
              'https://www.googleapis.com/auth/admin.directory.group']

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

    service = build('admin', 'directory_v1', credentials=creds)

    return service


def get_all_users() -> list:
    """
    Get all data on all users and return it as a list of dictionaries.

    :return all_user_data: List of dictionaries of all users data.
    """
    all_user_data = []
    results = dir_service().users().list(customer='my_customer', orderBy='email').execute()
    next_page_token = results['nextPageToken']
    users = results['users']
    for user in users:
        all_user_data.append(user)

    while next_page_token:
        next_page_results = dir_service().users().list(customer='my_customer',
                                                       pageToken=next_page_token,
                                                       orderBy='email').execute()
        users = next_page_results['users']
        for user in users:
            all_user_data.append(user)
        keys_list = list(next_page_results.keys())
        if 'nextPageToken' in keys_list:
            next_page_token = next_page_results['nextPageToken']
        else:
            next_page_token = False

    return all_user_data


def find_user(user_email: str) -> dict:
    """
    Search for user by email.

    :param user_email: Users email address.
    :return user_data: Users data in a dictionary.
    """
    user_data = dir_service().users().get(userKey=user_email).execute()

    return user_data


def get_all_groups() -> list:
    """
    Get all data on all groups and return it as a list of dictionaries.

    :return all_group_data: List of dictionaries of all group data.
    """
    all_group_data = []
    results = dir_service().groups().list(customer='my_customer').execute()
    next_page_token = results['nextPageToken']
    groups = results['groups']
    for group in groups:
        all_group_data.append(group)

    while next_page_token:
        next_page_results = dir_service().groups().list(customer='my_customer',
                                                        pageToken=next_page_token).execute()
        groups = next_page_results['groups']
        for group in groups:
            all_group_data.append(group)
        keys_list = list(next_page_results.keys())
        if 'nextPageToken' in keys_list:
            next_page_token = next_page_results['nextPageToken']
        else:
            next_page_token = False

    return all_group_data
