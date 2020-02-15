from article_fetcher import article_fetch
from link_fetcher import link_fetch
from url_builder import url_build
from path_builder import build_dir
import json
from random import randint
from time import sleep
class bbc_crawler(object):
    def __init__(self):
        self.url_build = url_build()
        self.link_fetch = link_fetch()
        self.article_fetch = article_fetch()
    
    @staticmethod
    def sleep_inter(count, upper):
        if count == upper:
            count = 0
            sleep_time = randint(4,6)
            print('sleeping...')
            sleep(sleep_time)
        else:
            count += 1

    def daily_crawler(self, url, date):
        dir = build_dir()
        links = link_fetch.fetch(self.link_fetch, url)
        print('crawling %s news, total number %d' % (str(date), len(links)))
        articles = []
        count = 0
        for link in links:
            #每请求5个页面等待
            self.sleep_inter(count, 5)
            print('crwaling %s', link)
            news_json = article_fetch.article_link2json(self.article_fetch, link, date)
            if news_json is not None:
                articles.append(news_json)
            else:
                print('null info...')

        with open(dir + '\\' + str(date) + '.json', 'w', encoding='utf-8') as f:
            json.dump(articles, f, indent=4)

    def go(self):
        while True:
            url, date = url_build.next_url(self.url_build)
            if url == None:
                print('finished')
                break
            self.daily_crawler(url, date)


                