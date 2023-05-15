import requests
import re
import jieba
from urllib.request import urlopen
from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.swu.edu.cn/xxgl_msfc.html'
respond = requests.get(url)
respond.encoding = 'gb2312'

print(respond.text)

every_num = re.findall(r'<a href="xywh/msfc/(\w+).html" target="_blank">', respond.text)
name = re.findall(r'<td .*?><a .*?>(.*?)</a>', respond.text)
add_name = re.findall(r'<td .*?><a .*?>(.*?)<a/>', respond.text)
name.insert(11,'李  明')

#print(every_num)
#print(name)
#print(len(name))



count = 0

for man in every_num[:1000]:

    man_url = 'http://www.swu.edu.cn/xywh/msfc/{}.html'.format(man)
    man_respond = requests.get(man_url)
    man_respond.encoding = 'gb2312'

    #print(man_respond.text)
    #print(man,end="   ")

    text1 = re.findall('<div class="ct-body">(.*?)</div>', man_respond.text, re.S)
    text2 = re.sub(r'<p>|<p >|&nbsp;|</p>|<.*?>', '', text1[0]).strip()
    text2 = text2.replace('&#8212','-')
    text2 = text2.replace('&#8220','“')
    text2 = text2.replace('&#8221','”')
    text2 = text2.replace('&#8220；','；“')
    text2 = text2.replace('&quot','"')
    text2 = text2.replace('&#183','·')
    #text3 = re.sub(r'<.*?>','',text2)

    count += 1
    print("text",count,":", text2)
    #print("\n\n")


    #photo = r'<img .*? src="(.*?)" '
    #result = re.findall(photo, text1[0], re.I)


#print(result)