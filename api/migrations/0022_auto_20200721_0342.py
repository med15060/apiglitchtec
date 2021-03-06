# Generated by Django 3.0.6 on 2020-07-21 03:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20200719_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderid',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Balancerate',
            field=models.FloatField(default=0.8),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 21, 3, 42, 0, 334776)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 21, 3, 42, 0, 331231, tzinfo=utc)),
        ),
    ]
