from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['birthday_email_sender']
users_collection = db['my_users']

users = list(users_collection.find())
for user in users:
    print(user)
