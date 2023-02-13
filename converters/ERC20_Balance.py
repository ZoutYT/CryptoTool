from requests import get
# from bs4 import BeautifulSoup
# from flask import Flask
# from flask import request
# from flask import send_file
from requests import Request, Session
import json
import pprint
from Coinmarketcap import *
from polkadot import *
import requests
import json
from requests.structures import CaseInsensitiveDict
# app = Flask(__name__)
def get_eth_price(address, slug):
    API_KEY_ERC20 = "VFQD2DD2SHUEFWSPUKBKI5ZHUAN5N58UJV" 

    ETH_PRICE = getethprice(slug)

    Ether_value = 10 ** 18
    BASE_URL = "https://api.etherscan.io/api"

    def make_api_url(module, action, address, **kwargs):
        url = BASE_URL + f"?module={module}&action={action}&address={address}&apikey={API_KEY_ERC20}"
        
        for key, value in kwargs.items():
            url += f"&{key}={value}"

        return url
    def get_account_balance(address):
        get_balance_url = make_api_url("account", "balance", address, tag="latest")
        response = get(get_balance_url)
        data = response.json()

        value = int(data["result"]) / Ether_value
        return value

    eth = get_account_balance(address)
    ethprice = eth * ETH_PRICE
    print(ethprice)
