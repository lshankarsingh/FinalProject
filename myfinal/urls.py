
from django.contrib import admin
from django.urls import path,include
from FinalApp import views as task_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',task_views.index,name='index'),
    path('task',include('FinalApp.urls')),
    path('account/',include('UserApp.urls')),
    path('contact',task_views.contact,name='contact'),
    path('about',task_views.about,name='about'),
    
]
