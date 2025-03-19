import os
import re
import time


def create_normal_time(current_time,time_array):
    if len(current_time) == 2:
        current_time.append('00')
        updated_elements = ["0" + el if len(el) == 1 else el for el in current_time]
        normal_time = ":".join(updated_elements)
        if normal_time in time_array:
            return normal_time
        else:
            return None
    else:
        return None


def clear_console_no_dates():
    print("No available dates")
    time.sleep(2)
    os.system('cls')


def validate_fullname(user_input):
    pattern = re.match(r'^[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]{3,} [A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]{3,}$', string=user_input)
    if pattern:
        return pattern.group()
    else:
        return None


def validate_email(user_input):
    pattern = re.match(r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9_-]+)*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}$', user_input)
    if pattern:
        return pattern.group()
    else:
        return None


def process_date(user_input, dates):
    user_current_date = user_input.replace(".", "/")

    date_parts = user_current_date.replace("/", "-").split("-")

    if len(date_parts) == 3 and user_current_date in dates:
        return "-".join(reversed(date_parts))
    else:
        return None
