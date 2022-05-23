from django.db import models
from django.utils import timezone

class SlackMessage(models.Model):

    submission_date = models.DateTimeField(default=timezone.now)
    goal_date = models.DateField()
    time_spent = models.IntegerField()