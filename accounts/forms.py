from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(UserCreationForm):
    id = forms.IntegerField(required=True)
    class Meta:
        model = User
        fields = ["id", "password1", "password2"]
        field_order = ["id", "password1", "password2"]


# class CustomAuthenticationForm(AuthenticationForm):
#     username = forms.CharField(
#         label="ID",
#         widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'الرقم المالى'}),
#     )
#     password = forms.CharField(
#         label="Password",
#         widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
#     )



        
