from django import forms
from django.forms import ModelForm
from .models import *


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

        widgets = {

            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'O seu nome completo '}),
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Insira aqui o title do seu novo post.'}),
            'description' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Faça uma breve descrição do seu post.'}),
            'link' : forms.URLInput(attrs={'class' : 'form-control', 'placeholder' : 'www.google.com'})
            

        }

        labels = {
            'author' : 'Autor',
            'title' : 'Título',
            'data' : 'Data',
            'description' : 'Descrição',
            'image' : 'Imagem',



        }

        help_texts = {
            'data' : 'Meta a data na ordem : YYYY/MM/DD'
        }


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'



class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class WebForm(ModelForm):
    class Meta:
        model = News
        fields = '__all__'