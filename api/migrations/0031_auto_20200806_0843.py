# Generated by Django 3.0.6 on 2020-08-06 06:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20200806_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 6, 43, 8, 387536, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 8, 43, 8, 389566)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 6, 43, 8, 383546, tzinfo=utc)),
        ),
    ]