# Generated by Django 3.2.13 on 2022-06-13 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='skill_number',
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default=1, upload_to='portfolio/static/portfolio/images'),
            preserve_default=False,
        ),
    ]
