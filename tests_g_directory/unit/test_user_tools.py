from g_tool_box import user_tools


def test_is_fte():
    # TODO move this function to a lime project.

    fte_user = "dijana.antic@li.me"
    fte_ou = "/Lime IT"

    user_is_fte = user_tools.is_fte(fte_ou, fte_ou)
    assert user_is_fte

    not_fte_user = "Not.fte@li.me"
    not_fte_ou = "/Lime Support"

    user_is_fte = user_tools.is_fte(not_fte_ou, not_fte_user)
    assert not user_is_fte

    except_user = fte_user
    user_is_fte_exception = user_tools.is_fte(not_fte_ou, except_user)
    assert user_is_fte_exception