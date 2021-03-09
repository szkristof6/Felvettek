from django.db import models
import uuid
import datetime
from datetime import datetime


class Lista(models.Model):
    id = models.CharField(
        primary_key=True, default=uuid.uuid4().hex, editable=False, unique=True, max_length=32)
    om_azonosito = models.CharField(max_length=11)
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
        with open('felvettek.tsv', 'r') as f:
            for t in f.readlines():
                tan = t.split('\t')
                if tan[0] and tan[1] and tan[2] and tan[3] and len(str(tan[0])) == 11 and str(tan[0])[0] == "7":
                    Lista.objects.create(
                        om_azonosito=str(tan[0]), nev=str(tan[1]), tagozat=str(tan[2]), dontes=str(tan[3]), date=datetime.now())

    def kereses(json):
        try:
            query = Lista.objects.filter(om_azonosito=json['om_azonosito'])
            if not list(query):
                return {"response": 'nem talált om_azonosito'}
            else:
                return {"response": True, "lista": list(query)}
        except ValueError:
            return {"response": ValueError}


# Create your models here.
