# Generated by Django 3.0.6 on 2020-08-04 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20200805_0400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messageinfo',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='messageinfo',
            name='color',
        ),
        migrations.RemoveField(
            model_name='messageinfo',
            name='ddate',
        ),
        migrations.RemoveField(
            model_name='messageinfo',
            name='file',
        ),
        migrations.RemoveField(
            model_name='messageinfo',
            name='food',
        ),
        migrations.AddField(
            model_name='quizzinfo',
            name='bio',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='quizzinfo',
            name='color',
            field=models.CharField(choices=[('Red', 'Red'), ('Green', 'Green'), ('Blue', 'Blue')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='quizzinfo',
            name='ddate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='quizzinfo',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='quizzinfo',
            name='food',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
