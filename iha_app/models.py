from django.db import models
from django.contrib.auth.models import User

class Iha(models.Model):
    marka = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    agirlik = models.FloatField()
    kategori = models.CharField(max_length=255)

    def __str__(self):
        return self.marka
    
class Kiralama(models.Model):
    iha = models.ForeignKey(Iha, on_delete=models.CASCADE)
    tarih = models.DateField()
    saat_araligi = models.CharField(max_length=50)
    kiralayan_uye = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.iha.marka