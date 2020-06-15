#! python3
# -*- coding: utf-8 -*-
import os, codecs
import jieba
import wordcloud
from collections import Counter


import jieba

import wordcloud

# f = open("全球精灵时代.txt","r",encoding = "gbk")  #打开文件
# t = f.read()        #读取文件，并存好
# f.close()
# ls = jieba.lcut(t)        #对文本分词
# txt = " ".join(ls)        #对文本进行标点空格化
# w = wordcloud.WordCloud(font_path = "msyh.ttc",width = 1000,height = 700,background_color = "white")      #设置词云背景，找到字体路径（否则会乱码）
# w.generate(txt)     #生成词云
# w.to_file("wordcloud.png")    #保存词云图
def get_cloud():
    hack_mask = np.array(Image.open('./pkq.jpg'))
    fd = open("全球精灵时代.txt", "r", encoding="gbk")  # 打开文件
    t = fd.read()  # 读取文件，并存好
    fd.close()
    ls = jieba.lcut(t)  # 对文本分词
    txt = " ".join(ls)  # 对文本进行标点空格化
    w = wordcloud.WordCloud(font_path="msyh.ttc", width=500, height=333, background_color="white", mask=hack_mask,max_words=500, max_font_size=150)  # 设置词云背景
    w.generate(txt)  # 生成词云
    w.to_file("wordcloud.png")  # 保存词云图
    fd.close()

if __name__ == '__main__':
    with codecs.open('全球精灵时代.txt', 'r', 'gbk') as f:
        txt = f.read()
    get_cloud()
