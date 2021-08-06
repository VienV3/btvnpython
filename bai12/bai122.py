from peewee import Source
import requests
from util_db import *
def get_score(sbd):

    url = "https://diemthi.vnanet.vn/Home/SearchBySobaodanh?code={sbd}&nam=2021"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    res = requests.get("https://diemthi.vnanet.vn/Home/SearchBySobaodanh?code={sbd}&nam=2021",headers=headers).json()

    try:
        toan = res['result'][0]['Toan']
        van = res['result'][0]['NguVan']
        anh = res['result'][0]['NgoaiNgu']
    except:
        toan = -1
        van = -1
        anh = -1    
    return toan,van, anh
sbd = "26004493"
get_score(sbd)
instance = Score(sbd = sbd,toan = toan,van = van,anh = anh)
instance.save()