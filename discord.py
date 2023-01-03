import os
import requests
from settings import get_discord_webhook


def format_price(price):
    copper = price % 100
    silver = int(price / 100) % 100
    gold = int(price / 10000)
    return f'{gold}g {silver}s {copper}c'


def create_message(items):
    message = 'The below items are less than your requested price:\n'
    for item in items:
        message += f'\n{item[0]}: {format_price(item[1])}'

    return message


def post_content(items):
    if len(items) == 0:
        return

    url = get_discord_webhook()
    data = {
        'content': create_message(items)
    }
    requests.post(url, data=data)
