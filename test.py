from pymongo import MongoClient
import datetime

# conn = MongoClient("mongodb://greenmac16:mac50787@ds151141.mlab.com:51141/nlp") # 如果你只想連本機端的server你可以忽略，遠端的url填入: mongodb://<user_name>:<user_password>@ds<xxxxxx>.mlab.com:<xxxxx>/<database_name>，請務必既的把腳括號的內容代換成自己的資料。
# db = conn.ithome_ironman
# collection = db.articles

conn = MongoClient()
db = conn.test
collection = db.articles
new_posts = [{"author": "Mike",
    "text": "Another post!",
    "tags": ["bulk", "insert"],
    "date": datetime.datetime(2009, 11, 12, 11, 14)},
    {"author": "Eliot",
    "title": "MongoDB is fun",
    "text": "and pretty easy too!",
    "date": datetime.datetime(2009, 11, 10, 10, 45)}]
result = collection.insert_many(new_posts)
# print(new_posts)