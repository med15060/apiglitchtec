# Generated by Django 3.0.6 on 2020-08-04 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_status',
            field=models.CharField(choices=[('verified', 'verified'), ('Pending', 'Pending'), ('Declined', 'Declined')], max_length=200, null=True),
        ),
    ]
