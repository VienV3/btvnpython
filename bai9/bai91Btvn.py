import requests
from high_order_framework_requests_python_master import utils_class

string_Interact1=utils_class.String_Interact()
url='https://etherscan.io/tx/0x39f0a0cfc72be38692b0c5a2a0156859b246a1b08eb7ae64478ff89e9fbe89c4'
data=requests.get(url).text
# utils_class.File_Interact('code.html').write_file(data)
listCSSSelector=[
    '#spanTxHash',

]
listeAttr=[
    'innerText',

]
L0,=string_Interact1.extractListTextByCSSSelector(data,listCSSSelector=listCSSSelector,listeAttr=listeAttr)


# chua bai tap ve nha chua xong do bi chan ip