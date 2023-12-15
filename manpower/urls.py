from django.urls import path
from . import views

urlpatterns = [
    path('', views.mp_home, name = 'mp_home'),
    path('user_page/<str:pk>/', views.user_page, name = 'user_page'),
]