from django.db import models

def upload_file_handler(instance, filename):
    date = filename.split('-')
    day = date[0]
    month = date[1]
    year = date[2].split('.')[0]
    if len(year) < 3:
        year = '20'+year
    return f'daily/{year}/{month}/{day}/{filename}'
class ExcelSaverModel(models.Model):
    daily_report_file = models.FileField(upload_to=upload_file_handler, null=True)



class Budget(models.Model):
    MDA_name = models.CharField(max_length=45)
    project_recipient_name = models.CharField(max_length=45)
    project_name = models.TextField()
    project_amount = models.FloatField()
    project_date = models.DateTimeField()
