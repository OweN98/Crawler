from config import save_path, NEWS_NUM, THREADNUM
from path_manager import manage_path
from link_fetcher import fetch_links
from page_fetcher import fetch_page
from article_fetcher import fetch_article
from url_manager import form_url
from queue import Queue
from threading import Thread, current_thread
import json
import time
import random


class Craw():
    def __init__(self):
        self.fetch_article = fetch_article()
        self.fetch_links = fetch_links()
        self.fetch_page = fetch_page()
        self.k = 0
        self.total_sleep_time = 0
        self.total_expected = 0
        self.total_news = 0
        self.link_queue = Queue()
        self.thread_num = THREADNUM
    

    def parse2save(self, html, path, url):
        news_json = fetch_article.fetch(html)
        print('get %s, ready to parse2save\n' % url)
        try:
            #date = news_json['time'][:10]
            uri = news_json['uri'][14:]
        except Exception:
            return None
        with open(path + uri + '.json', 'w+', encoding='utf-8') as f:
            json.dump(news_json, f, indent=4, ensure_ascii=False)
        self.total_news += 1

    def craw(self, path):
        while not self.link_queue.empty():
            self.k += 1
            link = self.link_queue.get()
            print(current_thread)
            print('waiting for response of %s ' % link)
            html = fetch_page.sync_conn(link)
            self.parse2save(html, path, link)
            if self.k == 10:
                self.k = 0
                t = random.uniform(3.0,5.0)
                print('sleep %.2f s' % t)
                self.total_sleep_time += t
                time.sleep(t)
            if self.total_news == NEWS_NUM:
                return None


    def go_craw(self):
        print('start crwaling')
        urls = form_url()
        if urls:
            print('urls: ' + str(len(urls)))
        manage_path(save_path)
        for url in urls:
            new_links = fetch_links.fetch(fetch_page.sync_conn(url))
            self.total_expected += len(new_links)
            print(len(new_links))
            for link in new_links:
                self.link_queue.put(link)
        print('links OK')
        print(self.link_queue.qsize())

        ths = []
        for i in range(self.thread_num):
            thr = Thread(target=self.craw,args=(save_path,))
            thr.start()
            ths.append(thr)
        for th in ths:
            th.join()  
            
            
    
        
'''
    async def craw(self, url, path):
        with await(self.sem):
            async with aiohttp.ClientSession() as session:  
                html = await fetch_page.conn(session, url)
                print('waiting for response of %s' % url)
                self.parse2save(html, path, url)

    def go_craw(self):
        t1 = time.time()
        print('start crwaling')
        urls = form_url()
        manage_path(save_path)
        for url in urls:
            new_links = fetch_links.fetch(fetch_page.fetch(url))
            links = fetch_links.check_links(new_links)
            print('links OK')   
            loop = asyncio.get_event_loop()
            tasks = [self.craw(link, save_path) for link in links]
            loop.run_until_complete(asyncio.wait(tasks))
            loop.close()

        t2 = time.time()
        print('total time: %.2f s' % (t2-t1))
'''