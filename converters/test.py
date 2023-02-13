from requests import Request, Session
import json
import pprint
def getethprice():
    URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"

    parameters = {
        "sort": "cmc_rank"
    }
    
    headers = {
        "accept": "application/json",
        "X-CMC_PRO_API_KEY": "6e387c03-e3c7-431f-b088-422f0da42278"
    }
    session = Session()
    session.headers.update(headers)

    response = session.get(URL, params=parameters)
    value = response.json()
    return value
print(getethprice())
    

