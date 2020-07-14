'''
    MovieCommentCrawler.py
    功能：爬取电影评论
'''
import requests, time
from lxml import etree
from settings import USER_AGENTS, COMMENTS_PAGES_NUM
from NowplayingMovieCrawler import HtmlDownloader
from threading import current_thread
def UrlManager(NowPlayingEntity):
    urls = []
    # 根据网页url的特点组织url数组
    base_url = 'https://movie.douban.com/subject/'+ NowPlayingEntity['id']+'/comments?start={}&limit-20'
    for i in range(COMMENTS_PAGES_NUM):
        # 组成前10页评论的url
        comment_url = base_url.format(i * 20)
        urls.append(comment_url)
    return urls

# 解析出评论
def CommentListHtmlparser(html):
    try:
        html = etree.HTML(html)
        # 根据HTML源代码特点编写解析评论的XPath表达式
        eachCommentList = html.xpath('//div[@class="comment-item"]//div[@class="comment"]//span[@class="short"]/text()')
    except Exception as e:
        print('get comments page error!')
        print(e)
        exit(0)

    return eachCommentList

# 获取评论爬虫调度器
def CommentListSchedular(NowPlayingEntity):
    urls = UrlManager(NowPlayingEntity)
    print('thread ' + str(current_thread().ident) + ' is feteching ' + NowPlayingEntity['name'] + '\'s comments......')
    # 将获取的评论进行组合
    eachCommentList = []
    for url in urls:
        html = HtmlDownloader(url)
        eachCommentList.append(CommentListHtmlparser(html))
        # time.sleep(0.3)
    print(NowPlayingEntity['name'] + '\'s Comments are ready to process...')
    return eachCommentList