import re
from telnetlib import LOGOUT
from django.shortcuts import render,redirect
from django.views.generic import View
from taskapp.models import Task
from taskapp.forms import RegistrationForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        forms=RegistrationForm(data=request.POST)
        if forms.is_valid():
            User.objects.create_user(**forms.cleaned_data)
            # forms.save()
            return redirect("todo-all")
        else:
           return render(request,"register.html",{"form":form})
class SigninView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"signin.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                return redirect("todo-all")
            else:
                return render(request,"signin.html",{"form":form})

def signout_view(request,*args,**kwargs):   #use python fn method
    logout(request)
    return redirect("signin")
    
 
class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")
class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"login.html")
class SignupView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"registration.html")
class TaskAddView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add_task.html")
    def post(self,request,*args,**kwargs):
        # print(request.POST)
        username=request.user
        task=request.POST.get("task")
        Task.objects.create(user=username,task_name=task)
        return redirect("todo-all")
class TaskListView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:    #user logined or not
            all_tasks=Task.objects.filter(user=request.user)       #for geting the tasks of logined user used the filter fn
            # all_tasks=request.user.task_set.all()
            return render(request,"list-tasks.html",{"todos":all_tasks})
        else:
            return redirect("signin")
class TastDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        task=Task.objects.get(id=id)
        return render(request,"task-detail.html",{"todo":task})
class TaskDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        task=Task.objects.get(id=id)
        task.delete()
        return redirect("todo-all")


