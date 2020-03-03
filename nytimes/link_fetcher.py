from lxml import etree
import re

class fetch_links():
    def __init__(self):
        pass
    
    @staticmethod
    def fetch(html):
        ht = str(html)
        link_html = etree.HTML(ht)
        links = link_html.xpath('//div[@id="mainContent"]//li//a/@href')
        if links:
            return links
        else:
            return None
    @staticmethod
    def check_links(links):

        news_links = []
        for link in links:
            u = re.match("(.*?)//www.nytimes.com/(.*?)", link)
            if u:
                news_links.append(link)
            return news_links