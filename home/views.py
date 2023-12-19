from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Home Page for the app

def home(request):
  return render(request, 'home/home.html')



def documentation(request):
  return render(request, 'home/documentation.html')



def underconstruction(request):
  return render(request, 'underconstruction.html')