import jieba
from collections import Counter
def get_words(txt):
    fb=open('分词.txt','w',encoding='gbk')
    seg_list = jieba.cut(txt)   #对文本进行分词
    c = Counter()
    for x in seg_list:
        if len(x) > 1 and x != '\r\n':  #进行词频统计
            c[x] += 1
    print('常用词频度统计结果')
    for (k, v) in c.most_common(100):    #遍历输出高频词
        #print('%s%s %s  %d' % ('  ' * (5 - len(k)), k, '' * int(v / 3), v))
        print('%s %d' % (k,v))
    fb.writelines(str(c.most_common(100)))
if __name__ == '__main__':
    with open('全球精灵时代.txt', 'r') as f:
        txt = f.read()
    get_words(txt)