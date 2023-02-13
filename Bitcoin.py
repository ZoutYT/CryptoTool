from Coinmarketcap import *
from polkadot import *
import requests
from requests import get
import json
from requests.structures import CaseInsensitiveDict
# app = Flask(__name__)
def get_btc_price(address,slug):
    slug = "1"
    Bitcoin_price = getprice(slug)
    Bitcoin_amount = 10**8
    BASE_URL = "https://blockchain.info/balance?active="
    url = BASE_URL + address
    session = Session()
    response = session.get(url)
    value = response.json()[address]["final_balance"]
    value = (value / Bitcoin_amount) * Bitcoin_price
    return value

def get_btc_amount(address):
    slug = "1"
    Bitcoin_amount = 10**8
    BASE_URL = "https://blockchain.info/balance?active="
    url = BASE_URL + address
    session = Session()
    response = session.get(url)
    amount = response.json()[address]["final_balance"]
    amount = (amount / Bitcoin_amount)
    return amount



