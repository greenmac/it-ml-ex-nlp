# https://ithelp.ithome.com.tw/articles/10191259
from bs4 import BeautifulSoup
import requests
import pandas as pd

###----------
##bs4
# 一、把取得的html純文字送給BeautifulSoup，產生BeautifulSoup類別
re = requests.get('https://www.crummy.com/software/BeautifulSoup/bs4/doc/')
soup = BeautifulSoup(re.text)

# 二、找到element
# ## 透過tag名稱尋找元素(第一個，回傳一個元素類別)
# elem = soup.find_all('a')
# print(elem)
# print('------------------------------')
# ## 透過tag名稱尋找元素(全部，回傳一個元素類別「陣列」)
# elems = soup.find_all('a')
# for elem in elems:
#     print(elem)
# print('------------------------------')
# ## 透過selector尋找元素(回傳一個元素類別「陣列」)
# selector = '#quick-start > h1'
# elem = soup.select(selector)
# print(elem)
# print('------------------------------')

# # 三、取出element中的重要資訊
# ## 取出element特定attribute的值
# elem = soup.find('a')
# print(elem)
# print(elem['href']) ##方法一
# print(elem.get('href'))  ##方法二
# print('------------------------------')
# ## 取出一對tag間的文字
# selector = "#quick-start > h1"
# elem = soup.select(selector)
# print(elem[0])
# print(elem[0].text)
# print('------------------------------')
# ## 取得整個網頁的所有文字)
# print(soup.get_text())
# print('------------------------------')


# ###----------
# ##pandas
url = 'http://mops.twse.com.tw/server-java/t164sb01?step=1&CO_ID=1216&SYEAR=2017&SSEASON=1&REPORT_ID=C' ## 公開資訊觀測站的財報
dfs = pd.read_html(url) ## 回傳DataFrame類別的陣列
df = dfs[1]
# print(df)
# print('------------------------------')
# # 簡單的操作pandas教學
# ## 只查看前面五行
# print(df.head(5))
# print('------------------------------')
# # 查看所有的columns
columns = df.columns
# print(columns)
# print('------------------------------')
# ## 僅查看取特定column
showColumns = [columns[0], columns[1]]
# print(df[showColumns].head())
# print('------------------------------')
# ## 僅查看特定的row
# print(df.xs(5))  ##不可指派內容
# print(df.loc[5])  ##可指派內容
# print('------------------------------')
# ## 存檔
df.to_csv('{csv-IFRS單一公司案例文件預覽及下載}', index=False)
df.to_json('{json-IFRS單一公司案例文件預覽及下載}')