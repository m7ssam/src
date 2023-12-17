from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.mp_home, name = 'mp_home'),
    path('user_page/<str:pk>/', views.user_page, name = 'user_page'),
    path('mp_list/', views.mp_list, name = 'mp_list'),
    path('mp_search/', views.mp_search, name = 'mp_search'),
    path('mp_search_list/', views.mp_search_list, name = 'mp_search_list'),
    path('mplist', login_required(views.MpList.as_view()) , name = 'mplist'),
]