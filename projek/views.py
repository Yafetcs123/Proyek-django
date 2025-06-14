from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    context = {
        'title':'hallo'
    }
    return render(request, 'index.html', context)

def Login(request):
    user = None
    if request.method == 'POST':
        username_input = request.POST['username']
        password_input = request.POST['password']
        user = authenticate(request, username=username_input, password=password_input)
        if user is not None:
            login(request, user)
        return redirect('index')
    context = {
        'title':'hallo'
    }
    return render(request, 'login.html', context)


def logoutt(request):
   if request.method == 'POST':
       if request.POST["logout"] == "Submit":
           logout(request)
           return redirect('index')
   context = {
        'page':'holla'
    }
   return render(request, 'logout.html', context)