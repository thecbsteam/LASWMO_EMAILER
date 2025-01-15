from django.core.management.base import BaseCommand
from pymongo import MongoClient
from datetime import datetime
from django.core.mail import send_mail
#from dotenv import load_dotenv
#import os
#load_dotenv()

#db_password = os.getenv('DB_PASSWORD')


class Command(BaseCommand):
    help = "Send birthday emails to users from MongoDB"

    def handle(self, *args, **kwargs):
        # MongoDB connection
        client = MongoClient('mongodb+srv://osimigbubemigodsgift:mWtHyXvwEEqcGukR@cluster0.kmyaf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        db = client['EMAIL_SENDER']
        users_collection = db['user']

        # Get today's date in MM-DD format
        today = datetime.now().strftime('%m-%d')

        # Find users with today's birthday
        users = users_collection.find({
            "date_of_birth": {"$regex": f".*{today}$"}
        })

        users = list(users)

        if not users:
            self.stdout.write("No users with a birthday today.")
        else:
            self.stdout.write(f"Found {len(users)} user(s) with a birthday today.")
            for user in users:
                try:
                    send_mail(
                        "Happy Birthday!",
                        f"Dear {user['first_name']},\n\nWishing you a very Happy Birthday! Have a great day!\n\nBest Regards,\nYour Team",
                        "your_email@example.com",  # Replace with your sender email
                        [user['email']],
                        fail_silently=False,
                    )
                    self.stdout.write(f"Email sent to {user['email']}.")
                except Exception as e:
                    self.stderr.write(f"Failed to send email to {user['email']}. Error: {e}")
