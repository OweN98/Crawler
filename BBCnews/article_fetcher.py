'''
    get articles by parsing pages
'''
from link_fetcher import link_fetch
from page_fetcher import page_fetch
from bs4 import BeautifulSoup
from goose3 import Goose
import json

class article_fetch(object):
    def __init__(self):
        #self.link_fetch = link_fetch()
        self.page_fetch = page_fetch()

    def get_title(self, soup):
        return soup.title.get_text()

    def get_date(self, date):
        return date
        #return date.strftime('%Y-%m-%d')

    def get_authors(self, soup):
        authors_elements = soup.find_all('meta', property='article:author')
        return [authors_element['content'] for authors_element in authors_elements]

    def get_description(self, soup):
        description_element = soup.find('meta', property='og:description')
        return description_element['content']

    def get_section(self, soup):
        section_element = soup.find('meta', property='article:section')
        return section_element['content']

    def get_content(self, html):
        g = Goose({'enable_image_fetching': False})
        article = g.extract(raw_html=html)
        return article.cleaned_text
    
    def article_link2json(self, link, date):

        html = self.page_fetch.fetch(link)
        if html is None:
            return None
        #print(html)
        soup = BeautifulSoup(html, 'lxml')
        head = soup.head

        try:
            title = self.get_title(head)
            date = self.get_date(date)
            authors = self.get_authors(head)
            description = self.get_description(head)
            section = self.get_section(head)
            content = self.get_content(html)
            real_content = content.replace('\n', '')
        except Exception as e:
            #raise e
            return None

        return{
            'title': title,
            'link': link,
            'date': date,
            'authors': authors,
            'description': description,
            'section': section,
            'content': real_content
        }



    