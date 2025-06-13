from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate

class IndexView(TemplateView):
    template_name = 'index.html'
def index(request):
    context = {
        'title':'hallo'
    }
    return render(request, 'index.html', context)

def login(request):
    if request.method == 'POST':
        username_input = request.POST['username']
        password_input = request.POST['password']
        user = authenticate(username=username_input, password=password_input)
        if user is not None:
            login(request, user)
        redirect('index')
    context = {
        'title':'hallo'
    }
    return render(request, 'login.html', context)