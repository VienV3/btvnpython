from high_order_framework_requests_python_master import utils_chrome_selenium,utils_class
import requests,os,selenium,time
from selenium.webdriver.common.by  import By
title="Gia thế Nobita"
ndung='''Căn nhà mà Nobita sống có từ thời ông bà với chỉ hai tầng và một cái vườn nhỏ. Trong gia đình Nobi, bố của Nobita là một nhân viên văn phòng bình thường, hàng ngày đi làm bằng tàu điện ngầm. Còn mẹ của Nobita ở nhà làm công việc nội trợ và thường hỏi con câu hỏi kinh điển: "Đã làm bài tập về nhà chưa mà đi chơi?" Ông Nobisuke, bố của Nobita có sở thích câu cá, hút thuốc và đánh Golf, dù vậy cả bố mẹ ít khi nào đáp ứng sở thích của Nobita như mua đồ chơi, đi du lịch... Ngay cả sở thích xem tivi của Nobita cũng gặp nhiều trắc trở khi chiếc tivi liên tục dở chứng nhưng ông Nobisuke nhất quyết không sắm sửa cái mới vì... tốn tiền.'''
os = 'windows'
isLoadImage=True
isHeadless=False
folder_save=''
proxy=''

chrome_auto1 = utils_chrome_selenium.Chrome_auto(os,isLoadImage,isHeadless,folder_save, proxy)
driver1=chrome_auto1.initDriver()
driver1.get('http://oldwp.nghiahsgs.com/wp-admin/')
time.sleep(2)
# dien user
driver1.find_element_by_css_selector("input[type='text']").send_keys('nghiahsgs')

# nhap password
driver1.find_element_by_css_selector("input[type='password']").send_keys('261997')
# click vao login
driver1.find_element_by_css_selector("input[type='submit']").click()
# add new post
driver1.get('https://oldwp.nghiahsgs.com/wp-admin/post-new.php')
# find add title
driver1.find_element_by_css_selector('input[name="post_title"]').send_keys(title)
# fint content and add content
driver1.find_element(By.CSS_SELECTOR,'button[id="content-tmce"]').click()
driver1.find_element(By.CSS_SELECTOR,'iframe').click()
driver1.find_element(By.XPATH,'//*[@id="content_ifr"]').send_keys(ndung)
time.sleep(1)
# checkbox chuyen muc
driver1.find_element(By.XPATH,'//label[text()=" test_post"]').click()
# click upload anh
driver1.find_element(By.XPATH,'//a[text()="Set featured image"]').click()
#add anh dai dien tu may tinh
driver1.find_element(By.CSS_SELECTOR,'input[type="file"]').send_keys('C:\\Users\\NC\\Downloads\\binance_xs.png')
#  C:\\Users\\NC\\Downloads\\binance_xs.png
time.sleep(2)
driver1.find_element(By.XPATH,'//button[text()="Set featured image"]').click()
time.sleep(2)
driver1.find_element(By.XPATH,'//*[@id="publish"]').click()
time.sleep(2)
# driver1.find_element(By.XPATH,'//*[@id="editable-post-name"]').click()
# time.sleep(2)
# driver1.quit()










