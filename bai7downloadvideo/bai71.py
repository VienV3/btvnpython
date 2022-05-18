import re
import requests
from high_order_framework_requests_python_master import utils_class
string_interact1=utils_class.String_Interact()
#gom 2 phan:erorr,data
def get_direct_link(url_input):


    url_input = 'https://www.youtube.com/watch?v=GxYpY-Wf9Ls'
    #step 1:get data fron ajax
    url = 'https://www.y2mate.com/mates/vi252/analyze/ajax'
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'content-type':'application/x-www-form-urlencoded; charset=UTF-8'
    }
    dataPost = {
        "url":url_input,
        "q_auto":0,
        "ajax":1
    }
    res = requests.post(url,data=dataPost,headers=headers).text
    res= res.replace('\\','')
    #Step2: tach chuoi ra v_id, _id
    #utils_class.File_Interact('code.html').write_file(res)
    _id=string_interact1.regex_one_value('k__id = "(.*?)"',res) #su dung regex de lay duoc _id tu res.text
    v_id=string_interact1.regex_one_value('k_data_vid = "(.*?)"',res)#su dung regex de lay duoc v_id tu res.text
    # step3: 
    url="https://www.y2mate.com/mates/convert" #file url gianh de convert tu link can download sang link download
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'content-type':'application/x-www-form-urlencoded; charset=UTF-8'
    }

    dataPOST={
        'type': 'youtube',
        '_id': _id,
        'v_id': v_id,
        'ajax': 1,
        'token': '',
        'ftype': 'mp4',
        'fquality': '720'
    } #thiet lap thong so cho link can download
    res = requests.post(url,data=dataPOST,headers=headers).text
    res=res.replace('\\','')
    utils_class.File_Interact('code.html').write_file(res)
    direct_link=string_interact1.regex_one_value('<a href="(.*?)"',res)
    return direct_link
if __name__=="__main__":
    url_input=''
    direct_link=get_direct_link(url_input)
