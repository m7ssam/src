from django import forms
from django.contrib.auth.models import User
from .models import Project


class PostProject(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['recipient','project_name','photo']


   