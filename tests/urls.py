from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
  path('', views.test_home, name = 'test_home'),
  # -----------Manpower Test
  path('manpower_test', views.manpower_test, name = 'manpower_test'),
  path('manpower_test_move', views.manpower_test_move, name = 'manpower_test_move'),
  path('mp_have_move_req', views.mp_have_move_req, name = 'mp_have_move_req'),
  path('mp_move_list', views.mp_move_list, name = 'mp_move_list'),
  # -----------Equipment Test
  path('eqp_list_test', views.eqp_list_test, name = 'eqp_list_test'),
  path('eqplist', login_required(views.EqpList_test.as_view()), name = 'eqplist'),
]