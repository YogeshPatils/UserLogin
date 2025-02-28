from django import forms
from django.contrib.auth.models import User


class UserSignUpForm(forms.Form):
    # class Meta:
    #     model=User
    #     fields=['first_name','last_name','username','username','password']
    first_name=forms.CharField(max_length=200)
    last_name=forms.CharField(max_length=200)
    email=forms.EmailField(max_length=100)
    username=forms.CharField(max_length=200)
    password1=forms.CharField(max_length=100,widget=forms.PasswordInput)
    password2=forms.CharField(max_length=100,widget=forms.PasswordInput)
    

class UserLoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput())
    

