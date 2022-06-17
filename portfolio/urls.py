from . import views
from django.urls import path

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view),
    path('home', views.home_page_view, name='home'),
    path('blog', views.blog_page_view, name='blog'),
    path('newBlog', views.new_blog_post, name='newBlog'),
    path('editBlog/<int:blog_id>', views.edit_blog_post, name='editBlog'),
    path('deleteBlog/<int:blog_id>', views.delete_blog_post, name='deleteBlog'),


    path('newProject', views.new_project, name='newProject'),
    path('editProject/<int:project_id>', views.edit_project, name='editProject'),
    path('deleteProject/<int:project_id>', views.delete_project, name='deleteProject'),


    path('project', views.projects_page_view, name='project'),

    path('about_me', views.subjects_view, name='about_me'),
    path('edit_subject/<int:subject_id>', views.edit_subjects, name='edit_subject'),

    path('web', views.web_page_view, name='web'),

    path('login', views.view_login, name='login'),
    path('logout', views.view_logout, name='logout'),

    path('contacts', views.contacts_page_view,name = 'contacts')

]
