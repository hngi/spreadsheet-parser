from __future__ import unicode_literals
from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class ExcelUpload(models.Model):
    document = models.FileField(upload_to='user/', validators=[FileExtensionValidator(['xlsx'])])
    upload_at = models.DateTimeField(auto_now_add=True)
