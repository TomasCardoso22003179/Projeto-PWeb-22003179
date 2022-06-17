from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Blog)
admin.site.register(QuizzScore)
admin.site.register(Picture)
admin.site.register(Person)
admin.site.register(Project)
admin.site.register(ProgrammingLanguages)
admin.site.register(Subject)
admin.site.register(School)
admin.site.register(Interests)
admin.site.register(Skills)
admin.site.register(News)
admin.site.register(Tfc)