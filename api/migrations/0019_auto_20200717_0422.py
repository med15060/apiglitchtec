# Generated by Django 3.0.6 on 2020-07-17 04:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20200715_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_media',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_media',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 4, 22, 23, 814186)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 4, 22, 23, 809273, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
