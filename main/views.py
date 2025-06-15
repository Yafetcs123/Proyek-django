from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import Group
# Create your views here.
def main(request):
    context = {
      'page':'holla',
    }
    gr = Group.objects.get(name="Admin")
    usn = request.user.groups.all()
       
    if gr in usn:
        return render(request, 'pem.html', context)
    else:
        return render(request, 'no.html', context)
    return render(request, 'ma.html', context)