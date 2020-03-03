from Crawler import Craw
from config import save_path, start_date, end_date, sec2minsec
import time
if __name__ == '__main__':
    nytCrawler = Craw()
    t1 = time.time()
    nytCrawler.go_craw()
    t2 = time.time()
    t = t2 - t1 - nytCrawler.total_sleep_time
    min, sec = sec2minsec(t)
    print('Crwaler successfully fetched %d articles' % nytCrawler.total_news)
    print('total time: %.2f' % t)
    with open(save_path + 'result.txt', 'w', encoding='utf-8') as f:
        f.write('from %d links\n Successfully fetched %d articles\n from %s to %s \n total time: %d min %.2f sec \n efficiency: %.2f articles per sec' % (nytCrawler.total_expected, nytCrawler.total_news, start_date,end_date, min, sec, nytCrawler.total_news/t))