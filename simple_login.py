# -*- coding:utf-8 -*-
import requests


url = 'http://www.zhongdengwang.org.cn/rs/main.do'
cookies = {'Cookie':'JSESSIONID=235473429.20480.0000; BIGipServerpool_zdw_www=QOWQHsGleq/DQE5Kei6fpzeg/uZ0PoVWxdaaY42pXSVoZJ4IR+GmQVrz2fIlRZLRy18AJP1jXYuNUw==; BIGipServerpool_rs=eeIqw2bYHaKjhmdbgfFJe/GX0Jl48NZMctMWw+H2j75T1CiQKeVzZdZKT9fvb/OwcvtKkZfVS7BgeTE=; RSOUT=H4czhjCFqhjS69k9hBfdXlC1nlspvHMwrrMtNtMZLwJBkjpY3XYB!1021273420'}


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
r = requests.get(url=url,headers=headers,cookies=cookies)
html = r.text
print("66666666")
print(html)