from django.db import models

# Create your models here.
class Budget(models.Model):
    MDA_name = models.CharField(max_length=100)
    project_recipient_name = models.CharField(max_length=120)
    project_name = models.TextField()
    project_amount = models.FloatField()
    