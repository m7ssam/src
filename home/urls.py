from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('documentation', views.documentation, name = 'documentation'),
    path('underconstruction', views.underconstruction, name = 'underconstruction'),
]