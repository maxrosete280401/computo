from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hola(request):
    return HttpResponse("""
    <h1>Sergio Maximiliano Rosete Partida</h1>
    <a href = "/mensaje/"><h2>Mensajes</h2></a>
    """)
