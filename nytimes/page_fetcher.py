import requests
import threading
from config import USER_AGENTS
import random
import asyncio
import aiohttp
import re
class fetch_page():
    def __init__(self):
        self.url = None

    
    @staticmethod
    async def async_conn(session, url):
        headers = {
            'User-Agent': random.choice(USER_AGENTS)
        }

        async with session.request('GET', url, headers=headers, timeout=10) as response:
            if response.status_code == 200:
                return await response.text()


    @staticmethod
    def sync_conn(url):
        headers = {
            'User-Agent': random.choice(USER_AGENTS)
        }
        try:
            print('Current Thread Name %s, Url: %s ' % (threading.currentThread().name, url))
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                return response.text
 
        except Exception:
            print('ERROR fetching %s' % url)
            return None