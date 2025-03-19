import asyncio
import logging
import os
import time

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
        print(dates_for_wniosek)
    else:
        clear_console_no_dates(status_code)
    logging.basicConfig(
        filename="gdansk.log",
        filemode='a',
        level=logging.INFO
    )

    logger.info(
        f"{logging.Formatter('%(asctime)s').format(logging.LogRecord(None, None, None, None, None, None, None))} | Статус: {status_code}, Данные: {dates_for_wniosek}")
