from g_tool_box import drive_tools
from pathlib import Path


def test_drive_create_upload_delete():
    """
    This tests the functionality of finding, creating, and deleting folders. It also test uploading of a csv file to
    G drive.

    """
    # Empty the trash before you begin.
    drive_tools.empty_trash()

    tmp_base_folder = "delete_this_root_folder"

    # Confirm folder does not exist, if it does then delete it.
    find_folder = drive_tools.find_folder_by_name(tmp_base_folder)  # Find a folder that the Oauth user has access to.
    if find_folder:
        file_deleted = drive_tools.delete_file_or_folder(find_folder['id'])
        assert file_deleted
        find_folder = drive_tools.find_folder_by_name(tmp_base_folder)

    assert not find_folder

    # create base folder for test
    folder_id = drive_tools.create_folder_in_drive("delete_this_root_folder")
    assert isinstance(folder_id, str)

    # Confirm folder was created.
    find_folder = drive_tools.find_folder_by_name(tmp_base_folder)
    assert isinstance(find_folder, dict)

    # Upload csv file to folder_id in g drive.
    path_to_upload_csv = "tests_g_directory/func/test_upload_files"
    csv_file_name = "csv_move_to_drive_test.csv"
    upload_file = drive_tools.upload_csv_to_drive(csv_path=path_to_upload_csv,
                                                  csv_name=csv_file_name,
                                                  folder_id=folder_id)

    # Confirm file was uploaded.
    find_file = drive_tools.find_file_by_name(csv_file_name)
    assert isinstance(find_file, dict)


    # Delete folder and empty trash
    file_deleted = drive_tools.delete_file_or_folder(folder_id)
    assert file_deleted
    drive_tools.empty_trash()

    # Confirm file was deleted.
    find_folder = drive_tools.find_folder_by_name(tmp_base_folder)  # Find a folder that the Oauth user has access to.
    assert not find_folder






