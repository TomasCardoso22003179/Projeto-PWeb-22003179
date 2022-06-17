from urllib import request
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
import datetime
from matplotlib import pyplot as plt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .models import * 
from .forms import *
# Create your views here.

def view_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas.'
            })

    return render(request, 'portfolio/login.html')


def view_logout(request):
    logout(request)
    return render(request, 'portfolio/login.html', {
                'message': 'Foi desconetado.'})



def blog_page_view(request):
    context = {'posts' : Blog.objects.all()}
    return render(request, 'portfolio/blog.html', context)


def new_blog_post(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}

    return render(request, 'portfolio/blog_new_post.html', context)



@login_required
def edit_blog_post(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    form = BlogForm(request.POST or None, instance=blog)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'blog_id': blog_id}
    return render(request, 'portfolio/blog_edit.html', context)

    

def delete_blog_post(request, blog_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:blog'))
    Blog.objects.get(id=blog_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))

    

def quizz_score(request):
    questScore = 0
    if request.POST.get("question1") == 'Hypertext Markup Language':
        questScore += 4
    if request.POST.get('question2') == False:
        questScore += 5
    if request.POST.get('question3') == True:
        questScore += 6
    if request.POST.get('question4') == '2005':
        questScore += 2
    if request.POST.get('question5') == True:
        questScore += 1
    
    return questScore

def quizz(request):
    if request.method == 'POST':
        n = request.POST["name"]
        p = quizz_score(request)
        r = QuizzScore(name=n, score=p)
        r.save()
        design_graphics(QuizzScore.objects.all())

    return render(request, 'portfolio/web.html')

def design_graphics(objects):

    data = sorted(objects, key=lambda t: t.score, reverse=True)
    plt.figure(figsize=(10, 5))
    plt.barh(data.keys(),data.values())
    plt.title("Pontuação dos Users")
    plt.xlabel("Nomes")
    plt.ylabel("Pontuação")
    plt.savefig('portfolio/static/portfolio/images/final_graphic.png')

def quizz_page_view(request):
    name = request.POST['name']
    question1 = request.POST('question1')
    question2 = request.get('question2')
    question3 = request.get('question3')
    question4 = request.get('question4')
    question5 = request.get('question5')
    Quizz = (name,question1,question2,question3,question4,question5)
    Quizz.save()
    quizz(Quizz)
    form = QuizzForm(request.POST, use_required_attribute=False)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.path_info)

    context = {'form': form}

    return render(request, 'portfolio/quizz.html', context)


def subjects_view(request):
    context = {'subject': Subject.objects.all, 'school' : School.objects.all, 'interest' : Interests.objects.all, 'skill' : Skills.objects.all}
    return render(request, 'portfolio/about_me.html', context)

@login_required
def edit_subjects(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    form = SubjectForm(request.POST or None, instance=subject)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('about_me'))
        

    context = {'form':form, 'subject_id':subject_id}
    return render(request, 'portfolio/edit_subject.html', context)


    
def home_page_view(request):
	return render(request, 'portfolio/layout.html')

def degree_page_view(request):
    return render(request, 'portfolio/degree.html')

def contacts_page_view(request):
    context = {'person' : Person.objects.all}
    return render(request, 'portfolio/contacts.html',context)

def projects_page_view(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:project'))
    context = {'project': Project.objects.all, 'tfcs' : Tfc.objects.all}
    return render(request, 'portfolio/project.html', context)


def new_project(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:project'))

    context = {'form': form }

    return render(request, 'portfolio/new_project.html', context)


@login_required
def edit_project(request, project_id):
    project = Project.objects.get(id=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:project'))

    context = {'project_id': project_id}
    return render(request, 'portfolio:edit_project.html', context)

def delete_project(request, project_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:project'))
    Project.objects.get(id=project_id).delete()
    return HttpResponseRedirect(reverse('portfolio:project'))


def web_page_view(request):
    form = WebForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:web'))
    context = {'programming_languages' : ProgrammingLanguages.objects.all, 'noticias' : News.objects.all, 'project': Project.objects.all}
    return render(request, 'portfolio/web.html', context)


def about_me_page_view(request):
    return render(request, 'portfolio/about_me.html')

def resolution_path(instance, filename):
    return f'users/{instance.id}/'