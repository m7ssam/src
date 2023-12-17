from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
  path('', views.test_home, name = 'test_home'),
  path('manpower_test', views.manpower_test, name = 'manpower_test'),
  path('manpower_test_move', views.manpower_test_move, name = 'manpower_test_move'),
  path('mp_have_move_req', views.mp_have_move_req, name = 'mp_have_move_req'),
  path('mp_move_list', views.mp_move_list, name = 'mp_move_list'),
]