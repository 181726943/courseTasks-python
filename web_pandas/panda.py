import re

import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from selenium import webdriver

""" 请求页面 """
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
}  # 请求

url = "https://www.bilibili.com/video/av{}"

def craw(html,id):
    """ 解析页面 """
    soup = BeautifulSoup(html, "html.parser")
    #弹幕数量
    danmaku = re.search("\d+", str(soup.select("#viewbox_report > div > span.dm")[0]))      
    #播放量
    view = re.search("\d+", str(soup.select("#viewbox_report > div > span.view")[0]))           
    #投硬币数
    coin = re.search("\d+", str(soup.select("#arc_toolbar_report > div.ops > span.coin")[0]))    
    #包含收藏量的字符串
    collect = str(soup.select("#arc_toolbar_report > div.ops > span.collect")[0])                  
    collection = re.findall(r"</i>(.*?)</span>", collect, re.S)[0]          #收藏量
    #点赞数
    like = re.search("\d+", str(soup.select("#arc_toolbar_report > div.ops > span.like")[0]))       
    #包含分享数的原始字符串
    share = str(soup.select("#arc_toolbar_report > div.ops > span.share")[0])                     
    shared = re.findall(r'</i>(.*?)<!-- -->', share, re.S)[0]              #分享量

    # print (type(collection))  #查看collection的数据类型
    # print (type(shared))   #查看shared的数据类型

    #去除换行符空格
    collection = collection.replace('\r', '').replace('\n', '')   
    shared = shared.replace('\r', '').replace('\n', '')

    # print("弹幕数:",danmaku.group())
    # print("播放量",view.group())
    # print("投硬币数",coin.group())
    # print("点赞数",like.group())
    # print ("收藏量",collection)
    # print("分享量",shared)
    list = ["av"+str(id), view.group(), danmaku.group(), coin.group(), collection, like.group(),shared]
    print("执行craw函数")
    
    return list


if __name__ == "__main__":
    table = PrettyTable(['视频编号',  '播放量',  '弹幕',  '硬币',  '收藏',  '点赞',  '分享'])
    print ("开始爬取")
    id = int(input("输入视频编号："))
    num = int(input("输入爬取视频个数："))
    i = 1
    while(i <= num):
        # print("函数开始时",id)
        r = requests.get(url.format(id), headers=header)
        html = r.text
        # print (r.status_code)
        if r.status_code == 200:
            try:
                # print("craw函数使用前",id)
                data = craw(html, id)
                # print("craw函数使用后",id)
                table.add_row(data)
            except Exception as e:
                id += 1
                # print("捕获到异常时",id)
                continue
        else :
            break
        # print("正常执行时",id)
        id += 1
        # print("id加1后",id)
        i += 1
    print (table)
    print ("爬取完成")
