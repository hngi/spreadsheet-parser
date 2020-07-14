from __future__ import unicode_literals
from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class CDNUpload(models.Model):
    link = models.CharField(max_length=2083)
    upload_at = models.DateTimeField(auto_now_add=True)


class ExcelUpload(models.Model):
    document = models.FileField(upload_to='user/', validators=[FileExtensionValidator(['xlsx'])])
    upload_at = models.DateTimeField(auto_now_add=True)
