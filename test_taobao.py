# -*- coding:utf-8 -*-
import requests
import time


url = "https://s.taobao.com/search?q=python&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
proxies = {"https": "https://58.220.95.107:8080"}

while True:
    r = requests.get(url, proxies=proxies, headers=headers)
    length = len(r.text)
    print("11111111")
    if length != 0:
        t = time.time()
        print(t)
        print("开始计数！")
        a = 0
        while a == 0:
            r1 = requests.get(url, proxies=proxies, headers=headers)
            t1 = time.time()
            length = len(r1.text)
            print("222222222")
            if length != 0 :
                print(r1.text)
                print("啦啦啦啦")
                print(t1 - t)
                print(r1.cookies)
                a = 1
        print("33333333")
        break




