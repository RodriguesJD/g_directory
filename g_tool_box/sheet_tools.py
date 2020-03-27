from googleapiclient.discovery import build

try:
    from g_tool_box.google_credentials import google_creds
except ModuleNotFoundError:
    from g_directory.google_credentials import google_creds


def sheets_service() -> object:
    """
    This function negotiates access to Google Sheets.

    Returns:
        object: Google Sheets API service instance.

    """
    g_sheets_service = build('sheets', 'v4', credentials=google_creds())

    return g_sheets_service


def create_sheets(title, values):
    spreadsheet = {
        'properties': {
            'title': title
        }
    }

    spreadsheet = sheets_service().spreadsheets().create(body=spreadsheet,
                                                         fields='spreadsheetId').execute()

    spreadsheet_id = spreadsheet.get('spreadsheetId')

    body = {
        'values': values
    }
    result = sheets_service().spreadsheets().values().update(spreadsheetId=spreadsheet_id,
                                                             range="A1",
                                                             valueInputOption="USER_ENTERED",
                                                             body=body).execute()

    return spreadsheet_id


