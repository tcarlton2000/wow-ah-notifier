import os
import requests
from requests.auth import HTTPBasicAuth
from settings import get_client_id, get_client_secret, get_wanted_items


def get_token():
    client_id = get_client_id()
    client_secret = get_client_secret()

    basic = HTTPBasicAuth(client_id, client_secret)
    resp = requests.post('https://oauth.battle.net/token', data={ 'grant_type': 'client_credentials' }, auth=basic)
    return resp.json()['access_token']


def filter_items():
    all_items = get_commodities()
    return [(item['description'], all_items[item['id']]) for item in get_wanted_items()]


def best_price_items():
    all_items = get_commodities()
    return [(item['description'], all_items[item['id']]) for item in get_wanted_items() if all_items[item['id']] <= item['price']]


def get_commodities():
    token = get_token()

    url = 'https://us.api.blizzard.com/data/wow/auctions/commodities'
    params = {
        'namespace': 'dynamic-us',
        'region': 'us',
        'locale': 'en_US',
        'access_token': token
    }
    resp = requests.get(url, params=params)
    auctions = resp.json()['auctions']

    item_map = {}
    for auction in auctions:
        item_id = auction['item']['id']
        price = auction['unit_price']

        if item_id not in item_map:
            item_map[item_id] = price
            continue

        if price < item_map[item_id]:
            item_map[item_id] = price

    return item_map
    