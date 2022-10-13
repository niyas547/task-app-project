from django.shortcuts import render
from django.views.generic import View
from taskapp.models import Task
# Create your views here.

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")
class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"login.html")
class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"registration.html")
class TaskAddView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add_task.html")
    def post(self,request,*args,**kwargs):
        print(request.POST)
        username=request.POST.get("username")
        task=request.POST.get("task")
        Task.objects.create(user=username,task_name=task)
        return render(request,"add_task.html")
class TaskListView(View):
    def get(self,request,*args,**kwargs):
        all_tasks=Task.objects.all()
        return render(request,"list-tasks.html",{"todos":all_tasks})