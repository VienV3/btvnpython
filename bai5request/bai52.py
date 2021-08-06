import requests
from requests.api import head
url="https://drive.google.com/drive/u/1/folders/1_kDoUZ_bq1BGDj8gG1i1iCDosPz9xDVQ?fbclid=IwAR2fYXa4fKGS31eVRvxpu_wG_H3OWkhXBcjenYmJvxjsYQOgZIHFJKj0ejI"
hearders={
    "resurl":"https://play.google.com/log?format=json&hasfast=true&authuser=1",
    "cokie":"ANID=AHWqTUl307nfcm6YA-xDPBjnyy_Fo9WY4prwsUCDm-FfOdSfNlaVHUjh0BHB-CNE; OGP=-19025051:-19022622:; OGPC=19022519-1:19025051-1:19022622-1:19025227-1:; SID=AAjIl-2xVzyvQuGaZLFPEl2nUYPDAu3_1MI5a-zzhMF931GfYO39KMxpBhsC1ZMZqaWcKg.; __Secure-1PSID=AAjIl-2xVzyvQuGaZLFPEl2nUYPDAu3_1MI5a-zzhMF931GfLC7eJpwf7m41XHy35JBEsg.; __Secure-3PSID=AAjIl-2xVzyvQuGaZLFPEl2nUYPDAu3_1MI5a-zzhMF931Gfj9EHH6tKHNFp0r1VdxPsQA.; HSID=AnTjJ-riT6dMtwr54; SSID=ANphjtIppa1qHAOaO; APISID=ZIwexag0-Kt3SeSa/AnL4NnOPndMKfuBfZ; SAPISID=wPRuGUCwfG02YcJb/A921UOR989mcPpWbx; __Secure-1PAPISID=wPRuGUCwfG02YcJb/A921UOR989mcPpWbx; __Secure-3PAPISID=wPRuGUCwfG02YcJb/A921UOR989mcPpWbx; SEARCH_SAMESITE=CgQIlpMB; NID=220=pZ0aOqq_eL1s3yO8mcK-dHJsNKis2olZTkF9TTk7PyMcsnsjR_bOTqXl80zkLVSZO8OPJaUBIhT3LQPzrvdFIJHfQ4SkZBpp-Mj6-VPQkR_NYUR2oBwi15QqSeFbiGGCvBuAcx9shiAUnxaeRl4WJLEbEEHVT5zRTEHHZG4LHRlYndcxTAeG3v4qxpsgn5QVvqBfD2jYlZ9MYKquePXk9lU9_meDjC09QSixb3P3xQh_nYFPwcyR1PvE5Q4x5s5V1d5JDUsUgXvS0EEgVjsqZpbWQW9Ottb3jyx-tD8hQwddkVWBcbgyxJVk6zbh21mcaEl98k6Io2_xImFG6FJI-7GAkdxmzmDhEVzjEujDZS8qcLWvQ-kXmqHsfe0OVqCwQxp00haWrzGsuUrUKVrU9TqxQnPrxNukSmRkF9WqqtLS5NPjVnD07PSRf1BfAEQGg9R9BQ; 1P_JAR=2021-08-01-12; SIDCC=AJi4QfGR6oiRA7m9k95js7PHUB3pr_EEBsL_i4CKAiOPxG0M4hmGv_g3IOD9Ow3FU-lquE37jA; __Secure-3PSIDCC=AJi4QfE4lye06vYDA05L48PlcyCuML3fgr4CMiFxfjBmy4CNv6YOSjsAXqTPGOKJujaKFLC0Zzk",
    "x-client-data":"CJa2yQEIpbbJAQjBtskBCKmdygEIj7nKAQiG3MoBCNCaywEIoKDLAQjc8ssBCO/yywEIzvbLAQi0+MsBCJ75ywEIyfnLAQjw+csBCPr5ywEIsPrLAQjw+ssBGI6eywEYuvLLARiP9csB",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}
res=requests.get(url,headers=hearders)
data=res.text