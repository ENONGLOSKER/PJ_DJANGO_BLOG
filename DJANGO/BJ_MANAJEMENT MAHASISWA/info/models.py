from django.db import models

# Create your models here.
class pos(models.Model):
    title = models.CharField(max_length=255)
    body  = models.TextField()
    jenis = models.CharField(max_length=255, default="berita")
    waktu = models.DateTimeField(auto_now_add= True)

    # merubah nama pos objek
    def __str__(self):
        return "{}".format(self.title)