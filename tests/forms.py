from django import forms
from django.contrib.auth.models import User
from .models import project_name_test, client_name_test, Mp_location_test
from manpower.models import Mp_list

class Mp_move(forms.ModelForm):
  class Meta:
    model = Mp_location_test
    fields = ['id','recipient']





   