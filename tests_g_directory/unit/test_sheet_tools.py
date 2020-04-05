try:
    from g_tool_box import sheet_tools
    from g_tool_box import drive_tools
except ModuleNotFoundError:
    from g_directory.g_tool_box import sheet_tools
    from g_directory.g_tool_box import drive_tools


def test_dir_service():
    assert str(type(sheet_tools.sheets_service())) == "<class 'googleapiclient.discovery.Resource'>"


def test_write_to_existing_sheet():
    file_name = "del_me_test_writing_to_sheets"
    # Create test file
    sheet_id = drive_tools.create_file_in_drive(file_name)

    what_to_write_to_sheet = [["testa", "testb", "testc"]]
    result = sheet_tools.write_to_existing_sheet(sheet_id, what_to_write_to_sheet)
    assert isinstance(result, dict)

    find_file = drive_tools.find_file_by_name(file_name)
    assert isinstance(find_file, dict)

    # Delete file
    drive_tools.delete_file_or_folder(sheet_id)

    # Confirm the file is gone
    find_file = drive_tools.find_file_by_name(file_name)
    assert not find_file


