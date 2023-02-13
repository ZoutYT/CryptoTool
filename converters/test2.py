from requests import Request, Session
import json
import pprint
BASE_URL = "https://blockchain.info/balance?active="
address = "16rCmCmbuWDhPjWTrpQGaU3EPdZF7MTdUk"
url = BASE_URL + address
session = Session()
response = session.get(url)
value = response.json()[address]["final_balance"]
print(value)