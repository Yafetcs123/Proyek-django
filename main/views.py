from django.shortcuts import render

# Create your views here.
def main(request):
    context = {
      'page':'holla',
    }
    return render(request, 'main.html', context)