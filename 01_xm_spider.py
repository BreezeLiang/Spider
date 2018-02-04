import requests
import re
import time
import urllib  # 用来获取音频


header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

for n in range(1,2):
    # 一个page内容
    url = 'http://www.ximalaya.com/4932085/album/3160816?page={}'.format(n)
    # print(url)
    html = requests.get(url,headers=header)
    # print(html.status_code)
    str = html.text
    data = re.findall(r'href="/4932085/sound/(\d+?)/"',str)
    # 获取page内每个片段的连接
    print(data)
    for m in set(data[0:1]):
        # 获取每片段json的url
        urls = 'http://www.ximalaya.com/tracks/{}.json'.format(m)
        print(urls)
        # 获取json文件
        html2 = requests.get(url=urls,headers=header)
        # print(html2.text)
        # json文件，可以用json的格式获取音频字段的连接
        print(html2.json())
        m4a = html2.json()['play_path_64']
        # urllib缺少对应模块
        urllib.request.urlretrieve(m4a,'C:\\Users\\Breeze\\Desktop\\喜马拉雅\\'+m+'.m4a') # 用来保存音频
        time.sleep(2)

