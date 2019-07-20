import base64
import requests

url_ip = "http://api.wandoudl.com/api/ip?app_key=8f9c40153895e81433aaa9ec551414ae&pack=0&num=20&xy=1&type=2&lb=\r\n&mr=1&"

response = requests.get(url_ip)
print(response.text)
proxies = []
for ip in response["data"]:
    print(ip)
    ip_port = str(ip['ip']) + ':' + str(ip['port'])
    proxies.append(ip_port)


print(proxies)


