"""This file mimics path where future scripts will be called from."""
from tool_box import g_tools
from pprint import pprint


for group in g_tools.get_all_groups():
    pprint(group)

