import json

settings_file = open('settings.json')
settings = json.load(settings_file)


def get_client_id():
    return settings['wow_client_id']


def get_client_secret():
    return settings['wow_client_secret']


def get_discord_webhook():
    return settings['discord_webbook_url']


def get_wanted_items():
    return settings['wanted_items']
