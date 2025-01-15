from  pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
mongo_db = client['birthday_email_sender']
users_collection = mongo_db['my_users']

def save_user_to_mongo(user_data):
    """Insert user details into MongoDB."""
    users_collection.insert_one(user_data)

def get_all_users_from_mongo():
    """Retrieve users whose birthday is today."""
    # Get today's date in YYYY-MM-DD format
    today = datetime.now().strftime('%Y-%m-%d')

    # Query MongoDB for users with birthdays matching today's date
    return list(users_collection.find({"date_of_birth": today}))
