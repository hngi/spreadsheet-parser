# Generated by Django 3.0.8 on 2020-07-13 14:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parse', '0004_cdnupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelupload',
            name='document',
            field=models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['xlsx'])]),
        ),
    ]
