from g_tool_box import drive_tools


def test_dir_service():
    assert str(type(drive_tools.drive_service())) == "<class 'googleapiclient.discovery.Resource'>"


def test_list_folders():
    list_of_folders = drive_tools.list_folders()
    assert isinstance(list_of_folders, list)

    for folder in list_of_folders:
        assert isinstance(folder, dict)

        kind = folder['kind']
        assert kind == 'drive#file'

        folder_id = folder['id']
        assert isinstance(folder_id, str)

        folder_name = folder['name']
        assert isinstance(folder_name, str)

        folder_type = folder['mimeType']
        assert folder_type == 'application/vnd.google-apps.folder'

