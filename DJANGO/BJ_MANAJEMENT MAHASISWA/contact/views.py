from contextvars import Context
from django.forms import forms
from django.shortcuts import render
from .forms import kontak

# Create your views here.
def contact(request):
    kontak_form = kontak()
    context ={
        'judul':'Contact',
        'icon':'/img/djangoproject.svg',
        'user':'/img/elqusairi.png',
        'kontak_f':kontak_form
    }
    if request.method == "POST":
            context["Kontak_in"] = request.POST["Kontak_in"]
            context["Nomor_in"] = request.POST["Nomor_in"]
            context["Alamat_in"] = request.POST["Alamat_in"]

    return render(request,'contact/contact.html',context)