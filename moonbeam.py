from requests import Request, Session
import requests
import json
from requests.structures import CaseInsensitiveDict
from Coinmarketcap import *
def get_moonbeam_price(address):
    slug = "6836"
    moonbeam_price = getprice(slug)
    moonbeam_value = 10**18
    URL = "https://moonbeam.api.subscan.io/api/scan/account/tokens"
    headers = {
    'Content-Type': 'application/json',
    'X-API-Key': 'e7e864a7bed146fca9db9bba7965148d',
    }

    json_data = {
        'address': address,
    }

    response = requests.post(URL, headers=headers, json=json_data)
    value = response.json()["data"]["native"][0]["balance"]
    value = (float(value) / moonbeam_value) * moonbeam_price
    return value
def get_moonbeam_tokens(address):
    moonbeam_value = 10**18
    URL = "https://moonbeam.api.subscan.io/api/scan/account/tokens"
    headers = {
    'Content-Type': 'application/json',
    'X-API-Key': 'e7e864a7bed146fca9db9bba7965148d',
    }

    json_data = {
        'address': address,
    }

    response = requests.post(URL, headers=headers, json=json_data)
    value = response.json()["data"]["native"][0]["balance"]
    value = (float(value) / moonbeam_value)
    return value


    
    
