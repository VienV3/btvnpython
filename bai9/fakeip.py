import requests
from high_order_framework_requests_python_master import utils_class
host='171.253.128.245'
dcom_port='4000'

http_proxy=f"http://{host}:{dcom_port}"
https_proxy=f"https://{host}:{dcom_port}"
proxyDict={
    'http' : http_proxy,
    'https' : https_proxy,
}
url='https://httpbin.org/ip'
res=requests.get(url,proxies=proxyDict).json()
print(res)

string_Interact1=utils_class.String_Interact()
url='https://etherscan.io/tx/0x39f0a0cfc72be38692b0c5a2a0156859b246a1b08eb7ae64478ff89e9fbe89c4'
data=requests.get(url,proxies=proxyDict).text
utils_class.File_Interact('code2.html').write_file(data)