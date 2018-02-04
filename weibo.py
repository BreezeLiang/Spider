# -*- coding:utf-8 -*-
# 微博爬取评论
import requests
import pandas
import time


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
Cookie = {'Cookie':'_T_WM=07507c320e967b5d786d0f0a2eccc76b; ALF=1518441604; SCF=AuPPd_NDpic1yqJyzVpKKA6Mm7R3Sqdq1M_is1C9CA9D-HMviPIrVEFE0hhpbZ79Zo06X0E4va-GPj_FZyKnw4M.; SUB=_2A253Xn7VDeThGeBN6FEX8yzOyTuIHXVUoQKdrDV6PUJbktBeLRb1kW1NRJXYs51fNOsJppkqVLb4TZQYiUHbCg9E; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW3wdI8T3BsW6LD_JMOHUJI5JpX5K-hUgL.Foq0e0ece0zEeoM2dJLoIpYLxK-L12BL1K-LxKMLBo2LB.zLxKqLBo2LB.x4Soxc; SUHB=0A0ZQ9jhx5wL4X; H5_INDEX=0_all; H5_INDEX_TITLE=%E5%8D%95%E7%B1%BB%E6%B1%BDy64v; WEIBOCN_FROM=1110006030; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D3%2526q%253D%25E6%259D%258E%25E5%25B0%258F%25E7%2592%2590%26featurecode%3D20000320%26fid%3D1076031191044977%26uicode%3D10000011'}
url = 'https://m.weibo.cn/api/comments/show?id=4191091647728210&page=1'

html = requests.get(url,headers=headers,cookies=Cookie)
print(html.status_code)
print("*"*36)
li = 1
while html.status_code == 200:
    if html.json()['ok'] == 0:
        break
    try:
        for jj in range(len(html.json()['data']['data'])):
            data1 = [(html.json()['data']['data'][jj]['user']['screen_name'],
                     html.json()['data']['data'][jj]['created_at'],
                     html.json()['data']['data'][jj]['source'],
                     html.json()['data']['data'][jj]['user']['id'],
                     html.json()['data']['data'][jj]['user']['profile_url'],
                     html.json()['data']['data'][jj]['user']['profile_image_url'],
                     html.json()['data']['data'][jj]['text'])]
            data2 = pandas.DataFrame(data1)
            data2.to_csv('C:\\Users\\Breeze\\Desktop\\data\\weibo.csv', header=False, index=False, mode='a+')
    except:
        li -= 1
    time.sleep(2)
    li += 1
    print("*"*20,li,"*"*20)
    url_next = 'https://m.weibo.cn/api/comments/show?id=4191091647728210&page=' + str(li)
    html = requests.get(url=url_next, headers=headers, cookies=Cookie)

print("结束爬取！")

