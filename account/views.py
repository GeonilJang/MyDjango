# account/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import SignupForm
# Create your views here.

@login_required
def profile(request):
    return render(request,"accounts/profile.html")


def login(request):
    return render(request,"account/login.html")


def signup(request):
    if request.method =="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()

    return render(request, 'accounts/signup_form.html',{
        'form':form,
    })
