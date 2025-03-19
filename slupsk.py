import asyncio
import logging
import os
import time

import requests
from art import tprint

from utils.available_dates import available_dates
from utils.utils import clear_console_no_dates

tprint("Online Registration", font="cybermedum")
tprint("Slupsk", font="cybermedum")
time.sleep(5)
os.system('cls')

while True:
    print("Fetching dates...")
    status_code, dates_for_wniosek = asyncio.run(
        available_dates('https://kolejka.gdansk.uw.gov.pl/admin/API/date/8/198/pl'))
    if dates_for_wniosek and status_code == 200:
        print(dates_for_wniosek)
        for i in range(len(dates_for_wniosek)):
            available_times = \
                requests.get(f'https://kolejka.gdansk.uw.gov.pl/admin/API/time/8/49/{dates_for_wniosek[i]}').json()[
                    'TIMES']
            print(f"{dates_for_wniosek[i]} : {available_times} ")
        print('\n\n')
    else:
        clear_console_no_dates(status_code)
    logging.basicConfig(
        filename="slupsk.log",
        filemode='a',
        level=logging.INFO
    )

    logger = logging.getLogger()

    logger.info(
        f"{logging.Formatter('%(asctime)s').format(logging.LogRecord(None, None, None, None, None, None, None))} | Статус: {status_code}, Данные: {dates_for_wniosek}")
