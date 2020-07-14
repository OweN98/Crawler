'''
    run.py
    功能：总调度器
'''
from MovieCommentCrawler import CommentListSchedular
from WordAnalyse import WordSegmentation, CleanComments
from NowplayingMovieCrawler import NowplayingMovieCrawler_Schedular
from WordCloud import WordCloudGenerator
from threading import Thread
from queue import Queue
from settings import THREAD_NUM
import time
def go(MovieQueue):
    # 当电影队列非空
    while not MovieQueue.empty():
        # 获取队列中的单个电影实体
        NowPlayingEntity = MovieQueue.get()

        # 对于每一部电影获取评论
        eachCommentList = CommentListSchedular(NowPlayingEntity)
        
        # 评论清洗
        cleaned_comments = CleanComments(eachCommentList)
        
        # 分词
        keywords = WordSegmentation(cleaned_comments)
        
        # 生成词云
        WordCloudGenerator(keywords, NowPlayingEntity['name'])

if __name__ == '__main__':
    t1 = time.time()
    # 获取正在上映电影的id和名字
    NowPlayingList = NowplayingMovieCrawler_Schedular()

    # 将电影实体存入队列
    MovieQueue = Queue()
    for NowPlayingEntity in NowPlayingList:
        MovieQueue.put(NowPlayingEntity)
    
    # 开启多线程
    ths = []
    for i in range(THREAD_NUM):
        thr = Thread(target=go,args=(MovieQueue,))
        thr.start()
        ths.append(thr)
    for th in ths:
        th.join()  

    t2 = time.time()
    print('Finished! Total time: %.2f s' % (t2-t1))