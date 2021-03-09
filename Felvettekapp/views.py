from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from ratelimit.decorators import ratelimit

from .models import Lista


@ratelimit(key='ip', rate='5/m')
def index(request, *args, **kwargs):
    if request.method == "POST":
        array = json.load(request)

        if not array["om_azonosito"]:
            data = {
                "massage": "Add meg az OM-Azonosítót!"
            }
        else:
            if len(str(array["om_azonosito"])) != 11 and str(array["om_azonosito"])[0] != "7":
                data = {
                    "massage": "Nem megfelelő az OM-Azonosító formátuma!"
                }
            elif not getattr(request, 'limited', False):
                response = Lista.kereses(array)
                if response["response"] == True:
                    lista = []
                    for elem in response["lista"]:
                        array = {
                            "om_azonosito": elem.om_azonosito,
                            "nev": elem.nev,
                            "tagozat": elem.tagozat,
                            "dontes": elem.dontes
                        }
                        lista.append(array)
                    data = {
                        "massage": "OK",
                        "lista": lista
                    }
                elif response["response"] == "nem talált om_azonosito":
                    data = {
                        "massage": "Nem található ilyen OM-Azonosító!"
                    }
                else:
                    data = {
                        "massage": response["response"]
                    }
            else:
                data = {
                    "massage": "Túl sok kérelem érkezett! Várj egy kicsit!"
                }

        return JsonResponse(data)
    return render(request, "index.html", {})

# Create your views here.
