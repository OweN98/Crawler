'''
    get page's html from single url
'''
from settings import USER_AGENTS
import requests
from requests.exceptions import ConnectionError
import random

class page_fetch(object):
    def __init__(self):
        self.url = None

    def fetch(self, url):
        headers = {
            'User-Agent': random.choice(USER_AGENTS)
        }
        try:
            response = requests.get(url, headers = headers)
            if response.status_code == 200:
                print('fetch_page %s OJBK' % url)
                #print(response.text)
                return response.text
        except Exception:
            print('requests %s Failed' % url)
            return None