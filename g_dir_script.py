"""This file mimics path where future scripts will be called from."""
import os
from pprint import pprint
import  csv
from g_tool_box import g_tools
from googleapiclient.errors import HttpError



def user_is_terminated(org_path):
    """
    If the user's email has the @li.me then the user is a full time employee.

    :param user_email:
    :return:
    """
    terminated_ou_s = ['/Terminated', '/Terminated - Legal Hold', '/Terminated - Active']
    if org_path in terminated_ou_s:
        user_terminated = True
    else:
        user_terminated = False

    return user_terminated


users_terminated = []

with open('needActiveUserList - Sheet1.csv') as user_file:
    csv_reader = csv.reader(user_file, delimiter=',')
    for user in csv_reader:
        username = user[0]
        user_not_active = False
        try:
            user_data = g_tools.find_user(user[0])
            if user_data:
                org_path = user_data['orgUnitPath']
                is_term = user_is_terminated(org_path)

        except HttpError:
            is_term = True

        if is_term:
            users_terminated.append(user)


with open('terminated.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for user in users_terminated:
        employee_writer.writerow(user)

