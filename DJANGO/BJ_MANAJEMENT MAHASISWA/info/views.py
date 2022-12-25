from django.shortcuts import render
from django.shortcuts import render
from .models import pos
# Create your views here.
def info(request):
    posts = pos.objects.all()
    context = {
        'judul':'Info',
        'icon':'/img/djangoproject.svg',
        'user':'/img/elqusairi.png',
        'post':posts,
    }
    return render (request,'info/info.html',context)
