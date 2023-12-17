from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.db import IntegrityError
from django import forms
from django.views import View
from manpower.models import Mp_list
from django.contrib.auth.decorators import login_required
# from .forms import CustomAuthenticationForm
# from django.contrib.auth.views import LoginView
# from django.urls import reverse_lazy
# from django.views.generic import FormView

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_id_input = form.cleaned_data.get("id")
            # Check if the user ID exists in the User_id model
            if Mp_list.objects.filter(id=user_id_input).exists():
                user_record = Mp_list.objects.get(id=user_id_input)
                first_name = user_record.first_name
                last_name = user_record.last_name
                try:
                  user.username = user_id_input
                  user.first_name = first_name
                  user.last_name = last_name
                  user.is_active = True
                  user.save()
                  login(request, user)
                  return redirect("/accounts/created")
                except IntegrityError:
                  return redirect("/accounts/dublication")
            else:
                return redirect("/accounts/invalid_user")  
    else:
        form = RegisterForm()
    return render(request, "registration/sign_up.html", {"form": form})



# class CustomLoginView(LoginView):
#     template_name = 'login.html'  
#     authentication_form = CustomAuthenticationForm
#     success_url = reverse_lazy('success_url_name')

# class CustomLoginViewWithExtraContext(FormView):
#     template_name = 'login.html'
#     form_class = CustomAuthenticationForm
#     success_url = reverse_lazy('success_url_name')
#     def form_valid(self, form):
#         return super().form_valid(form)



def logout_user(request):
  logout(request)
  return redirect("/accounts/login/")

def created(request):
  return render(request, 'registration/created.html')

def dublication(request):
  return render(request,"registration/dublication.html")

def invalid_user(request):
  return render(request, 'registration/invalid.html')

def password_change(request):
  return render(request,"registration/password_change.html")




