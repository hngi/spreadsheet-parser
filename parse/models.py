from django.db import models

# Create your models here.


class ExcelUpload(models.Model):
    name = models.CharField(max_length=25)
    document = models.FileField(upload_to='user/')
    upload_at = models.DateTimeField(auto_now_add=True)
