import json
import time

import requests


async def registration(SedcoBranchID, SedcoServiceID, BranchID, ServiceID, date, reservation_time, full_name, email):
    headers = {
        'sec-ch-ua-platform': '"Android"',
        'Referer': 'https://kolejka.gdansk.uw.gov.pl/branch/8',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Brave";v="134"',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary0iY4aqPrxgkfQOBm',
        'sec-ch-ua-mobile': '?1',
    }
    data = {
        "SedcoBranchID": SedcoBranchID,
        "SedcoServiceID": SedcoServiceID,
        "BranchID": BranchID,
        "ServiceID": ServiceID,
        "AppointmentDay": date,
        "AppointmentTime": reservation_time,
        "CustomerInfo": {
            "AdditionalInfo": {
                "CustomerName_L2": full_name,
                "Email": email,
                "checkbox": True
            }
        },
        "LanguagePrefix": "pl",
        "SelectedLanguage": "pl",
        "SegmentIdentification": "internet"
    }
    json_string = json.dumps(data)
    files = {
        'JSONForm': (None, json_string)
    }
    print(files)
    time.sleep(10)
    response = requests.post('https://kolejka.gdansk.uw.gov.pl/admin/API/take_appointment', headers=headers,
                             files=files)
    return response

## SEND TO C
# files = {
#     'JSONForm': (None, '{"SedcoBranchID":181,"SedcoServiceID":202,"BranchID":8,"ServiceID":50,"AppointmentDay":"2025-03-27","AppointmentTime":"09:30:00","CustomerInfo":{"AdditionalInfo":{"CustomerName_L2":"asdasdas sadds","Email":"asdasd@gmail.com","checkbox":true}},"LanguagePrefix":"pl","SelectedLanguage":"pl","SegmentIdentification":"internet"}'),
# }
