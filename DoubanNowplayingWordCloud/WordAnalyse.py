'''
    WordAnalyse.py
    功能：数据清洗，分词
'''

import re
import jieba.analyse

def CleanComments(eachCommentList):
    comments=''
    for k in range(len(eachCommentList)):
        comments+=(str(eachCommentList[k])).strip()
    pattern=re.compile(r'[\u4e00-\u9fa5]')
    filterdata=re.findall(pattern,comments)
    cleaned_comments=''.join(filterdata)
    # print(cleaned_comments)
    return cleaned_comments

def WordSegmentation(comments):
    result=jieba.analyse.textrank(comments,topK=200,withWeight=True)
    keywords=dict()
    for i in result:
        keywords[i[0]]=i[1]
    return keywords

