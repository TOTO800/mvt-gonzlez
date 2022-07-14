from pydoc import doc
from django.http import HttpResponse
from django.template import Context, Template, loader
from AppMvt.models import Padre, Madre, Hermano

def saludo(request):
    return HttpResponse ('Hola, bienvenido a mi primer mvt')

def plantilla (self):
    plantilla= loader.get_template('template1.html')
    doc= plantilla.render()
    
    return HttpResponse(doc)

def padre(self):
    padre= Padre(nombre='Viktor',apellido= 'Gonzalez',profesion= 'Vj,constructor')
    padre.save()
    texto= f'Datos del padre: {padre.nombre} {padre.apellido} {padre.profesion}'
    return HttpResponse (texto)

def madre(self):
    madre= Madre(nombre='Amalia',apellido= 'Lopez',profesion= 'Docente')
    madre.save()
    texto= f'Datos de la madre: {madre.nombre} {madre.apellido} {madre.profesion}'
    return HttpResponse (texto)

def hermano(self):
    hermano= Hermano(nombre='Manuel',apellido= 'Gonzalez',profesion= 'Programador')
    hermano.save()
    texto= f'Datos del padre: {hermano.nombre} {hermano.apellido} {hermano.profesion}'
    return HttpResponse (texto)


