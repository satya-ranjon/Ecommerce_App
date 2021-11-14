from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse

# Authentication 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

#forms and models
from .models import Profile
from .froms import ProfileForm,SingUpForm,LoginForm,ChangeUsPassword

#Messages
from django.contrib import messages

# Create your views here.

def Sign_Up(request):
    form = SingUpForm()
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Accound Create Successfully')
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'User_App/sign_up.html', context={'form':form, 'title':'sign up '})



def Login_User(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,'You Have login successfully')
                return HttpResponseRedirect(reverse('shop'))
    return render (request,'User_App/login.html',context={'form':form,'title':'login !'})



@login_required()
def Logout_User(request):
    logout(request)
    messages.warning(request, "You are logged out!!")
    return HttpResponseRedirect(reverse('shop'))


@login_required()
def User_Ch_Profile(request):
    current_user_profile = Profile.objects.get( user = request.user)
    form = ProfileForm(instance=current_user_profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=current_user_profile)
        if form.is_valid():
            form.save()
            form = ProfileForm(instance=current_user_profile)
            messages.warning(request, 'Save Successfully !')
            return HttpResponseRedirect(reverse('user_ch_pro'))
    return render(request,'User_App/change_profile.html',{'form':form})


@login_required()
def Change_Password(request):
    form = ChangeUsPassword(request.user)
    if request.method == 'POST':
        form = ChangeUsPassword(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Your password change successfully')
            return HttpResponseRedirect(reverse('shop'))
    return render(request,'User_App/change_password.html',{'form':form})