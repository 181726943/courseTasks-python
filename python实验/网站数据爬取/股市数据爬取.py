import requests
import json

cookies = {
    'st_si': '73343528210128',
    'qgqp_b_id': '825faa73fe957c26020c364c14bf79d5',
    'em_hq_fls': 'js',
    'HAList': 'f-0-000001-^%^u4E0A^%^u8BC1^%^u6307^%^u6570',
    'cowCookie': 'true',
    'cowminicookie': 'true',
    'waptgshowtime': '2020930',
    'st_asi': 'delete',
    'st_pvi': '33922399815878',
    'st_sp': '2020-09-29^%^2021^%^3A57^%^3A09',
    'st_inirUrl': 'https^%^3A^%^2F^%^2Fwww.eastmoney.com^%^2F',
    'st_sn': '59',
    'st_psi': '20200930105800985-111000300841-4604928350',
    'intellpositionL': '320px',
    'intellpositionT': '965px',
}

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63',
    'Accept': '*/*',
    'Referer': 'http://data.eastmoney.com/zjlx/detail.html',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

params = (
    ('pn', '1^'),
    ('pz', '50^'),
    ('po', '1^'),
    ('np', '1^'),
    ('ut', 'b2884a393a59ad64002292a3e90d46a5^'),
    ('fltt', '2^'),
    ('invt', '2^'),
    ('fid0', 'f4001^'),
    ('fid', 'f62^'),
    ('fs', 'm:0 t:6 f:^!2,m:0 t:13 f:^!2,m:0 t:80 f:^!2,m:1 t:2 f:^!2,m:1 t:23 f:^!2,m:0 t:7 f:^!2,m:1 t:3 f:^!2^'),
    ('stat', '1^'),
    ('fields', 'f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f165,f175,f84,f87,f204,f205,f124^'),
    ('rt', '53381158^'),
    #('cb', 'jQuery1830341427871747334_1601434750349^'),
    ('_', '1601434750797'),
)

response = requests.get('http://push2.eastmoney.com/api/qt/clist/get', headers=headers, params=params, cookies=cookies, verify=False)





print(response)







#数据清洗

resp_dict = json.loads(response.text)    #将response.text转化为字典

datas = resp_dict.get('data').get('diff')

companies = []
prices = []

for data in datas:
    #print(data)
    #公司名
    company = data.get('f14')

    #print(data)

    #流入量
    share_1 = data.get('f184')
    share_5 = data.get('f165')
    share_10 = data.get('f175')

    #股价
    price = data.get('f2')


    if share_1 >= 10 and share_5>=1 and  share_10 >= 1:
        companies.append(company)
        prices.append(price)


print(companies)
print(prices)






#数据可视化

from pyecharts.charts import Bar 
import pyecharts.options as opts


bar = Bar()
bar.add_xaxis(companies)
bar.add_yaxis("股价图",prices)


bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(
        axislabel_opts = opts.LabelOpts(rotate=-40)
    ),
    yaxis_opts=opts.AxisOpts(name="价格:(元/股)")

)

bar.render("股价图.html")
