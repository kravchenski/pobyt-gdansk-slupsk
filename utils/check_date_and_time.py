import asyncio
import os
import time
import requests

from utils.phrases import dates_phrase, enter_date_phrase, available_time_phrase, enter_time_phrase, \
    enter_full_name_phrase, \
    enter_email_phrase
from utils.registration_in_current_date import registration
from utils.utils import create_normal_time, validate_fullname, validate_email, process_date


def check_date_and_time(SedcoBranchID, SedcoServiceID, BranchID, ServiceID, times_admin_url, dates):
    user_fullname = None
    user_email = None
    user_normal_time = None
    normal_user_date = None
    print(dates_phrase.format(dates))
    time.sleep(2)
    while normal_user_date is None:
        user_input = input(enter_date_phrase)
        valid_date = process_date(user_input, dates)
        if valid_date is None:
            print("Incorrect date format. Try again.")
        else:
            normal_user_date = valid_date
    available_times = requests.get(f'{times_admin_url}/{normal_user_date}').json()[
        'TIMES']
    available_time_array = [available_time['time'] for available_time in available_times]
    print(available_time_phrase.format(available_time_array))
    time.sleep(2)
    while user_normal_time is None:
        user_current_time = input(enter_time_phrase).split('.')
        user_normal_time = create_normal_time(user_current_time, available_time_array)
        if user_normal_time is None:
            print("The time entered is incorrect. Try again.")
        else:
            user_normal_time = user_normal_time

    while user_fullname is None:
        user_fullname = validate_fullname(input(enter_full_name_phrase))
        if user_fullname is None:
            print("The fullName entered is incorrect. Try again.")
        else:
            user_fullname = user_fullname
    while user_email is None:
        user_email = validate_email(input(enter_email_phrase))
        if user_email is None:
            print("The email entered is incorrect. Try again.")
        else:
            user_email = user_email

    asyncio.run(
        registration(SedcoBranchID, SedcoServiceID, BranchID, ServiceID, normal_user_date,
                     user_normal_time, user_fullname, user_email))
    os.system('cls')
