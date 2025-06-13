from django.db import models

class Jurnal(models.Model):
    username = models.CharField()
    foto = models.ImageField(upload_to='post/')
    deskripsi = models.TextField()
    tanggal = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.username.username