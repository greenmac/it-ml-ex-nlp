# https://ithelp.ithome.com.tw/articles/10191848
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
maxpage = int(soup.select('.pagination')[0].find_all('a')[-2].text) ## 定位出最後一頁的頁數print(maxpage)

urls = []
for i in range(maxpage):  ## 把接下來要爬的網頁準備好
    page = i+1
    url = "https://ithelp.ithome.com.tw/ironman?page=" + str(page) + "#ir-list"  ## 大家可以觀察每一頁url的變化
    urls.append(url)

# 接著爬入每一頁，把每個文章的比賽分類，以及其網址抄下來。之所以要抄分類，是因為文章網址內部找不到分類，所以只好在這邊些記錄下來。
articles_rows = []
for idx, url in enumerate(urls): # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    articles = soup.select('.ir-list')  ## 找出該頁面的所有文章

    for article in articles:
        article_dict = {}
        group = article.select('.group-badge__name')[0].text.replace(' ', '').replace('\n', '')  ## 定位該篇文章參與比賽的參賽組別
        article_url = article.select('.ir-list__title')[0].select('a')[0]['href']  ## 紀錄該篇文章的網址
        article_dict['group'] = group  
        article_dict['article_url'] = article_url
        articles_rows.append(article_dict)
    
    if idx % 10 == 0:  ## 讓你大概知道進度到哪了
        print(idx)


df = pd.DataFrame(articles_rows)
# print(df)


def ArticleContentCrawler(row):
    url = row['article_url']
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    
    ## linke count
    like_count = int(soup.select('.likeGroup__num')[0].text)  ## 定位讚的次數

    ## article header
    header = soup.select('.qa-header')[0]
    corpusinfo = header.select('h3')[0].text.replace(' ', '').replace('\n', '')
    corpus_title = corpusinfo.split('第')[0]  ## 定位文章集的的主題
    corpus_day = int(re.findall(r'第[\d]+篇', corpusinfo)[0].replace('第', '').replace('篇', ''))  ## 定位參賽第幾天

    article_title = header.select('h2')[0].text.replace(' ', '').replace('\n', '')  ## 定位文章的title
    writer_name = header.select('.ir-article-info__name')[0].text.replace(' ', '').replace('\n', '')  ## 定位作者名稱
    writer_url = header.select('.ir-article-info__name')[0]['href']  ## 定位作者的個人資訊業面

    publish_date_str = header.select('.qa-header__info-time')[0]['title']  ## 定位發文日期，為了讓日期的格式被讀成python的datetime，所以做了下面很瑣碎的事
    date_items = pd.Series(publish_date_str.split(' ')[0].split('-') + publish_date_str.split(' ')[1].split(':')).astype(int)
    publish_datetime = datetime(date_items[0], date_items[1], date_items[2], date_items[3], date_items[4], date_items[5])

    browse_count = int(re.findall(r'[\d]+', header.select('.ir-article-info__view')[0].text)[0])  ## 定位瀏覽次數
    
    ## markdown_html
    markdown_html = soup.select('.markdown__style')[0]
    text_content = "\n".join([p.text for p in markdown_html.select('p')])  ## 定位所有文章的段落
    h1 = [h1.text for h1 in markdown_html.select('h1')]  ## 定位文章的標題們
    h2 = [h2.text for h2 in markdown_html.select('h2')] 
    h3 = [h3.text for h3 in markdown_html.select('h3')]
    h4 = [h4.text for h4 in markdown_html.select('h4')]
    h5 = [h5.text for h5 in markdown_html.select('h5')]
    h6 = [h6.text for h6 in markdown_html.select('h6')]
    
    row['like_count'] = like_count
    
    row['corpus_title'] = corpus_title
    row['corpus_day'] = corpus_day
    row['article_title'] = article_title
    row['writer_name'] = writer_name
    row['writer_url'] = writer_url
    row['publish_datetime'] = publish_datetime
    row['browse_count'] = browse_count
    
    row['text_content'] = text_content
    row['h1'] = h1 if h1 != [] else None  ## 如果是空list的話紀錄為None後面比較好處理
    row['h2'] = h2 if h2 != [] else None
    row['h3'] = h3 if h3 != [] else None
    row['h4'] = h4 if h4 != [] else None
    row['h5'] = h5 if h5 != [] else None
    row['h6'] = h6 if h6 != [] else None
    
    row['crawled_date'] = datetime.now()
    
    if int(row.name) % 50 == 0:  ## 列印出進度
        print(str(row.name) + " pages crawled!")
    
    return row

df = df.apply(ArticleContentCrawler, axis=1)
# print(df)

## 存成csv檔
# df.to_csv('ithomeironman.csv', index=False, encoding='utf8')
# pd_read = pd.read_csv('ithomeironman.csv')  ## 把檔案讀出來看看有沒有儲存成功
# print(pd_read)

## 存進MongoDB
from pymongo import MongoClient
##線上mongodb,目前多筆塞不進去
conn = MongoClient("mongodb://greenmac16:mac50787@ds155774.mlab.com:55774/ithome_ironman") # 如果你只想連本機端的server你可以忽略，遠端的url填入: mongodb://<user_name>:<user_password>@ds<xxxxxx>.mlab.com:<xxxxx>/<database_name>，請務必既的把腳括號的內容代換成自己的資料。
db = conn.ithome_ironman
collection = db.articles
cursor = collection.insert_many(list(df.T.to_dict().values()))  # 這是DataFrame塞進Mongo的常見寫法

##本機mongodb
# conn = MongoClient()
# db = conn.ithome_ironman
# collection = db.articles
# cursor = collection.insert_many(list(df.T.to_dict().values()))  # 這是DataFrame塞進Mongo的常見寫法