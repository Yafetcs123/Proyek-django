from django.shortcuts import render

# Create your views here.
def main(request):
    context={
      'page_title':'Selamat Datang',
    }
    return render(request, 'main.html', context)