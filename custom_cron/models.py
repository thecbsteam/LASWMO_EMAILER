from django.db import models
from django_cron.models import CronJobLog as OriginalCronJobLog

class CronJobLog(OriginalCronJobLog):
    """
    Custom CronJobLog class that inherits from the base django_cron CronJobLog model.
    This class doesn't need to redefine indexes because the parent model already defines them.
    """
    class Meta:
        # This ensures that the table for this model uses the same name as the parent model table
        db_table = 'custom_cron_cronjoblog'
        app_label = 'custom_cron'
        # Inherit indexes from the parent model (no need to redefine them here)



