from __future__ import unicode_literals
from django.db import models

# Create your models here.


class LinkUpload(models.Model):
    link = models.CharField(max_length=2083)
    upload_at = models.DateTimeField(auto_now_add=True)
