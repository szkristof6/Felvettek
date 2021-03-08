from django.db import models
import uuid
from uuid import UUID
import datetime
from datetime import datetime

class Lista(models.Model):
    id = models.CharField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True, max_length=32)
    om_azonosito = models.IntegerField()
    nev = models.CharField(max_length=100)
    tagozat = models.CharField(max_length=2)
    dontes = models.CharField(max_length=5)
    date = models.DateField()
    
    class Meta:
        verbose_name = 'Elem'
        verbose_name_plural = 'Lista'
        ordering = ['-date']

    def __str__(self):
        return f"{self.om_azonosito} {self.nev}"

    def beolvas():
        print("beolvas")

    def kereses(json):
        try:
            query = Lista.objects.filter(om_azonosito=json['om_azonosito'])
            if not list(query):
                return 'nem talált om_azonosito'
            else:
                return True
        except ValueError:
            return ValueError



# Create your models here.
