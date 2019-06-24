# -*- coding: utf-8 -*-
import scrapy


class Github1Spider(scrapy.Spider):
    name = 'github1'
    allowed_domains = ['xxx.cn']
    start_urls = ['https://github.com/MangoApe']


    def start_requests(self):
        cookies_str = '_ga=GA1.2.1787641698.1554105525; _octo=GH1.1.2042677556.1554105525; _device_id=d5e2664eb466eab879cd0c0fc0510451; has_recent_activity=1; _gat=1; tz=Asia%2FShanghai; user_session=z-xu7FIukEXnKV8gk5Z71SI237E5HCcaMFoX8psL_GkQ-77E; __Host-user_session_same_site=z-xu7FIukEXnKV8gk5Z71SI237E5HCcaMFoX8psL_GkQ-77E; logged_in=yes; dotcom_user=MangoApe; _gh_sess=Vng3M1A2b0dmMUxVSHE2WUR3eU5XOEhPRytjRlZNTVRpbDJrbEp1aXBwODlBTXFxbWtxL2JhVmJxSWV1RzhhNHVEcXNReG9jRXMxeG1BRU5QWDZkbTEvYnZrYllEN0FaMGppbWlyTzlmWnE5Y3Q1Y0w4dnRoQ2puek42Wm5ZTWM4c3BEajdpRHlFVHdyc3JrWTF2TGtHVFJ5K2VDbzVQTE9TcGtGZURyTEFrZFNrMTNDZXAydFBsUmhYK1FjR3FFTmp6YUJ6OGlOblg4ZGNrcDU1N3YzZnlBSXNBRlF0blZjaU14SW5uZnU2VC96SEY3Q0hPaGphM2Q5NGFjNUlWSWhzTDFhSWt4MlJmM05lVDFHUk43VHc9PS0tY1VOb0tSU3JsMloxZHdqUThJKzFTdz09--67e1aa0bbc893fd7b0601ec897c98175a6c2d5ca'
        cookies_dict = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookies_str.split('; ')}
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                cookies=cookies_dict,
                callback= self.parse
            )

    def parse(self, response):
        # print(response.body.decode())
        with open('github.txt', 'w')as f:
            f.write(response.body.decode())
        print(response.status)

