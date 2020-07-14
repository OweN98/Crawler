'''
    WordCloud.py
    功能：生成词云
'''
import matplotlib.pyplot as plt
import matplotlib
from wordcloud import WordCloud, ImageColorGenerator
from settings import BG_PATH
import numpy as np
from PIL import Image

def WordCloudGenerator(keywords, name):
# 显示图像的最大范围
    matplotlib.rcParams['figure.figsize']=(20.0,10.0)
# 读取背景图
    bg_pic=np.array(Image.open(BG_PATH))
# 停用词设置
    stop_words=[]
    for line in open('stopwords', 'r', encoding='utf-8'):
        stop_words.append(line.rstrip('\n'))
    keywords={x:keywords[x] for x in keywords if x not in stop_words}
    # print('删除停用词后',keywords)

    wordcloud=WordCloud(
        font_path='simhei.ttf',
        background_color='white',
        mask=bg_pic,
        max_font_size=80,
        stopwords=stop_words
    )
    word_frequence=keywords
    myword=wordcloud.fit_words(word_frequence)
    image_colors=ImageColorGenerator(bg_pic)
    # 展示云图
    # plt.imshow(myword)
    # plt.axis('off')
    
    # plt.show()
    wordcloud.to_file(name + '-wordcloud.jpg')
