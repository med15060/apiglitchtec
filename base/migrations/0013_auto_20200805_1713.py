# Generated by Django 3.0.6 on 2020-08-05 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20200805_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizz',
            name='filee',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
