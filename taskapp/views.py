
import imp
from django.shortcuts import render,redirect
from django.views.generic import View,ListView,DetailView,UpdateView
from taskapp.models import Task
from taskapp.forms import RegistrationForm,LoginForm,TaskUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
# Create your views here.

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"you must login")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper


class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        forms=RegistrationForm(data=request.POST)
        if forms.is_valid():
            User.objects.create_user(**forms.cleaned_data)
            # forms.save()
            messages.success(request,"registration completed")
            return redirect("signin")
        else:
            messages.success(request,"registration failed")
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
                messages.success(request,"login success")
                return redirect("todo-all")
            else:
                messages.error(request,"invalid credentials")
                return render(request,"signin.html",{"form":form})
@signin_required
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
@method_decorator(signin_required,name="dispatch")
class TaskAddView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add_task.html")
    def post(self,request,*args,**kwargs):
        # print(request.POST)
        username=request.user
        task=request.POST.get("task")
        Task.objects.create(user=username,task_name=task)
        messages.success(request,"task has been added")
        return redirect("todo-all")
@method_decorator(signin_required,name="dispatch")
class TaskListView(ListView):
    model=Task
    template_name="list-tasks.html"
    context_object_name="todos"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    # def get(self,request,*args,**kwargs):
    #     if request.user.is_authenticated:    #user logined or not
    #         all_tasks=Task.objects.filter(user=request.user)       #for geting the tasks of logined user used the filter fn
    #         # all_tasks=request.user.task_set.all()
    #         return render(request,"list-tasks.html",{"todos":all_tasks})
    #     else:
    #         return redirect("signin")
@method_decorator(signin_required,name="dispatch")
class TastDetailView(DetailView):
    model=Task
    template_name="task-detail.html"
    context_object_name="todo"
    pk_url_kwarg="id"
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     task=Task.objects.get(id=id)
    #     return render(request,"task-detail.html",{"todo":task})
@method_decorator(signin_required,name="dispatch")
class TaskDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        task=Task.objects.get(id=id)
        task.delete()
        messages.success(request,"task deleted")
        return redirect("todo-all")

class TaskUpdateView(UpdateView):
    model=Task
    form_class=TaskUpdateForm
    template_name="todo-update.html"
    pk_url_kwarg="id"
    success_url=reverse_lazy("todo-all")

