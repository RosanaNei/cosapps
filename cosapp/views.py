from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse


# Create your views here.

def index(request):
    saludos = ['Hola', 'Hello', 'Olá', "Buenas"]
    idioma_saludo = {'en': 'Hello', 'es': 'Hola', 'br': 'Olá'}
    return render(request, 'cosapp/index.html', {'hoy': datetime.now, "saludos": saludos, "idioma_saludos": idioma_saludo})

def segundo(request):
    return render(request, 'cosapp/segundo.html')


