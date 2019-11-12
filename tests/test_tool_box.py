from tool_box.g_tools import dir_service


def test_dir_service():
    assert str(type(dir_service())) == "<class 'googleapiclient.discovery.Resource'>"