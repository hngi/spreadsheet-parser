# Generated by Django 3.0.8 on 2020-07-10 01:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='excelupload',
            name='name',
        ),
        migrations.AlterField(
            model_name='excelupload',
            name='document',
            field=models.FileField(blank=True, upload_to='user/', validators=[django.core.validators.FileExtensionValidator(['xlsx'])]),
        ),
    ]
