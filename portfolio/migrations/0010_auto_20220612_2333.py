# Generated by Django 3.2.13 on 2022-06-12 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_interests_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
