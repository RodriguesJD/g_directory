from g_tool_box import drive_tools


def test_drive_create_upload_delete():
    # Empty the trash before you begin.
    drive_tools.empty_trash()

    tmp_base_folder = "delete_this_root_folder"

    # Confirm folder does not exist.
    find_folder = drive_tools.find_folder_by_name(tmp_base_folder)  # Find a folder that the Oauth user has access to.
    assert not find_folder

    # create base folder for test
    tmp_drive_folder = drive_tools.create_folder_in_drive("delete_this_root_folder")
    assert isinstance(tmp_drive_folder, str)

    # Confirm folder was created.
    find_folder = drive_tools.find_folder_by_name(tmp_base_folder)
    assert isinstance(find_folder, dict)

    # Delete folder and empty trash
    file_deleted = drive_tools.delete_file(tmp_drive_folder)
    assert file_deleted
    drive_tools.empty_trash()

    # Confirm file was deleted.
    find_folder = drive_tools.find_folder_by_name(tmp_base_folder)  # Find a folder that the Oauth user has access to.
    assert not find_folder






