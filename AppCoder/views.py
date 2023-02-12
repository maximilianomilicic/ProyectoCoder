from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.
def curso(self):
    curso = Curso(nombre="Desarrollo web", comision=1982)
    curso.save()
    documentosDeTexto = f'-----> Curso: {curso.nombre} comision: {curso.comision}'
    return HttpResponse(documentosDeTexto)

# aqui agregamos algo
