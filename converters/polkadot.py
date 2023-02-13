from requests import Request, Session
import requests
import json
from requests.structures import CaseInsensitiveDict
def get_polk_tokens(address):
    Dot_Value = 10**10
    URL = "https://polkadot.api.subscan.io/api/scan/account/tokens"
    headers = {
    'Content-Type': 'application/json',
    'X-API-Key': 'e7e864a7bed146fca9db9bba7965148d',
    }

    json_data = {
        'address': address,
    }

    response = requests.post(URL, headers=headers, json=json_data)
    value = response.json()["data"]["native"][0]["balance"]
    Value_dot = float(value) / Dot_Value
    print(Value_dot)
    
    
