 # -*- coding: utf-8 -*-
import re
import scrapy


class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        authenticity_token = re.search(r'name="authenticity_token" value="(.*?)" />' ,response.body.decode()).group(1)
        formdata = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': authenticity_token,
            'login': 'MangoApe',
            'password': 'Wearem2010'
        }
        login_url = 'https://github.com/session'
        #专门发送post请求， 请求参数该外formdata， 没有method参数， 其他参数和request模块一样
        yield scrapy.FormRequest(login_url, formdata=formdata, callback=self.check_login)


    def check_login(self,response):
        #发送一个登录后才能获取的页面， 来验证是否登录成功
        check_url = 'https://github.com/MangoApe'
        yield scrapy.Request(check_url, callback=self.save_html)


    def save_html(self,response):
        with open('github2.txt', 'w')as f:
            f.write(response.body.decode())
