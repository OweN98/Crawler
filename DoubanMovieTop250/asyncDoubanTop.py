import aiohttp
import time
import asyncio
import requests
import re
import json
import sqlite3
from lxml import etree
from requests.exceptions import RequestException

sem = asyncio.Semaphore(5)
htmls = []
def get_url():
    url = 'https://movie.douban.com/top250?start='
    urls = []
    for i in range(10):
        urls.append(url + str(i * 25))
    return urls

async def get_html(url):
    with await(sem):
        async with aiohttp.ClientSession() as session:
            async with session.request('GET', url) as res:
                html = await res.text()
                htmls.append(html)

def parse_page(html):
   
    pattern = re.compile('<li>.*?class="title">(.*?)</span>.*?<p\sclass="">(.*?)&nbsp;&nbsp;&nbsp;(.*?)<br>(.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?)</p>.*?property="v:average">(.*?)</span>.*?<span>(.*?)</span>.*?<span class="inq">(.*?)</span>.*?</li>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        print(item)
        yield{
            'name' : item[0],
            'director' : item[1].strip(),
            'actors' : item[2].strip(),
            'year' : item[3].strip(),
            'country' : item[4],
            'division' : item[5].strip(),
            'score' : item[6],
            'commentCount' : item[7],
            'description' : item[8]
        }

def write_to_file(content):
    with open('Async_doubanMovieTop250.txt', 'a', encoding = 'utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def write_to_db(content):
    conn = sqlite3.connect("\\Database\\DBMOVIE.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS DBMOVIE()")

def main():
    urls = get_url()
    loop = asyncio.get_event_loop()
    tasks = [get_html(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == '__main__':
    start = time.time()
    main()
    for html in htmls:
        for i in parse_page(html):
            #print(i)
            write_to_file(i)
    print('total time taken: %.5f s' % float(time.time() - start))

   


