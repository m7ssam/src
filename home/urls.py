from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('documentation', views.documentation, name = 'documentation'),
    path('documentation_ar', views.documentation_ar, name = 'documentation_ar'),
    path('underconstruction', views.underconstruction, name = 'underconstruction'),
]