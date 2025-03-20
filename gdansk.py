import asyncio
import logging
import os
import time

import requests
from art import tprint
from utils.available_dates import available_dates
from utils.utils import clear_console_no_dates

tprint("Online Registration", font="cybermedum")
tprint("Gdansk", font="cybermedum")
time.sleep(5)
os.system('cls')
logger = logging.getLogger()

while True:
    print("Fetching dates...")
    status_code, dates_for_wniosek = asyncio.run(
        available_dates('https://kolejka.gdansk.uw.gov.pl/admin/API/date/5/304/pl'))
    if dates_for_wniosek and status_code == 200:
        dates_with_time = []
        for i in range(len(dates_for_wniosek)):
            normal_date = '-'.join(list(reversed(dates_for_wniosek[i].replace('/', '-').split('-'))))
            try:
                available_times = \
                    requests.get(f'https://kolejka.gdansk.uw.gov.pl/admin/API/time/5/3/{normal_date}').json()[
                        'TIMES']
                element = f"'{dates_for_wniosek[i]}' : '{",".join([available_time['time'] for available_time in available_times])}'"
                print(element)
                dates_with_time.append(element)
            except requests.exceptions.ConnectionError:
                print('NO INTERNET CONNECTION.....')
                logger.info(
                    f"{logging.Formatter('%(asctime)s').format(logging.LogRecord(None, None, None, None, None, None, None))} | Статус: {status_code}, Данные(время): ConnectionError")
                break

            except requests.exceptions.JSONDecodeError:
                print('Error: JSONDecodeError')
                logger.info(
                    f"{logging.Formatter('%(asctime)s').format(logging.LogRecord(None, None, None, None, None, None, None))} | Статус: {status_code}, Данные(время): JSONDecodeError")
                break
        print('\n\n')
        logger.info(
            f"{logging.Formatter('%(asctime)s').format(logging.LogRecord(None, None, None, None, None, None, None))} | Статус: {status_code}, Данные(время): {dates_with_time}")

    else:
        clear_console_no_dates(status_code)
    logging.basicConfig(
        filename="gdansk.log",
        filemode='a',
        level=logging.INFO
    )

    logger.info(
        f"{logging.Formatter('%(asctime)s').format(logging.LogRecord(None, None, None, None, None, None, None))} | Статус: {status_code}, Данные: {dates_for_wniosek}")
