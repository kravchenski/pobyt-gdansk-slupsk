import requests


async def get_branch_service_info(url, i):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.7',
        'priority': 'u=1, i',
        'referer': 'https://kolejka.gdansk.uw.gov.pl/branch/8',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Brave";v="134"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36',
    }
    # https://kolejka.gdansk.uw.gov.pl/admin/API/branch/5
    response = requests.get(url, headers=headers).json()
    ServiceID = response["services"][i]["id"]
    SedcoServiceID = response["services"][i]["service_id"]
    SedcoBranchID = response["branch"]["branch_id"]
    BranchID = response["branch"]["id"]
    return SedcoBranchID, SedcoServiceID, BranchID, ServiceID
