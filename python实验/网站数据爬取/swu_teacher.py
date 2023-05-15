import requests
import re
import jieba
from urllib.request import urlopen

url = 'http://www.swu.edu.cn/xxgl_msfc.html'
respond = requests.get(url)
respond.encoding = 'gb2312'

# print(respond.text)

every_num = re.findall(r'<a href="xywh/msfc/(\w+).html" target="_blank">', respond.text)
file_name = re.findall(r'<td .*?><a .*?>(.*?)</a>',
                       respond.text)  # 获取   形如  "<a href="xywh/msfc/2.html" target="_blank">王　钊</a>" 的超链接   之间的中文内容，即获取名师姓名
add_name = re.findall(r'<td .*?><a .*?>(.*?)<a/>',
                      respond.text)  # "<a href="xywh/msfc/liming.html" target="_blank">李  明<a/>"    这一串中末尾是<a/>，与其他超链接不一样，需要另外添加
file_name.insert(11, '李  明')

img_name = file_name[:]  # 将file_name中的内容复制到img_name中

# print(every_num)
# print(name)

count = 1
name_count = 0  # 为了检索名师姓名

for man in every_num[:1000]:

    man_url = 'http://www.swu.edu.cn/xywh/msfc/{}.html'.format(man)
    man_respond = requests.get(man_url)
    man_respond.encoding = 'gb2312'

    # print(man_respond.text)
    # print(man,end="   ")

    text1 = re.findall('<div class="ct-body">(.*?)</div>', man_respond.text, re.S)  # 提取人物简介
    text2 = re.sub('<p>|<p >|&nbsp;|</p>|<.*?>', '', text1[0]).strip()  # 替换字符串中匹配项

    # 以下代码是为了解决HTML文档中中文标点符号问题
    text2 = text2.replace('&#8212', '-')
    text2 = text2.replace('&#8220', '“')
    text2 = text2.replace('&#8221', '”')
    text2 = text2.replace('&#8220；', '；“')
    text2 = text2.replace('&quot', '"')
    text2 = text2.replace('&#183', '·')

    # 打开一个.txt文档没，有的话就新建，并以相关人物的名字命名
    with open("swu_teachers\\" + file_name[name_count] + ".txt", mode='w', encoding="utf-8") as f:
        f.write('{}. '.format(count) + text2 + '\n')
        count += 1

    photo = r'<img .*? src="(.*?)" '
    result = re.findall(photo, text1[0], re.I)

    """  #获取相关名师的图片链接的末尾字符串
    形如<img width="161" height="209" src="24_wpsCA1C.tmp.png" align="left" hspace="12">.
    通过上面的表达式便可以得到  "24_wpsCA1C.tmp.png"   些内容，即关与图片链接的末尾，完整链接为
    http://www.swu.edu.cn/xywh/msfc/24_wpsCA1C.tmp.png，result 即为链接末尾部分，例如"24_wpsCA1C.tmp.png" """

    if result:
        picurl = r'http://www.swu.edu.cn/xywh/msfc/{0}'.format(result[0].replace(' ', r'%20'))  # 获得完整链接
        # 打开一个.png文件(即图片文件)，没有的话就新建，并以相关名师的名字命名
        with open("swu_teachers\\" + img_name[name_count] + ".png", 'wb') as fpic:
            fpic.write(urlopen(picurl).read())
    name_count += 1
