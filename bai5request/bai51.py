#request
import requests
from requests.api import head
#vidu ve GET
url = "https://api.myip.com/"
#header la tat ca cac goi tin
headers={
    "user agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "cookie":"__cf_bm=da9186f162c4ca9bb6de59afc1a64ea94e81d039-1627744540-1800-AWEbrXLGkkIeUr9yvouk2BDYmyyIsM4Zs2bOJjSCAmM4seHuYj5bHBPumhcWzRKOl/1rozDeUPMeR4QbP+WJhcE=; path=/; expires=Sat, 31-Jul-21 15:45:40 GMT; domain=.myip.com; HttpOnly; Secure; SameSite=None",

}
res = requests.get(url,headers=headers)
#res
#status_code=res.status_code
data=res.text