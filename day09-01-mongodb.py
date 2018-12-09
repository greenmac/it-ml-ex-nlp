# import
from pymongo import MongoClient
from bson.objectid import ObjectId #這東西再透過ObjectID去尋找的時候會用到

# connection
client = MongoClient("127.0.0.1", 27017) # 如果你只想連本機端的server你可以忽略，遠端的url填入: mongodb://<user_name>:<user_password>@ds<xxxxxx>.mlab.com:<xxxxx>/<database_name>，請務必既的把腳括號的內容代換成自己的資料。
db = client['PK10']
collection = db['bet_20181206']
# test if connection success
collection.stats  # 如果沒有error，你就連線成功了。

#尋找一筆資料
# cursor = collection.find_one({'_id': ObjectId('5c0c9cbc8f5e7357c0539d46')}) #如果你在意速度的話用Id尋找會比用內容尋找快很多喔!
# print(cursor)
#回傳全部資料
cursor = collection.find() #此處須注意，其回傳的並不是資料本身，你必須在迴圈中逐一讀出來的過程中，它才真的會去資料庫把資料撈出來給你。
# data = [d for d in cursor] #這樣才能真正從資料庫把資料庫撈到python的暫存記憶體中。
# print(data)
for d in cursor:
    print(d)
#尋找全部資料
# cursor = collection.find({'_id': ObjectId('5c0c9cbc8f5e7357c0539d46')})

# # 刪除一筆資料
# collection.delete_one({'<column_name>': '<what_you_want>'})
# # 刪除全部資料
# collection.delete_many({})
# # 刪除多筆資料
# collection.delete_many({'<column_name>': '<what_you_want>'})


player_dict = {
    "product" : 'test01',
    "date" : '2018-12-09',
    "player_name" : 'Charles',
    "bet_0" : {
        'nunmber': '112234'
    },
}

# 插入一筆資料: 請放入一個dict
x = collection.insert_one(player_dict)
# print(x)
# 插入多筆資料: 請放入一個dist
# collection.insert_many(player_dict)