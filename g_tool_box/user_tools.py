

def is_fte(ou: str, primary_email: str) -> bool:
    """
    Decide if a user is FTE or CW.

    NOTE: All users in the /Lime Support ou are CW except dijana.antic@li.me
    Args:
        ou (str): The users ou according to google.
        primary_email (str): The users primary email according to google.

    Returns:
        bool: If the user is not in an ou listed below then they are FTE. If false they are not an FTE.
    """
    if "/Lime Support" in ou:
        if primary_email == 'dijana.antic@li.me':  # This is the only exception to /Lime Support, all others are not FTE
            user_is_fte = True
        else:
            user_is_fte = False
    elif "/Lime Contractor" in ou:
        user_is_fte = False
    elif '/Service Accounts' in ou:
        user_is_fte = False
    elif '/Terminated' in ou:
        user_is_fte = False
    elif "/Test OU" in ou:
        user_is_fte = False
    elif "/Warehouse Devices" in ou:
        user_is_fte = False
    elif "/Warehouse Devices" in ou:
        user_is_fte = False
    else:
        user_is_fte = True

    return user_is_fte
