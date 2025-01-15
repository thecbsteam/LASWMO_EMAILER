from apscheduler.schedulers.blocking import BlockingScheduler
import os

# Define the function that will run your Django command
def send_birthday_emails():
    os.system('python manage.py send_birthday_emails')

# Create the scheduler
scheduler = BlockingScheduler()

# Add the job to the scheduler (set to run every day at 9:00 AM)
scheduler.add_job(send_birthday_emails, 'interval', days=1, start_date='2025-01-08 10:00:00')

# Start the scheduler
scheduler.start()



