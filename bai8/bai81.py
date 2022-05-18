from xml.dom.minidom import Document
import requests
# from high_order_framework_requests_python_master import utils_class
from utils_class import *
String_Interact1=String_Interact()
url='https://nghiahsgs.com/'
data=requests.get(url).text
# File_Interact('test.html').write_file(data)
listCSSSelector=[
    '.entry-title',
    '.entry-title',
]
listeAttr=[
    'innerText',
    'innerHTML',
]
L0,L1=String_Interact1.extractListTextByCSSSelector(data,listCSSSelector=listCSSSelector,listeAttr=listeAttr)
