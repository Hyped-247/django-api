# Generated by Django 2.1.3 on 2019-01-11 01:13

from django.db import migrations, models
import status.models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_auto_20181211_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=status.models.upload_status_image),
        ),
    ]
