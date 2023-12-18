from django.shortcuts import render, redirect
from .forms import Mp_move
from .models import Mp_location_test, Eqp_list_test
from manpower.models import Mp_list
from django.db import IntegrityError
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

# Home Page for the app
@login_required()
def test_home(request):
  return render(request, 'tests/home.html')

# ------------------- Man Power Test -----------------------------------------------#
# Home Page for the app
@login_required()
def manpower_test(request):
  return render(request, 'tests/manpower_test_home.html')

@login_required()
def mp_have_move_req(request):
  return render(request, 'tests/mp_have_move_req.html')

@login_required()
def mp_move_list(request):
  list = Mp_location_test.objects.all()
  form = Mp_move()
  if request.method == "POST":
      pk = request.POST.get("delete")
      td = Mp_location_test.objects.get(id = pk)
      td.delete()
  context = {"list": list, "form" : form}
  return render(request, 'tests/mp_move_list.html', context)

@login_required()
def manpower_test_move(request):
  if request.method == "POST":
    form = Mp_move(request.POST)
    if form.is_valid():
      form_data = form.save(commit=False)
      user_id_input = form.cleaned_data.get("id")
      if Mp_list.objects.filter(id=user_id_input).exists():
        mp_record = Mp_list.objects.get(id=user_id_input)
        mp_name = f"{mp_record.first_name} {mp_record.last_name}"
        try:
          form_data.name = mp_name
          form_data.save()
          return redirect("mp_move_list")
        except IntegrityError:
          return redirect("mp_have_move_req")
      else:
        return redirect("mp_have_move_req")  
  else:
    form = Mp_move()
  context = {"form" : form}
  return render(request, 'tests/manpower_test_move.html', context)



# ------------------- Equipment Test -----------------------------------------------#

def eqp_list_test(request):
  return render(request, 'tests/home.html')

class EqpList_test(ListView):
  model = Eqp_list_test
