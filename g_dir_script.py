"""This file mimics path where future scripts will be called from."""
from tool_box.g_tools import get_all_users

for user in get_all_users():
    print(user)
