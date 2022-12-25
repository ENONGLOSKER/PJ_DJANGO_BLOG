from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'Home',
        'icon':'/img/djangoproject.svg',
        'user':'/img/elqusairi.png',
    }
    return render(request,'index.html',context)
    