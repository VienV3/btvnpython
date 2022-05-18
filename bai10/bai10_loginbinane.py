from high_order_framework_requests_python_master import utils_chrome_selenium,utils_class
import os
import time
import requests
os='windows'
isLoadImage=True
isHeadless=False
folder_save=r'E:\\001-NguoiDung-Chrome\\DATA-ProfileChrome\\NguoiDung-001'
proxy=''
chrome_autologinbinane=utils_chrome_selenium.Chrome_auto(os,isLoadImage,isHeadless,folder_save,proxy)
driver1=chrome_autologinbinane.initDriver()
# driver1.get('https://accounts.binance.com/en/login?return_to=aHR0cHM6Ly93d3cuYmluYW5jZS5jb20vZW4%3D')
#tim dien thong tin user
# driver1.find_element_by_css_selector('input[type="email"]').send_keys('tripp8kmccarty@gmail.com')
#dien thong tin pwd
# driver1.find_element_by_css_selector('input[type="password"]').send_keys("Visofts686868bnba@")
# driver1.find_element_by_css_selector('button#click_login_submit').click()
# time.sleep(3)
# veri_code=requests.get("https://2fa.live/tok/Y6QR44QIO7Z75OQK").text[10:16]
# driver1.find_element_by_css_selector('input[data-bn-type="input"]').send_keys(veri_code)
# driver1.find_element_by_css_selector('button.inactive').click()
driver1.get('https://docs.google.com/forms/d/1dPvIy31JjAloWiPruwwGuYYMGUntgBFI-PJiCQNXvM0/prefill')