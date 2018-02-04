# -*- coding:utf-8 -*-

# 分析
# 搜索首页url:
# https://s.taobao.com/search?q=python&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180105&ie=utf8
# 首页有12条数据是后来加载的

# 第二页url
# url_ = "https://s.taobao.com/search?data-key=s&data-value=44&ajax=true&_ksTS=1515160656339_835&callback=jsonp836&q=python&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180105&ie=utf8&bcoffset=4&ntoffset=0&p4ppushleft=1%2C48"

import time
import requests
import re
import json
from hashlib import md5
import xlwt


# 数据
DATA = []
# 时间
t = time.localtime()
# 搜索关键字
find_word = 'python'
# 参数
find_arg = {
    'q':find_word,
    'initiative_id': 'staobaoz_%s%02d%02d'%(t[0],t[1],t[2]),
}
# 表明身份
headers = {"Usr-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
# 搜索页面url
first_url = "https://s.taobao.com/search?imgfile=&js=1&stats_click=search_radio_all%3A1&ie=utf8"
# 启用代理Ip
proxies = {"https": "https://58.220.95.107:8080"}
# 发送请求
# url = "https://s.taobao.com/search?q=python&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306"
# r = requests.get(url,proxies=proxies,headers=headers)
a = 0
r = ''
html = ''
t = time.localtime()
print(t[5])
while a == 0:
    r = requests.get(first_url,params=find_arg,proxies=proxies,headers=headers)
    html = r.text
    if len(html) > 0 :
        t1 = time.localtime()
        print(t1[5])
        a = 1

# 分析找出信息
print(r)
print("开始****")
print(html)
content = re.findall(r'g_page_config = (.*?)g_srp_loadCss',html,re.S)[0][:-6]
# 转成字典
content = json.loads(content)
# 提取数据
data_list = content['mods']['itemlist']['data']['auctions']
for item in data_list:
    temp = {
        # 标题
        'title':item['title'],
        # 价格
        'view_price':item['view_price'],
        # 销量
        'view_sales':item['view_sales'],
        # 是否包邮
        'view_fee':'否' if float(item['view_fee']) else '是',
        'isTmall':'是' if item['shopcard']['isTmall'] else '否',
        'area':item['item_loc'],
        'name':item['nick'],
        'detail_url':item['detail_url'],
    }
    DATA.append(temp)

# 保存一下cookie
cookie_ = r.cookies

# 首页后面12条
ksts = str(int(time.time()*1000))
url2 = "https://s.taobao.com/api?_ksTS={}_226&callback=jsonp227&ajax=true&m=customized&stats_click=search_radio_all:1&q=python&s=36&imgfile=&initiative_id=staobaoz_20180105&bcoffset=0&js=1&ie=utf8&rn={}".format(ksts,md5(ksts.encode()).hexdigest())
# 再次发送请求
r2 = requests.get(url2,params=find_arg,cookies=cookie_)
html = r2.text
################
print(re.findall(r'{.*?}',html)[0])
print("9999999")
str = re.findall(r'{.*?}',html)
print(str)
print(type(str))
# 不是标准json，还是自己来吧
data_list = json.loads(str) #
################
# print(data_list)
# 提取数据
# for item in data_list:
#     temp = {
#         # 标题
#         'title':item['title'],
#         # 价格
#         'view_price':item['view_price'],
#         # 销量
#         'view_sales':item['view_sales'],
#         # 是否包邮
#         'view_fee':'否' if float(item['view_fee']) else '是',
#         'isTmall':'是' if item['shopcard']['isTmall'] else '否',
#         'area':item['item_loc'],
#         'name':item['nick'],
#         'detail_url':item['detail_url'],
#     }
#     DATA.append(temp)
#
# # 更新cookie
# cookie_ = r2.cookies
# # 爬取剩下的9页
# for i in range(1,10):
#     ktsts = time.time()
#     find_arg['_ksTS'] = "%s_%s" % (int(ktsts*1000),str(ktsts)[-3:])
#     find_arg['callback'] = "jsonp%d" % (int(str(ktsts)[-3:])+1)
#     find_arg['data-value'] = 44 * i
#     # 后面format没看到用处
#     url = "https://s.taobao.com/search?data-key=s&data-value=44&ajax=true&imgfile=&js=1&stats_click=search_radio_all%3A1&bcoffset=4&ntoffset=0&p4ppushleft=1%2C48".format(time.time())
#     if i > 1:
#         find_arg['s'] = 44 * (i - 1)
#     # params把data-value覆盖掉了
#     r3 = requests.get(url,params=find_arg,cookies=cookie_)
#     html = r3.text
#     # 转换为字典
#     data_list = json.loads(html)
#     # 提取数据
#     for item in data_list:
#         temp = {
#             # 标题
#             'title': item['title'],
#             # 价格
#             'view_price': item['view_price'],
#             # 销量
#             'view_sales': item['view_sales'],
#             # 是否包邮
#             'view_fee': '否' if float(item['view_fee']) else '是',
#             'isTmall': '是' if item['shopcard']['isTmall'] else '否',
#             'area': item['item_loc'],
#             'name': item['nick'],
#             'detail_url': item['detail_url'],
#         }
#         DATA.append(temp)
#     # 更新cookie
#     cookie_ = r3.cookies
#
# # 持久化 excel
# f = xlwt.Workbook(encoding='utf-8')
# sheet01 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
# # 写标题
# sheet01.write(0,0,'标题')
# sheet01.write(0,1,'标价')
# sheet01.write(0,2,'购买人数')
# sheet01.write(0,3,'是否包邮')
# sheet01.write(0,4,'是否天猫')
# sheet01.write(0,5,'地区')
# sheet01.write(0,6,'店名')
# sheet01.write(0,7,'url')
# # 写内容
# for i in range(len(DATA)):
#     sheet01.write(i+1,0,DATA[i]['title'])
#     sheet01.write(i+1,1,DATA[i]['view_price'])
#     sheet01.write(i+1,2,DATA[i]['view_sales'])
#     sheet01.write(i+1,3,DATA[i]['view_fee'])
#     sheet01.write(i+1,4,DATA[i]['isTmall'])
#     sheet01.write(i+1,5,DATA[i]['area'])
#     sheet01.write(i+1,6,DATA[i]['name'])
#     sheet01.write(i+1,7,DATA[i]['detail_url'])
#
# f.save(u'搜索%s的结果.xls' % find_word)

