from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
        path("", include("django.contrib.auth.urls")),
        path('sign-up', views.sign_up, name = 'sign_up'),
        path('login', views.login, name = 'login'),
        path('logout_user', views.logout_user, name = 'logout_user'),
        path('created', views.created, name = 'created'),
        path('invalid_user', views.invalid_user, name = 'invalid_user'),
        path('dublication', views.dublication, name = 'dublication'),
        path('password_change', views.password_change, name = 'password_change'),
]



        # path('login/', views.CustomLoginView.as_view(), name='login'),