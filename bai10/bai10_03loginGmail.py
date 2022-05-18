from high_order_framework_requests_python_master import utils_chrome_selenium,utils_class
import os
import time
os='windows'
isLoadImage=True
isHeadless=False
folder_save=r'E:\\001-NguoiDung-Chrome\\DATA-ProfileChrome\\NguoiDung-001'
proxy=''
chrome_autologingmail=utils_chrome_selenium.Chrome_auto(os,isLoadImage,isHeadless,folder_save,proxy)
driver1=chrome_autologingmail.initDriver()
driver1.get('https://mail.google.com/mail/u/0/')
driver1.save_screenshot('screen_gmail.png')


# driver1.quit()