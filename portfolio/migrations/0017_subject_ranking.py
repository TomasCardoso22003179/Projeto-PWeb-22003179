# Generated by Django 3.2.13 on 2022-06-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_tfc'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='ranking',
            field=models.IntegerField(default=0),
        ),
    ]