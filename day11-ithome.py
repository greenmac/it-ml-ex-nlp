import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# 首先我們先到iThome鐵人的首頁，把第一頁到最後一頁的網址抄下來
url = 'https://ithelp.ithome.com.tw/ironman?page=1#ir-list'
res = requests.get(url) ## 先爬下第一頁
soup = BeautifulSoup(res.text, 'lxml')
maxpage = soup.select('.pagination')[0].find_all('a')[-2].text ## 定位出最後一頁的頁數print(maxpage)

# urls = []
# for i in range(maxpage):  ## 把接下來要爬的網頁準備好
#     page = i+1
#     url = "https://ithelp.ithome.com.tw/ironman?page=" + str(page) + "#ir-list"  ## 大家可以觀察每一頁url的變化
#     urls.append(url)

# # 接著爬入每一頁，把每個文章的比賽分類，以及其網址抄下來。之所以要抄分類，是因為文章網址內部找不到分類，所以只好在這邊些記錄下來。
# articles_rows = []
# for idx, url in enumerate(urls):
#     res = requests.get(url)   
#     soup = BeautifulSoup(res.text, 'lxml')
#     articles = soup.select('.ir-list')  ## 找出該頁面的所有文章

#     for article in articles:
#         article_dict = {}
#     group = article.select('.group-badge__name')[0].text.replace(' ', '').replace('\n', '')  ## 定位該篇文章參與比賽的參賽組別
#     article_url = article.select('.ir-list__title')[0].select('a')[0]['href']  ## 紀錄該篇文章的網址
#     article_dict['group'] = group  
#     article_dict['article_url'] = article_url
#     articles_rows.append(article_dict)
    
#     if idx % 10 == 0:  ## 讓你大概知道進度到哪了
#         print(idx)
# # 尚未讀完(從第3項開始)