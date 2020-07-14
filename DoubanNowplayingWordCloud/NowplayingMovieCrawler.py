'''
    NowplayingMovieCrawler.py
    功能：获取正在上映电影的id和名字
'''
import requests, random
from lxml import etree
from settings import USER_AGENTS, NOW_PLAYING_URL

# 从settings中获取正在上映电影的url
def UrlManager():
    url = NOW_PLAYING_URL
    return url

# 解析网页为HTML源代码
def HtmlDownloader(url):
    try:
        res = requests.get(url, headers = {
            'User-Agent':random.choice(USER_AGENTS)
        })
        # headers中设置用户代理为用户代理池中的随机一个
        if res.status_code == 200:
            # 当获取成功时返回状态码200
            return res.text
        return None
    except Exception as e:
        print(e)
        return None

def Htmlparser(html):
    movie_list = []
    try:
        html = etree.HTML(html)
        # 构造XPath解析对象并对HTML文本进行自动修正
    except Exception as e:
        raise(e)
        print('can\'t get nowplaying page')
        print(e)
        exit(0)
    
    # 分析网页的HTML源代码结构，编写XPath表达式，返回符合结果的内容合并为的数组
    NowplayingPart_id = html.xpath('//div[@id="nowplaying"]//div[@class="mod-bd"]//ul[@class="lists"]/li')
    
    # 获取单个电影的id和名字
    for i in NowplayingPart_id:
        movie_id = i.xpath('./@id')
        movie_name = i.xpath('./@data-title')
        movie_entity = {
                'id': movie_id[0],
                'name' : movie_name[0]
        }
        movie_list.append(movie_entity)
    return movie_list

# 获取正在上映电影爬虫调度器
def NowplayingMovieCrawler_Schedular():
    url = UrlManager()
    html = HtmlDownloader(url)
    NowPlayingList = Htmlparser(html)
    print('近期正在上映的电影有')
    for i in NowPlayingList:
        print(i['name'])
    print('\n')
    return NowPlayingList
