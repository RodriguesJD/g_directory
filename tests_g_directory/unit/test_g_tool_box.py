import os
try:
    from g_tool_box import g_tools
except ModuleNotFoundError:
    from g_directory.g_tool_box import g_tools

my_work_email = os.environ["WORK_EMAIL"]
group_email = os.environ["WORK_GROUP_EMAIL"]


def test_dir_service():
    assert str(type(g_tools.directory_service())) == "<class 'googleapiclient.discovery.Resource'>"


def test_get_all_users():
    all_users = g_tools.get_all_users()
    assert isinstance(all_users, list)
    for user in all_users:
        assert isinstance(user, dict)


def test_find_user():
    user = g_tools.find_user(my_work_email)
    assert isinstance(user, dict)


def test_update_user():
    pass


def test_get_all_groups():
    all_groups = g_tools.get_all_groups()
    assert isinstance(all_groups, list)
    for group in all_groups:
        assert isinstance(group, dict)


def test_find_group():
    group = g_tools.find_group(group_email)
    assert isinstance(group, dict)


def test_find_group_members():
    group_email = os.environ["WORK_GROUP_EMAIL"]
    group_member_dict = g_tools.find_group_members(group_email)
    assert isinstance(group_member_dict, dict)
    assert isinstance(group_member_dict["members"], list)


def test_get_all_orgunits():
    all_org_units = g_tools.get_all_orgunits()
    assert isinstance(all_org_units, list)
    for org_unit in all_org_units:
        assert isinstance(org_unit, dict)
