from django.shortcuts import render
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

# Create your views here.
