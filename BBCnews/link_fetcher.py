'''
    get news article links in single day from content pages
'''
from page_fetcher import page_fetch
from settings import RETRY_TIME, start_date, end_date
from lxml import etree
import re
class link_fetch(object):
    def __init__(self):
        self.page_fetcher = page_fetch()
        #self.url_builder = url_build(start_date, end_date)

    def html2link(self, html):
        link_html = etree.HTML(html)
        h1 = link_html.xpath('//h1//text()')
        #some pages may be lost, so skip them
        if h1[0] == 'Page not found':
            print('skip the page')
            return []
        else:
            links = link_html.xpath('//tr[@class="row0"]//@href')
            real_links = []
            #get real link to news article page, not category page
            for link in links:
                l = re.match('.*?(\d+)', link)
                if l is not None:
                    real_links.append(link)
            return real_links

    def fetch(self, url):
        print('fetching daily links %s ' % url)
        html = self.page_fetcher.fetch(url) 
        if html is None or len(html) == 0:
            print('fetch daily link %s failed' % url)
            return []
        links = self.html2link(html)
        return links

    