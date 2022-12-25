from django.shortcuts import render

# Create your views here.
def skills(request):
    context = {
        'judul':'Skills',
        'icon':'/img/djangoproject.svg',
    }
    return render(request,'skills/skills.html',context)