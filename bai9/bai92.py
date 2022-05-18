from high_order_framework_requests_python_master import utils_chrome_selenium
os='windows'
isLoadImage=True
isHeadless=False
folder_save=''
proxy=''
chorme_auto1=utils_chrome_selenium.Chrome_auto(os,isLoadImage,isHeadless,folder_save, proxy)
driver1=chorme_auto1.initDriver()
driver1.get('https://nghiahsgs.com')
# document.querySelector('.entry-title').innerText
# kieu tuong tac1: lay gia tri cua no:text. lay link, (url, anh ...)=> lay astribute element
# element=driver1.find_element_by_css_selector('.entry-title')
# driver1.find_element_by_css_selector('.entry-title').get_attribute('innerHTML')

# kieu tuong tac 2: send text or click
# L_element=driver1.find_elements_by_css_selector('.entry-title a')
# L_element[1].click()

# element=driver1.find_elements_by_css_selector('input[type=search]')[1]
# element.send_keys('nghia')
# 

# kieu tuong tac 3
# gui js di
# js_command='''localtion.reload()'''
# driver1.execute_script(js_command)
# js_command='''document.querySelectorAll('.entry-title a')[0].click()'''
# driver1.execute_script(js_command)
# 
js_command='''return document.querySelector('.entry-title').innerText'''
tieude=driver1.execute_script(js_command)
# document.querySelectorAll('.entry-title')
# List_element=driver1.find_elements_by_css_selector('.entry-title')
# 1:27