from sqlite3 import IntegrityError
from tokenize import Name
from unicodedata import name
from django.db import models
from datetime import datetime

# Create your models here.

class Blog(models.Model):
      author =  models.CharField(max_length = 60)
      data = models.DateField(default=datetime.now)
      title = models.CharField(max_length=30)
      description = models.CharField(max_length= 1000)
      link = models.URLField(blank=True)
      image = models.ImageField(upload_to='portfolio/static/portfolio/images', blank=True)
      date_criated = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return f"{self.title}"

class QuizzScore(models.Model):
        name = models.CharField(max_length=20)
        score = models.IntegerField() 

        def __str__(self):
            return f"{self.name};{self.score}"


class Picture(models.Model):
        name = models.CharField(max_length=100)
        image = models.ImageField(upload_to='portfolio/static/portfolio/images', blank=True)

        def __str__(self):
            return f"{self.name}"

    

class Person(models.Model):
        name = models.CharField(max_length=40)
        age = models.IntegerField(null=True)
        link_linkedin = models.URLField(max_length=400, blank=True)
        link_lusofona = models.URLField(max_length=400, blank=True)

        def __str__(self):
            return f"{self.name}"

class Project(models.Model):
        name_of_projects = models.CharField(max_length=40)
        image = models.ImageField(upload_to = 'portfolio/static/portfolio/images')
        description = models.TextField(blank=True)
        year = models.IntegerField(default=0)
        participants_in_projects = models.ManyToManyField(Person)
        github = models.TextField(default = "")

        
        def __str__(self):
            return f"{self.name_of_projects}"

class ProgrammingLanguages(models.Model):
        name = models.CharField(max_length=40)
        image = models.ImageField(upload_to = 'portfolio/static/portfolio/images')
        description = models.TextField(blank=True)
        link_wiki = models.URLField(max_length=400)

        
        def __str__(self):
            return f"{self.name}"

class Subject(models.Model):
        name = models.CharField(max_length=100)
        year = models.IntegerField(default=0)
        semester = models.IntegerField(default=0)
        etcs = models.IntegerField(default=0)
        description = models.TextField(blank=True)
        programing_languages = models.ManyToManyField(ProgrammingLanguages)
        teacher = models.ManyToManyField(Person)
        projetos = models.ManyToManyField(Project)
        link_lusofona = models.URLField(max_length=405)
        ranking = models.IntegerField(default=0)

        def __str__(self):
            return f"{self.name}"

class School(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.IntegerField(default=0)
    end_date = models.IntegerField(default=0)
    link_school = models.URLField(max_length=405)
    image = models.ImageField(upload_to = 'portfolio/static/portfolio/images', null=True)

    def __str__(self):
        return f"{self.name}"



class Interests(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='portfolio/static/portfolio/images')
    
    def __str__(self):
        return f"{self.name}"

class Skills(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length= 400 ,default= "nothing")
    skill_number = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"


class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length= 10000 ,default= "nothing")
    link_news = models.URLField(max_length=405)
    image = models.ImageField(upload_to='portfolio/static/portfolio/images')


    def __str__(self):
        return f"{self.title}"

class Tfc(models.Model):
    authors = models.ManyToManyField(Person)
    teacher = models.CharField(max_length=200)
    year = models.IntegerField(default = 0)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/static/portfolio/images')
    link_video = models.URLField(max_length=400)
    link_github = models.URLField(max_length=400)
    paper =  models.URLField(max_length=400)    

    def __str__(self):
        return f"{self.title}"
