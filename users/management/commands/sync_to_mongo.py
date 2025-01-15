from django.core.management.base import BaseCommand
from ...models import User  # Replace 'your_app' and 'User' with the correct names
#from ....birthday_system.mongoDB_util import save_user_to_mongo
from birthday_system.birthday_system.mongoDB_util import save_user_to_mongo

class Command(BaseCommand):
    help = "Sync users from Django database to MongoDB"

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        user_data_list = []
        for user in users:
            user_data_list.append({
                'name': user.name,
                'email': user.email,
                'birthday': user.birthday.strftime('%Y-%m-%d'),  # Format as string
            })
        
        for user_data in user_data_list:
            save_user_to_mongo(user_data)
        
        self.stdout.write("User details have been synced to MongoDB.")
