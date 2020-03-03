from lxml import etree
import asyncio
class fetch_article():
    def __init__(self):
        self.html = None
    
    @staticmethod
    def fetch(html):
        try:
            html = etree.HTML(html)
            paragraph = html.xpath('//p//text()')
            content = ''.join(paragraph[5:-1])
            time = html.xpath('//head//meta[@property="article:published"]/@content')
            section = html.xpath('//head//meta[@property="article:section"]/@content')
            description = html.xpath('//head//meta[@name="description"]/@content')
            tag = html.xpath('//head//meta[@property="article:tag"]/@content')
            title = html.xpath('//title/text()')
            authors = html.xpath('//head//meta[@name="byl"]/@content')
            link = html.xpath('//head//meta[@property="og:url"]/@content')
            uri = html.xpath('//head//meta[@name="nyt_uri"]/@content')
        except Exception:
            return None
        try:
            item = {
                'title': title[0],
                'link': link[0],
                'time': time[0],
                'authors': authors,
                'description': description[0],
                'section' : section[0],
                'tag': tag,
                'content': content,
                'uri' : uri[0]
            }
            return item
        except Exception:
            print('item fail')
            return None
        
