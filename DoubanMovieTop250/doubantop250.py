import requests
import re
import json
import time
from requests.exceptions import RequestException

def get_page(url):
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
        }
        res = requests.get(url, headers = headers)
        if res.status_code == 200:
            return res.text
        return None
    except RequestException:
        print('RequestException')
        return None

def parse_page(html):
    pattern = re.compile('<li>.*?class="title">(.*?)</span>.*?<p\sclass="">(.*?)&nbsp;&nbsp;&nbsp;(.*?)<br>(.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?)</p>.*?property="v:average">(.*?)</span>.*?<span>(.*?)</span>.*?<span class="inq">(.*?)</span>.*?</li>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        #print(item)
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
    with open('doubanMovieTop250.txt', 'a', encoding = 'utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(offset):
    url = 'https://movie.douban.com/top250?start=0' + str(offset)
    html = get_page(url)
    for i in parse_page(html):
        print(i)
        write_to_file(i)

if __name__ == '__main__':
    start = time.time()
    for k in range(10):
        main(offset = k * 25)
    print('total time taken: %.5f s' % float(time.time() - start))