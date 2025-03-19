import asyncio
import os
import time

from art import tprint

from utils.check_date_and_time import check_date_and_time
from utils.get_branch_info import get_branch_service_info
from utils.phrases import type_of_registration_phrase
from utils.available_dates import available_dates
from utils.utils import clear_console_no_dates

tprint("Online Registration", font="cybermedum")
tprint("Gdansk / Slupsk", font="cybermedum")
time.sleep(5)
os.system('cls')

while True:
    type_of_registration = input(type_of_registration_phrase).upper()
    if type_of_registration == "B" or type_of_registration.startswith('B'):
        print("Fetching dates...")
        dates_for_wniosek = asyncio.run(
            available_dates('https://kolejka.gdansk.uw.gov.pl/admin/API/date/8/198/pl'))
        print('Fetching neccesary data...')
        SedcoBranchID, SedcoServiceID, BranchID, ServiceID = asyncio.run(
            get_branch_service_info('https://kolejka.gdansk.uw.gov.pl/admin/API/branch/8', 0))
        os.system('cls')
        if dates_for_wniosek:
            check_date_and_time(SedcoBranchID, SedcoServiceID, BranchID, ServiceID,
                                "https://kolejka.gdansk.uw.gov.pl/admin/API/time/8/49", dates_for_wniosek)
        else:
            clear_console_no_dates()
    elif type_of_registration == "C" or type_of_registration.startswith('C'):
        print("Fetching data...")
        dates_for_zezwolenia = asyncio.run(
            available_dates('https://kolejka.gdansk.uw.gov.pl/admin/API/date/8/202/pl'))
        print('Fetching neccesary data...')
        SedcoBranchID, SedcoServiceID, BranchID, ServiceID = asyncio.run(
            get_branch_service_info('https://kolejka.gdansk.uw.gov.pl/admin/API/branch/8', 1))
        os.system('cls')
        if dates_for_zezwolenia:
            check_date_and_time(SedcoBranchID, SedcoServiceID, BranchID, ServiceID,
                                "https://kolejka.gdansk.uw.gov.pl/admin/API/time/8/50", dates_for_zezwolenia)
        else:
            clear_console_no_dates()
