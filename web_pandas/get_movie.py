import requests
from win32com.client import Dispatch
from bs4 import BeautifulSoup

# thunder = Dispatch('ThunderAgent.Agent64.1')
page_url = 'https://www.dydytt.net/html/gndy/dyzz/list_23_{}.html'
host = 'https://www.dydytt.net/'

header = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cookie':'XLA_CI=c078afe1ea64185bb655f2a9c0c356de; cscpvrich5041_fidx=4',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44'
    }

# 获取网页内容
def get_page(url):
    r = requests.get(url,headers=header)
    r.encoding = "gb2312"
    html = r.text
    return html

# 获取电影列表页面所有电影的信息(包含详情页面链接和电影名称)
def get_info(html):
    soup = BeautifulSoup(html,"html.parser")
    url_all = soup.find_all('a',attrs={'class':'ulink'})
    return url_all

# 获取电影名称
def get_name(url_a):
    soup = BeautifulSoup(str(url_a),"html.parser")
    name = soup.get_text()
    return name

# 获取下载链接的函数
def get_download(url):
    page_html = get_page(url)
    soup = BeautifulSoup(page_html,"html.parser")
    download_url = soup.find('a',attrs={'target':'_blank'})
    url = download_url.get("href")
    return url

if __name__ == "__main__":
    pages = int(input("请输入爬取页数:"))
    for i in range(1,pages+1):
        print("---当前开始爬取第"+str(i)+"页---")
        counter = 1
        list_url = page_url.format(str(i))   # 拼接电影列表页面链接
        page_html = get_page(list_url)   # 获取网页内容
        url_all = get_info(page_html)  # 获取电影列表页面信息
        for url_i in url_all:
            movie_name = get_name(url_i)
            url_i = url_i.get('href')
            movie_url = host + url_i
            download_url = get_download(movie_url)
            # thunder.AddTask(download_url,movie_name,r'D:\movies')
            # thunder.CommitTasks()
            with open ("movie_url.txt",mode='a+',encoding='gb2312') as movie:
                movie.write(str(counter)+"."+movie_name+":"+download_url+"\n")
                counter += 1
    print("----------爬取完成----------")

