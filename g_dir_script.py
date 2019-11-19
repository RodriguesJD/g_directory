"""This file mimics path where future scripts will be called from."""
from tool_box import g_tools
from pprint import pprint
import os


group_email = os.environ["WORK_GROUP_EMAIL"]
pprint(g_tools.find_group(group_email))
