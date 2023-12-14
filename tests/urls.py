from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
  path('', views.test_home, name = 'test_home'),
]