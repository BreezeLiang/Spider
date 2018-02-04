# -*- coding:utf-8 -*-
import yundama
import requests
from lxml import etree


class login(object):
    def __init__(self):
        self.login_url = "http://www.zhongdengwang.org.cn/rs/main.jsp"
        self.user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

    # 初始登录
    def parse_login(self):
        html = requests.get(url=self.login_url,headers=self.user_agent)
        str_ = html.text
        return str_

    # 获取验证信息存储
    def get_data(self,str):
        response = etree.HTML(str)
        img_src = response.xpath("//img[@class='input3']/@src")[0]
        img_src = 'http://www.zhongdengwang.org.cn' + img_src
        return img_src

    # 保存验证码
    def save_img(self,img_src):
        r = requests.get(url=img_src,headers=self.user_agent)
        f = open('./gitcode.png','wb')
        f.write(r.content)
        f.close()

    # 识别验证码并返回对应的值
    def check_cod(self):
        result = yundama.get_result()
        return result

    def login_main(self,result):
        pass

    # 运行
    def run_(self):
        str_ = self.parse_login()
        img_src = self.get_data(str_)
        print("开始保存图片!")
        self.save_img(img_src)
        print("开始识别验证码!")
        result = self.check_cod()
        print("识别结束!")
        print('验证码为:',result)
        return  result


if __name__ == '__main__':
    Login = login()
    result = Login.run_()
    t = open("code.txt",'a')
    t.write(result)
    t.write(';')
    t.close()

