from googleapiclient.discovery import build
from pprint import pprint


from g_tool_box.google_credentials import google_creds


def directory_service() -> object:
    """
    This function negotiates access to Google Directory API.

    Returns:
        object: Directory API service instance.

    """
    dir_service = build('admin', 'directory_v1', credentials=google_creds())

    return dir_service


def get_all_users() -> list:
    """
    Get all data on all users and return it as a list of dictionaries.

    Returns:
         list: List of dictionaries of all users data.
    """
    all_user_data = []
    results = directory_service().users().list(customer='my_customer', orderBy='email', projection="full").execute()
    next_page_token = results['nextPageToken']
    users = results['users']
    for user in users:
        all_user_data.append(user)

    while next_page_token:
        next_page_results = directory_service().users().list(customer='my_customer',
                                                             projection="full",
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


def find_user(primary_user_email: str) -> dict:
    """
    Search for user by primary email.
    Args:
        primary_user_email: Users primary email address.

    Returns:
        dict: Users data.
    """
    user_data = directory_service().users().get(userKey=primary_user_email, projection="full").execute()
    if primary_user_email.lower() != user_data['primaryEmail'].lower():
        user_data = False

    return user_data


def update_user(primary_user_email: str, user_dict: dict) -> dict:
    """
    Update or add data to an existing user.

    Args:
        primary_user_email: User's email.
        user_dict: New data that will update or add to existing data.

    Returns:
        dict: Response from Google's server.
    """
    # TODO create test for this func
    google_response = directory_service().users().update(userKey=primary_user_email, body=user_dict).execute()
    return google_response


def get_all_groups() -> list:
    """
    Get all data on all groups and return it as a list of dictionaries.

    Return:
         list: List of dictionaries of all group data.
    """
    all_group_data = []
    results = directory_service().groups().list(customer='my_customer').execute()
    next_page_token = results['nextPageToken']
    groups = results['groups']
    for group in groups:
        all_group_data.append(group)

    while next_page_token:
        next_page_results = directory_service().groups().list(customer='my_customer',
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


def find_group(group_email: str) -> dict:
    """
    Search for group by email.

    Args:
        group_email: Group email address.
    Returns:

        dict: Group data in a dictionary.
    """
    group_data = directory_service().groups().get(groupKey=group_email).execute()

    return group_data


def get_all_orgunits() -> list:
    """
    Get all data on all org_units and return it as a list of dictionaries.

    Returns:
        list: List of dictionaries of all org_unit data.
    """
    all_orgunits_data = []
    results = directory_service().orgunits().list(customerId='my_customer').execute()
    org_units = results['organizationUnits']
    for org_unit in org_units:
        all_orgunits_data.append(org_unit)

    keys_list = list(results.keys())
    if 'nextPageToken' in keys_list:
        next_page_token = results['nextPageToken']
        while next_page_token:
            next_page_results = directory_service().orgunits().list(customerId='my_customer',
                                                                    pageToken=next_page_token).execute()
            org_units = next_page_results['organizationUnits']
            for org_unit in org_units:
                all_orgunits_data.append(org_unit)

            keys_list = list(next_page_results.keys())
            if 'nextPageToken' in keys_list:
                next_page_token = next_page_results['nextPageToken']
            else:
                next_page_token = False

    return all_orgunits_data
