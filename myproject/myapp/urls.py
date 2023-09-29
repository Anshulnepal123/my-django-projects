from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('new-blog', views.new_blog,name='new_blog'),
    path('old-blog',views.old_blog,name='old-blog'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
    path("blogdetails/<blogid>",views.blogdetails,name='blogdetails'),
    path('delete/<blogid>',views.delete,name='delete'),
    path('editblog/<editid>',views.editblog,name='editblog')
]
