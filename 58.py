from bs4 import BeautifulSoup
import requests


def get_links_from(who_sells=0):
    urls = []
    list_view = 'http://sh.58.com/diannao/{}/'.format(str(who_sells))
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text,'lxml')
    for link in soup.select('td.t a.t'):
        href = link.get('href')
        print(href)
        urls.append(href)
    print(urls)
    return urls

# get_links_from()


def get_views_from(url):
    id = url.split('/')[-1].strip('x.shtml')
    api = 'http://jst1.58.com/counter?infoid={}'.format(id)
    js = requests.get(api)
    views = js.text.split('=')[-1]
    return views
    # print(views)


def get_item_info(who_sells):
    urls = get_links_from(who_sells)
    for url in urls:
        # print(url)
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        title = soup.title.text
        price = soup.select('#content span.price')
        time = soup.select('li.time')
        area = soup.select('.c_25d > a')
        # 转换
        list = []
        for r in area:
            list.append(r.text)
        area = list
        try:
            # print(area)
            # 构造数据结构
            data = {
                'title':title,
                'price':price[0].text,
                'date':time[0].text,
                'area':area,
                'cate':'个人' if who_sells == 0 else '商家',
                'views':get_views_from(url) if get_views_from(url) is not None else 0,
            }
            print(data)
        except:
            print("有异常！")

# url = 'http://sh.58.com/diannao/29696093514570x.shtml?adtype=1&PGTID=0d300023-0000-25a0-4395-4337efde3aca&entinfo=29696093514570_0&psid=195114284198773981486484100&iuType=_undefined&ClickID=2'
# get_item_info(url)
# get_views_from(url)

get_item_info(0)
