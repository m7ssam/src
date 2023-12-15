from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
def mp_home():
  pass


@login_required()
def user_page(request,pk):
  target_user = Mp_list.objects.get(id = pk)
  context = {"target_user": target_user}
  return render(request, "manpower/user_page.html", context)