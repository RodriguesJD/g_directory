from g_tool_box import drive_tools


def drive_create_upload_delete():

    # create base folder for test
    tmp_drive_folder = drive_tools.create_folder_in_drive("delete_this_root_folder")
    assert isinstance(tmp_drive_folder, str)




