# Generated by Django 3.0.6 on 2020-08-04 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('rate', models.CharField(max_length=255)),
                ('specializes', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('conuntry', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('password2', models.CharField(max_length=255)),
                ('introduction', models.CharField(max_length=255)),
            ],
        ),
    ]
