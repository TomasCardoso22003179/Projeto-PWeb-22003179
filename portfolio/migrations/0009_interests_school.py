# Generated by Django 3.2.13 on 2022-06-12 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_subject_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='portfolio/static/portfolio/images')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.IntegerField(default=0)),
                ('end_date', models.IntegerField(default=0)),
                ('link_school', models.URLField(max_length=405)),
                ('image', models.ImageField(null=True, upload_to='portfolio/static/portfolio/images')),
            ],
        ),
    ]
