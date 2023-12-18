from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def eqp_home(request):
  return render(request, 'eqp/eqp_home.html')
