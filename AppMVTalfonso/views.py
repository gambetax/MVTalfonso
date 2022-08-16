import datetime

import django.db
from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.template import loader

from AppMVTalfonso.models import Familia,Integrantes

# Create your views here.

def inicio(request):
    return HttpResponse('Vista Inicio')

def familia(request, apellido, cantidad_integrantes):
    #now = datetime.now()
    fam = Familia(apellido=apellido,cantidad_integrantes=cantidad_integrantes)
    fam.save()
    plantilla = loader.get_template('familia.html')
    contexto = {
        "apellido" : fam.apellido,
        "cantidad_integrantes" : fam.cantidad_integrantes
    }

    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def consultar_familia(request,apellido):

    data = Familia.objects.filter(apellido=apellido)

    contexto = {
        'familia': data,
    }

    return render(request,'consultarFamilia.html',contexto)

def familias(request):

    data = Familia.objects.all().values()
    contexto = {
        'familias' : data,
    }

    return render(request,'familias.html',contexto)

def integrante(request,nombre,apellido,edad):
    inte = Integrantes(nombre=nombre,apellido=apellido,edad=edad)
    inte.save()
    contexto = {
        'nombre': inte.nombre,
        'apellido': inte.apellido,
        'edad': inte.edad,
    }

    return render(request,'integrante.html',contexto)

def integrantes(request):
    data = Integrantes.objects.all().values()
    contexto = {
        'integrantes' : data,
    }
    return render(request,'integrantes.html',contexto)

