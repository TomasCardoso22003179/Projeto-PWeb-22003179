# Generated by Django 3.2.13 on 2022-05-28 20:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=60)),
                ('data', models.DateField(default=datetime.datetime.now)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1000)),
                ('link', models.URLField(default='www.google.com')),
                ('image', models.ImageField(default='', upload_to='')),
                ('date_criated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]