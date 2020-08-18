# Generated by Django 3.0.6 on 2020-08-06 16:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_auto_20200806_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 16, 57, 3, 704572, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 22, 57, 3, 706572)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 16, 57, 3, 701574, tzinfo=utc)),
        ),
    ]