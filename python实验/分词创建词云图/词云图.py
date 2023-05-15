import jieba
from wordcloud import WordCloud
import jieba.analyse
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt#绘制图像的模块

font = r'C:\Windows\Fonts\simsun.ttc'#电脑自带的字体

#jieba分词统计
with open("思考，快与慢.txt", 'r',encoding = 'GBK') as f:
    texts = f.read()  # 读取整个文件作为一个字符串
    #result = jieba.analyse.textrank(texts,topK=100, withWeight=False)  # textrank算法排序
    #result = jieba.analyse.extract_tags(sentence=texts,topk = 100, withWeight=False)  # tfidf考虑权重
    #print(result)
    #string = str(result)
    wordcut = jieba.cut(texts)  #分词
    string = " ".join(wordcut)  #将切分的词转化为字符串

#绘制词云图
img = Image.open('brain.png')   #打开图片
img_array = np.array(img)   #将图片转化为数组
stopword=['']  #设置停止词，也就是你不想显示的词
wc = WordCloud(
    background_color = 'white',
    width=1000,
    height=800,
    mask = img_array, #设置背景图片
    font_path=font,
    stopwords=stopword
).generate(string)#绘制图片
#wc.generate_from_text(string)#绘制图片
plt.imshow(wc)
plt.axis('off')#隐藏坐标轴
#plt.show()  #显示图片
wc.to_file('braincloud.jpg')  #保存图片