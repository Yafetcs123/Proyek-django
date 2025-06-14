from django.contrib import admin
from django.urls import path, include
from .views import index, Login, logoutt
urlpatterns =[
    path('logoutt', logoutt, name='logoutt'),
    path('Login', Login, name='Login'),
    path('index', index, name='index'),
    path('', include("main.urls")),
    path('admin/', admin.site.urls),
]
