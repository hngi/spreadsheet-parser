from django.db import models

# Create your models here.
def upload_file_handler(instance, filename):
    return f'daily/{filename}'

class ExcelSaverModel(models.Model):
    daily_report_file = models.FileField(upload_to=upload_file_handler, null=True)

class Budget(models.Model):
    MDA_name = models.CharField(max_length=100)
    project_recipient_name = models.CharField(max_length=120)
    project_name = models.TextField()
    project_amount = models.FloatField()
    project_date = models.DateField()
   
    def ___str___(self):
        return self.MDA_name