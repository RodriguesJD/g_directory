import os
from pathlib import Path
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


def test_find_folder_by_name():
    file_that_exists = os.environ["G_DRIVE_TEST_FOLDER"]
    folder = drive_tools.find_folder_by_name(file_that_exists)
    assert isinstance(folder, dict)

    kind = folder['kind']
    assert kind == 'drive#file'

    folder_id = folder['id']
    assert isinstance(folder_id, str)

    folder_name = folder['name']
    assert isinstance(folder_name, str)

    folder_type = folder['mimeType']
    assert folder_type == 'application/vnd.google-apps.folder'


def test_upload_csv_to_drive():
    path_to_upload_csv = "tests_g_directory/func/test_upload_files"
    csv_file_name = "csv_move_to_drive_test.csv"
    file_id = drive_tools.upload_csv_to_drive(csv_path=path_to_upload_csv, csv_name=csv_file_name)
    assert isinstance(file_id, str)

    # TODO find file to confirm it was made.

    # delete file from G drive after testing it.
    delete_status = drive_tools.delete_file_or_folder(file_id)
    assert delete_status
