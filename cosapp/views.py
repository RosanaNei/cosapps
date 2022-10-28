from cmath import rect
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from cosapp.forms import ContactoForm
from django.contrib import messages


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

def contacto(request):
    if request.method == 'POST':
        # Esta es la instacia que lleva los datos cargados
        contacto_form = ContactoForm(request.POST)
        #Valida y procesa los datos
    else:
        #Acá el formulario vacio con los datos de contacto
        contacto_form = ContactoForm
    return render(request, 'cosapp/contacto.html', {'contacto_form': contacto_form})
