from django import forms
from django.contrib.auth.models import User
from .models import Mp_Location, Mp_list


class Mp_move(forms.ModelForm):
  class Meta:
    model = Mp_Location
    fields = ['id','recipient']



class Mp_search(forms.ModelForm):
  class Meta:
    model = Mp_list
    fields = ["id","full_name","code","gender","contract","gov","national_id"]



   