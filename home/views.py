from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Home Page for the app
@login_required()
def home(request):
  return render(request, 'home/home.html')


@login_required()
def documentation(request):
  return render(request, 'home/documentation.html')


@login_required()
def underconstruction(request):
  return render(request, 'underconstruction.html')