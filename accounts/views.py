import imp
from re import I
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == 'POST':
        user_form = SignUpForm(data=request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid():
            new_user = user_form.save()
            new_profile = profile_form.save()
            new_profile.user = new_user
            new_profile.save()
            messages.success(request, "Register Successfully")
            return redirect('/accounts/login-user/')
        else:
            print(user_form.errors)
            print(profile_form.errors)
    else:
        user_form = SignUpForm()
        profile_form = UserProfileForm()

    context = {'user_form' : user_form, 'profile_form':profile_form}

    return render(request , 'registration/register.html' , context)

def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login Successfully")
            return redirect('/')
        else:
            messages.success(request, "Invalid User")
            return redirect('/accounts/login-user/')
    return render(request , 'registration/login.html' , locals())

@login_required
def profile(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if profile_form.is_valid():
            newuser = profile_form.save()
            newuser.user.email = request.POST['email']
            newuser.user.first_name = request.POST['first_name']
            newuser.user.last_name = request.POST['last_name']
            newuser.user.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('/profile/')
        else:
            print(profile_form.errors)
            messages.error(request, "There was an error updating your profile.")
    else:
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'registration/profile.html', locals())