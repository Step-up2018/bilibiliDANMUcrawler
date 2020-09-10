from os import path

import numpy as np
from PIL import Image
from wordcloud import WordCloud, wordcloud
import matplotlib.pyplot as plt

import jieba
def makecloud(ch1,id):
    if ch1 == "AV号":
        text = open("av" + id + '.txt', 'r', encoding='UTF-8').read()
    else:
        text = open("BV" + id + '.txt', 'r', encoding='UTF-8').read()
    # 中文分词
    text = ' '.join(jieba.cut(text))
    # 生成对象
    wc = WordCloud(width=1600, height=1200,mode='RGBA', background_color=(255,255,255),).generate(text=text)
    # 显示词云
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    # 保存文件
    if ch1 == "AV号":
        wc.to_file("av" + id + '.png')
    else:
        wc.to_file("BV" + id + '.png')

