'''
    form the list of urls to get content page
'''
import datetime
from settings import base_url, start_date, end_date

class url_build():
    def __init__(self):
        self.start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        self.cur = self.start + datetime.timedelta(days=-1)

    def build(self, cur):
        return base_url.format(cur.year, cur.month, cur.day)
        
    def next_url(self):
        if self.cur >= self.end:
            print('Over!!')
            return None, None
        self.cur += datetime.timedelta(days=1)
        url = self.build(self.cur)
        cur = datetime.datetime.strftime(self.cur, "%Y-%m-%d")
        return url, cur