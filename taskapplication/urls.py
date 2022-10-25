"""taskapplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from unicodedata import name
from django.contrib import admin
from django.urls import path
from taskapp.views import IndexView,LoginView,SignupView,TaskAddView,TaskListView,TastDetailView,TaskDeleteView,RegistrationView,SigninView,signout_view,TaskUpdateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",IndexView.as_view()),
    path("login/",LoginView.as_view()),
    path("register/",RegistrationView.as_view(),name="register"),
    path("todos/add/",TaskAddView.as_view(),name="todo-add"),
    path("todos/all/",TaskListView.as_view(),name="todo-all"),
    path("todos/<int:id>",TastDetailView.as_view(),name="todo-detail"),
    path("todos/<int:id>/delete",TaskDeleteView.as_view(),name="todo-delete"),
    path("",SigninView.as_view(),name="signin"),  #for openinig signin directly "" given
    path("signout",signout_view,name="signout"),
    path("todos/all/<int:id>/update",TaskUpdateView.as_view(),name="todo-update")
]
