from config import start_date, end_date, base_url, USER_AGENTS
import requests
import re
from link_fetcher import fetch_links

def form_url():
    urls = []
    start_year = int(start_date[:4])
    start_month = int(start_date[-2:])
    end_year = int(end_date[:4])
    end_month = int(end_date[-2:])
    for year in range(start_year, end_year+1):
        url = base_url.format(year)
        res = requests.get(url)
        html = res.content
        links = fetch_links.fetch(html)
        if start_year == end_year:
            for link in links:
                cur_month = re.match(".*?_(\d\d)_.*?", link)               
                cur_month = int(cur_month[1])                
                if cur_month <= end_month and cur_month >= start_month:
                    url = base_url.format(link[1:])
                    urls.append(url[:-1])
        elif year == start_year:
            for link in links:
                cur_month = re.match(".*?_(\d\d)_.*?", link)
                if int(cur_month[1]) > start_month:
                    url = base_url.format(link[1:])
                    urls.append(url[:-1])
        elif year == end_year:
            for link in links:
                cur_month = re.match(".*?_(\d\d)_.*?", link)
                if int(cur_month[1]) < end_month:
                    url = base_url.format(link[1:])
                    urls.append(url[:-1])
        else:    
            urls.append(links)
        
    return urls
