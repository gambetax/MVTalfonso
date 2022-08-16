import datetime

import django.db
from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.template import loader

from AppMVTalfonso.models import Familia,Integrantes

# Create your views here.

def inicio(request):
    return HttpResponse('Vista Inicio')

#metodo para ingresar una familia a DB
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


#metodo para consultar una familia a DB
def consultar_familia(request,apellido):

    data = Familia.objects.filter(apellido=apellido)

    contexto = {
        'familia': data,
    }

    return render(request,'consultarFamilia.html',contexto)

#metodo para consultar todas las familias
def familias(request):

    data = Familia.objects.all().values()
    contexto = {
        'familias' : data,
    }

    return render(request,'familias.html',contexto)

#metodo para ingresar un integrante de familia
def integrante(request,nombre,apellido,edad):
    inte = Integrantes(nombre=nombre,apellido=apellido,edad=edad)
    inte.save()
    contexto = {
        'nombre': inte.nombre,
        'apellido': inte.apellido,
        'edad': inte.edad,
    }

    return render(request,'integrante.html',contexto)

##metodo para consultar todos los integrantes en DB
def integrantes(request):
    data = Integrantes.objects.all().values()
    contexto = {
        'integrantes' : data,
    }
    return render(request,'integrantes.html',contexto)

#metodo para consultar integrantes de una determinada familia
def integrantes_por_familia(request,apellido):
    data = Integrantes.objects.filter(apellido=apellido)

    contexto = {
        'integrantes' : data
    }

    return render(request,'integrantes_por_familia.html',contexto)