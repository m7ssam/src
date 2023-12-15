from django.shortcuts import render


# Home Page for the app
def test_home(request):
  return render(request, 'tester/home.html')



