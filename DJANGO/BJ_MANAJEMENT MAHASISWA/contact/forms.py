from django import forms

class kontak (forms.Form):
    Kontak_in = forms.CharField()
    Nomor_in  = forms.CharField()
    Alamat_in = forms.CharField()