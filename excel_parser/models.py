from django.db import models

# Create your models here.


class Budget(models.Model):
    MDA_name = models.CharField(max_length=45)
    project_recipient_name = models.CharField(max_length=45)
    project_name = models.TextField()
    project_amount = models.FloatField()
    project_date = models.DateField()
   
    def ___str___(self):
        return self.MDA_name
