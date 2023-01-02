import os
import requests

def post_content(content):
    url = os.environ.get('DISCORD_WEBHOOK_URL')
    data = {
        'content': content
    }
    requests.post(url, data=data)
