from distutils.command.upload import upload
from django.db import models

# Create your models here.
class database(models.Model):
    img     = models.ImageField(upload_to="img")
    nama    = models.CharField(max_length=255)
    bidang  = models.CharField(max_length=255, default="Programming")
    nim     = models.CharField(max_length=255)
    progres = models.IntegerField()
    email   = models.EmailField()
    waktu  = models.DateTimeField(auto_now_add= True)

    # merubah nama pos objek
    def __str__(self):
        return "{}".format(self.nama)