# https://ithelp.ithome.com.tw/articles/10191165
# hotspotshield,一但你發現你的IP被封鎖了，直接重新連線hotspotshield，它就會幫你換到其他國家的IP了
import requests
import time
from selenium import webdriver

###----------
##直接偵測requests的header
# ## 這是一個很有名的，爬蟲愛好者常去挑戰的一個募資網站
# url = "https://www.indiegogo.com/projects/viviva-colorsheets-the-most-portable-watercolors-painting-travel--4#/" 
# ## 使用假header
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
# re = requests.get(url, headers=headers) 
# re.encoding = 'utf8'
# print(re.text)

###----------
##一秒太多次requests
# url = "http://cid.acad.ncku.edu.tw/files/14-1056-54086,r677-1.php?Lang=zh-tw" 
# contextLi = []
# i=0
# while i < 10:
#     re = requests.get(url)
#     re.encoding = 'utf8'
#     contextLi.append(re.text)
#     i += 1
#     print(i , " succeed")
#     time.sleep(2)
# print("this is the first requests----------------------------------\n", contextLi[0])
# print("this is the last requests----------------------------------\n",contextLi[-1])

###----------
##selenium
driver = webdriver.Chrome() # 如果你沒有把webdriver放在同一個資料夾中，必須指定位置給他
# driver = webdriver.Firefox() # 如果你沒有把webdriver放在同一個資料夾中，必須指定位置給他
driver.get('https://timetable.nctu.edu.tw/')
def tryclick(driver, selector, count=0): ##保護機制，以防無法定味道還沒渲染出來的元素
    try:
        elem = driver.find_element_by_css_selector(selector)
        # elem = driver.find_element_by_xpath(Xpath)  # 如果你想透過Xpath定位元素
        elem.click()
    except:
        time.sleep(2)
        count += 1
        if(count < 2):
            tryclick(driver, selector, count)
        else:
            print("cannot locate element" + selector)
tryclick(driver, "#flang > option:nth-child(2)") # 設定成中文
tryclick(driver, "#crstime_search") # 點擊「查詢」按鍵
time.sleep(3) # 等待javascript渲染出來，當然這個部分還有更進階的作法，關鍵字是implicit wait, explicit wait，有興趣可以自己去找
html = driver.page_source # 取得html文字
# driver.close() # 關掉Driver打開的瀏覽器
print(html)