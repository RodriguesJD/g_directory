"""This file mimics path where future scripts will be called from."""
import os
from tool_box import g_tools

my_work_email = os.environ["WORK_EMAIL"]
g_tools.find_user(my_work_email)



