from g_tool_box import sheet_tools


def test_dir_service():
    assert str(type(sheet_tools.sheets_service())) == "<class 'googleapiclient.discovery.Resource'>"


def test_create_sheets():
    # TODO create mock data, dump data to sheets, test the sheet, cleanup by deleting sheet
    pass
