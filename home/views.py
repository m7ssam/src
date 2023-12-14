from django.shortcuts import render

# Home Page for the app
def home(request):
  return render(request, 'home/home.html')
