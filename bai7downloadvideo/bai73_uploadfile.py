import requests
url=''
files={'file':open('a.jpg','rb')}
data=requests.post(url,files=files).json()
print(data)