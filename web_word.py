from bs4 import BeautifulSoup
import requests
from wordcloud import WordCloud
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt#绘制图像的模块
import jieba

if __name__ == "__main__":
    font = r'C:\Windows\Fonts\simsun.ttc'#电脑自带的字体
    url = "https://news.sina.cn/gn?vt=4"
    r = requests.get(url)
    r.encoding = "utf-8"
    html = r.text
    soup = BeautifulSoup(html,"html.parser")
    # word = soup.select('#j_nav56261_list > section:nth-child(1) > a > aside > h2')
    texts = soup.find_all('h2',attrs={"class":"m_f_con_t cm_tit"})
    # text = texts[0].get_text()
    # print(text)
    # print(texts[0],type(texts[0]))
    # print(word,type(word))
    num = len(texts)
    # 爬取web标题
    # for i in range(0,num ):
    #     text = texts[i].get_text()
    #     with open ("title_word.txt",mode='a+',encoding="utf-8") as f:
    #         f.write(text+"\n")
# jieba分词
    with open ("title_word.txt",mode="r",encoding="utf-8") as f:
        word = f.read()
        wordcut = jieba.cut(word)   #分词
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