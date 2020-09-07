from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Task
from .forms import Taskform
# Create your views here.
@login_required(login_url="user_login")
def home(request):

    form=Taskform()
    tasks=Task.objects.all()
    if request.method=="POST":
        form=Taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    data={ 'tasks':tasks ,'form':form}
    return render(request,"to_do/home.html",data)


@login_required(login_url="user_login")
def update(request,pk):
    task=Task.objects.get(id=pk)
    if request.method=="POST":
        form=Taskform(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('to_do_home')
    else:
        form=Taskform(instance=task)


    data={'form':form}
    return render(request,"to_do/update.html",data)

@login_required(login_url="user_login")
def delete(request,pk):
    task=Task.objects.get(id=pk)
    if request.method=="POST":
        task.delete()
        return redirect("to_do_home")
    return render(request,"to_do/delete.html")


