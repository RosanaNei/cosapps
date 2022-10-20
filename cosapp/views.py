from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse



# Create your views here.

def index(request):
    saludos = ['Hola', 'Hello', 'Olá', "Buenas"]
    idioma_saludo = {'en': 'Hello', 'es': 'Hola', 'br': 'Olá'}
    return render(request, 'cosapp/index.html', {'hoy': datetime.now,'greeting': 2, 'firstname': 'Emil', "saludos": saludos, "idioma_saludos": idioma_saludo})

def segundo(request):
    idiomas = ['English', 'Español', 'Portugues', 'Alemán']
    lista_atletas= ['juan',  'pepe', 'coso']
    return render(request, 'cosapp/segundo.html', {"lenguajes": idiomas, 'heading': 'Hello &lt;i&gt;my&lt;/i&gt; World!', 'atletas': lista_atletas})

def carta(request):
    return render(request, 'cosapp/carta.html')
