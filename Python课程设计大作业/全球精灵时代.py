import urllib.request
import requests
import re
import os, codecs
import time
import jieba
import wordcloud
from collections import Counter
import numpy as np
from PIL import Image

#自定义请求头headers
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36'}
url = 'http://www.5323391.com/xs/0/300/'
response = requests.get(url,headers)  #通过requests发送get请求

#乱码，就修改编码方式。
response.encoding = 'gbk'

#网页源码
html = response.text
print(html)  #response.text（文本属性，取出网页的源码） 200代表正常


#小说的名字
title = re.findall(r'<h1>(.*?)</h1>',html)[0]
print(title)

#新建一个文件，保存小说内容
fb=open('%s.txt' %title,'w',encoding='gbk')


#获取每一章的信息（标题、章节、url）
div = re.findall(r'<div class="book_list">.*?</div>',html,re.S)[0]  #匹配不可见字符 re.S
chapter_info_list = re.findall(r'<a href="(.*?)"(.*?)</a>',div,re.S)  #补上




#新建一个文件，保存小说内容
#with open('%s.txt' %title) as f:



#循环每一个章节，分别去下载
for chapter_info in chapter_info_list:
    chapter_title = chapter_info[1]
    chapter_url = chapter_info[0]
    chapter_url="http://www.5323391.com/xs/0/300/%s" % chapter_url #尽量不要用+来拼字符，+号会增加新的对象，占内存


   # 下载章节内容，跟上面获取html是一样的，只不过变量不同
    chapter_response = requests.get(chapter_url) #
    chapter_response.encoding='gbk'
    chapter_html = chapter_response.text  #取出章节网页


   #提取章节网页的内容，再次用 正则表达式,
    chapter_content = re.findall(r'<div id="htmlContent" class="contentbox clear">(.*?)</div>',chapter_html,re.S)[0]


   #清洗数据，删除空格,nbsp,br
    chapter_content = chapter_content.replace(' ','')
    chapter_content = chapter_content.replace('&nbsp;','')
    chapter_content = chapter_content.replace('<br>','')
    chapter_content = chapter_content.replace('<br/>','')
    #chapter_content = chapter_content.replace('<p>','')
    #chapter_content = chapter_content.replace('</p>','')

   #持久化
    fb.write(chapter_title)
    fb.write(chapter_content)
    fb.write('\n')

    print(chapter_title,chapter_url) #每下完一章就打印一章
    #time.sleep(2)

fb.close()

def get_words(txt):
    fc = open('分词.txt', 'w', encoding='gbk')
    seg_list = jieba.cut(txt)   #对文本进行分词
    c = Counter()
    for x in seg_list:
        if len(x) > 1 and x != '\r\n':  #进行词频统计
            c[x] += 1
    print('常用词频度统计结果')
    for (k, v) in c.most_common(100):    #遍历输出高频词
        #print('%s%s %s  %d' % ('  ' * (5 - len(k)), k, '' * int(v / 3), v))
        print('%s %d' % (k,v))
    fc.writelines(str(c.most_common(100)))
    fc.close()

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
    get_words(txt)
    get_cloud()



