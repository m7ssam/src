from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'project_home'),
    path('plist', views.projects, name = 'project_list'),
    
]