from tool_box import g_tools


def test_dir_service():
    assert str(type(g_tools.dir_service())) == "<class 'googleapiclient.discovery.Resource'>"


def test_get_all_users():
    all_users = g_tools.get_all_users()
    assert isinstance(all_users, list)
    for user in all_users:
        assert isinstance(user, dict)
        # TODO test the content of the dict
