# Generated by Django 3.2.13 on 2022-06-13 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_auto_20220613_0312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tfc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.CharField(max_length=200)),
                ('year', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='portfolio/static/portfolio/images')),
                ('link_video', models.URLField(max_length=400)),
                ('link_github', models.URLField(max_length=400)),
                ('paper', models.URLField(max_length=400)),
                ('authors', models.ManyToManyField(to='portfolio.Person')),
            ],
        ),
    ]