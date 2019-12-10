"""This file mimics path where future scripts will be called from."""
import os
from pprint import pprint

from tool_box import g_tools

me = os.environ["WORK_EMAIL"]

pprint(g_tools.find_user(me))


