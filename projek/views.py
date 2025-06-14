from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'title':'hallo'
    }
    template_name = None
    if request.user.is_authenticated:
       template_name = 'user.html'
    else:
        template_name = 'ano.html'
    return render(request, template_name, context)

def Login(request):
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
    if request.user.is_authenticated:
           return redirect('index')
    else:
        return render(request, 'login.html', context)
@login_required
def logoutt(request):
   if request.method == 'POST':
       if request.POST["logout"] == "Submit":
           logout(request)
           return redirect('index')
   context = {
        'page':'holla'
    }
   return render(request, 'logout.html', context)