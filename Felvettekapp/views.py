from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from ratelimit.decorators import ratelimit

from .models import Lista


def index(request, *args, **kwargs):
    return render(request, "index.html", {})


@ratelimit(key='ip', rate='5/m')
def kereses(request, *args, **kwargs):
    array = json.load(request)

    if not getattr(request, 'limited', False):
        response = Lista.kereses(array)
        if response == True:
            data = {
                "massage": "OK"
            }
        elif response == "nem talált om_azonosito":
            data = {
                "massage": "Nem található ilyen OM-Azonosító!"
            }
        else:
            data = {
                "massage": response
            }
    else:
        data = {
            "massage": "Ratelimit"
        }

    return JsonResponse(data)

def lekerdezes(request, om_azonosito, *args, **kwargs):
    if(Lista.protection(om_azonosito)):
        got_data = Lista.get_data(om_azonosito)
        lista = []

        for elem in got_data:
            array = {
                "tagozat": elem.tagozat,
                "dontes": elem.dontes
            }
            lista.append(array)

        return render(request, "lekerdezes.html", {"om_azonosito": got_data[0].om_azonosito, "nev": got_data[0].nev, "adatok": lista})
    else:
        return redirect("/")

# Create your views here.
