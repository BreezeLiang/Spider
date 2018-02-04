# -*- coding:utf-8 -*-
import requests
from lxml import etree
import time


class Movie(object):
    def __init__(self):
        self.url = "http://www.ygdy8.net/html/gndy/dyzz/index.html"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

    def parse_url(self,url):
        r = requests.get(url=url,headers=self.headers)
        print(type(r.content))
        html = r.text # 字符串
        return html

    def get_movie(self,html):
        html = etree.HTML(html)
        movie_list = html.xpath("//div[@class='co_content8']/ul//table")
        # movie_list = []
        print(html)
        print(movie_list)
        for movie in movie_list:
            movie_name = movie.xpath("./tbody/tr[2]/td[2]/b//a/text()")
            print(movie_name)

        # next_url = "http://www.ygdy8.net/html/gndy/dyzz/" + html.xpath("//div[@class='co_content8']/div[@class='x']/a[@text='下一页']/@href")[0] if html.xpath("//div[@class='co_content8']/div[@class='x']/a[@text='下一页']/@href") is not None else None
        next_url = html.xpath("//div[@class='co_content8']/div[@class='x']/a[@text='下一页']/@href")
        # next_url = []
        print("7777")
        print(next_url)
        return movie_list,next_url

    def save_movie(self,movie_list):
        f = open("./movie.csv","a")
        for movie in movie_list:
            movie_name = movie.xpath("./tbody/tr[2]/td[2]/b/a/text（）")
            print(movie_name)
            f.write(movie_name)
        f.close()

    def run(self):
        url = self.url
        html = self.parse_url(url)
        print(html)
        # movie_list, next_url = self.get_movie(html)
        # # self.save_movie(movie_list)
        # # print(next_url)
        # while next_url:
        #     time.sleep(2)
        #     html = self.parse_url(next_url)
        #     movie_list, next_url = self.get_movie(html)
        #     self.save_movie(movie_list)
        #     print(next_url)
        # print("爬取结束！")

if __name__ == '__main__':
    spider = Movie()
    spider.run()



