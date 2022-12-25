from django.shortcuts import render
from .models import database
# Create your views here.
def about(request):
    data = database.objects.all()
    context ={
        'judul':'About',
        'icon' : '/img/djangoproject.svg',
        'icon':'/img/djangoproject.svg',
        'user':'/img/elqusairi.png',
        'datas':data
    }
    return render(request,'about/about.html',context)