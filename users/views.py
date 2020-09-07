from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm,UserUpdateForm,ProfileUpdateForm
# Create your views here.

def UserRegister(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account has been created for {username} !')
            return redirect('to_do_home')
    else:
        form=SignupForm()
    data={'form':form}
    return render(request,'users/register.html',data)



@login_required(login_url='user_login')
def Userprofile(request):
    if request.method=="POST":
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Data has been updated!')
            return redirect('user_profile')

    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)


    data={'u_form':u_form,'p_form':p_form}
    return render(request,"users/profile.html",data)






