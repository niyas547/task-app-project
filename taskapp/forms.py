from tkinter import Widget
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","password","email"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control border border-info","placeholder":"enter firstname"}),
            "last_name":forms.TextInput(attrs={"class":"form-control border border-info","placeholder":"enter lastname" }),
            "username":forms.TextInput(attrs={"class":"form-control border border-info","placeholder":"enter username"}),
            "password":forms.PasswordInput(attrs={"class":"form-control border border-info","placeholder":"enter password"}),
            "email":forms.EmailInput(attrs={"class":"form-control border border-info","placeholder":"enter email"})
        }
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info","placeholder":"enter username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control border border-info","placeholder":"enter password"}))