import requests

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

from pprint import pprint


class Api:
    

# def get_accounts(url: str, token: str):
#     response = requests.post(url=url, headers=headers)
#     if response.status_code == 200:
#         return response


TOKEN = 't.BLtZWmlj_Raj-77CQuiflaKQQerwa1MSn56eO_AulW8X2QcC24Bb5RiBF_rjQdzNORfzTEhGmfdJoJeezyu-xQ'
URL = 'https://invest-public-api.tinkoff.ru/rest/tinkoff.public.invest.api.contract.v1.UsersService/GetAccounts'
headers = {'Authorization': f'Bearer {TOKEN}', 'accept': 'application/json', 'Content-Type': 'application/json'}

res = requests.request(method='POST', url=URL, headers=headers, json={})


pprint(res.json())