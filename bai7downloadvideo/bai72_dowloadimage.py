import requests
import shutil
url_image='https://nghiahsgs.com/wp-content/uploads/2021/08/doluong.jpg'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
respone=requests.get(url_image,stream=True,timeout=10,headers=headers,verify=False)
file_path='b.jpg'
with open(file_path,'wb') as out_file:
    shutil.copyfileobj(respone.raw,out_file)
del respone
