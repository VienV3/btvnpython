import requests
from high_order_framework_requests_python_master import utils_class

""" #Get
url="https://nghiahsgs.com/"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}
res=requests.get(url,headers=headers)

status_code=res.status_code
data=res.text
utils_class.File_Interact("test.html").write_file(data)
 """
 #POST
""" url="https://nghiahsgs.com/"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}
dataPOST={
    "username":"zzzzz",
    "age":"xxx"
}
res=requests.post(url,data=dataPOST,headers=headers) """
#get_current_myip
def get_current_ip():
    url="https://api.myip.com/"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    res=requests.get(url,headers=headers).json()
    my_ip=res["ip"]
    country=res["country"]
    return my_ip,country
if __name__=="__main__":
    my_ip,country=get_current_ip()