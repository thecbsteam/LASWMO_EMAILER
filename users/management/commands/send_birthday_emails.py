from django.core.management.base import BaseCommand
from ...models import User
from django.core.mail import send_mail
from datetime import date

class Command(BaseCommand):
    help = 'Send birthday emails to users'

    def handle(self, *args, **kwargs):
        today = date.today()
        birthday_users = User.objects.filter(birthday=today)
        for user in birthday_users:
            send_mail(
                'Happy Birthday!',
                f'Dear {user.first_name}, Happy Birthday!',
                'your_email@example.com',
                [user.email],
                fail_silently=False,
            )
        self.stdout.write(f"Sent birthday emails to {len(birthday_users)} users.")
