from django.db import models


class FilledQuestionnaire(models.Model):
    day_choices = models.CharField(max_length=9)
    month_choices = models.CharField(max_length=9)
