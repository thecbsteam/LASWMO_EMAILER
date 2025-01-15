from django_cron import CronJobBase, Schedule
from django.core.mail import send_mail
from ...models import User  # Replace with the actual model for users
from datetime import date

class BirthdayEmailCronJob(CronJobBase):
    # Set a unique code for your cron job
    RUN_AT_TIMES = ['00:18']  # Time(s) to run daily in HH:MM (24-hour format)

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'users.birthday_email_cron'  # Unique identifier for this job

    def do(self):
        today = date.today()
        birthday_users = User.objects.filter(birthday=today)  # Adjust based on your model
        for user in birthday_users:
            send_mail(
                'Happy Birthday!',
                f'Dear {user.name}, we wish you a wonderful birthday!',
                'your_email@gmail.com',
                [user.email],
                fail_silently=False,
            )
    