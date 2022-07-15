import requests
from pprint import pprint
import json
from typing import Dict, Union

from schemas import (
    AccountType,
    AccessLevel,
    SecurityTradingStatus,
    AccountStatus
)

from models import (
    GetAccountsResponse,
)


token = ''
url = 'https://invest-public-api.tinkoff.ru/rest/tinkoff.public.invest.api.contract.v1.UsersService/GetAccounts'
headers = {
	'accept': 'application/json',
	'Content-Type': 'application/json',
	'Authorization': f'Bearer {token}'
}



response = json.dumps(requests.request(method='POST', url=url, headers=headers, json={}).json())
tmp = GetAccountsResponse.parse_raw(response)
print(tmp)