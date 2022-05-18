from high_order_framework_requests_python_master import utils_chrome_selenium
from high_order_framework_requests_python_master import utils_class
import time
import os

import high_order_framework_requests_python_master
chrome_auto1=utils_chrome_selenium.Chrome_auto(os='windows',isLoadImage=True,isHeadless=False,folder_save='',proxy='')

list_image=os.listdir('C:\\Users\\NC\\Downloads\\image')
list_link_image=[]

driver1=chrome_auto1.initDriver()
driver1.get('https://oldwp.nghiahsgs.com/wp-admin')

# tim form user password de dien thong tin
# dien thong tin user
driver1.find_element_by_css_selector('input[type=text]').send_keys('nghiahsgs')
# dien thong tin password
driver1.find_element_by_css_selector('input[type=password]').send_keys('261997')
# click submit 
driver1.find_element_by_css_selector('input[type=submit]').click()
# tim va chon class chua phan upload anh
# driver1.find_elements_by_css_selector('li.wp-has-submenu')[3].click()
driver1.get('https://oldwp.nghiahsgs.com/wp-admin/media-new.php') #click vao luon phan upload anh
# for i in list_image:



# driver1.find_element_by_css_selector('input[type=file]').send_keys('C:\\Users\\NC\\Downloads\\image\\img1.jpg')#upload 1 image
#upload mutil image

for i in list_image:
    path_image=f'C:\\Users\\NC\\Downloads\\image\\{i}'
    #upload file
    driver1.find_element_by_css_selector('input[type="file"]').send_keys(path_image)
for i in range(0,len(list_image)):
    # lay link anh vua upload len
    link=driver1.find_elements_by_css_selector('div[class=centered"] img')[i].get_attribute("src")
    list_link_image.append(link)
utils_class.File_Interact('link.txt').write_file_from_list(list_link_image)
driver1.quit()
