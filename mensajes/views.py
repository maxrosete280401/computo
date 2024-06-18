from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import format_html
from mensajes.models import Mensajes

# Create your views here.
def msg_bienvenida(request):
    return HttpResponse("<h1>Estás en mensajes</h1>")

def msg_insertados(request):
    mensajes = Mensajes.objects.order_by('id')

    # Formatear los mensajes con el nombre completo de la persona en negritas y el nombre de la carrera en azul
    formatted_messages = []
    for mensaje in mensajes:
        nombre = mensaje.persona.nombre
        ap_pat = mensaje.persona.ap_pat
        ap_mat = mensaje.persona.ap_mat
        nombre_carrera = mensaje.persona.carrera.nombre
        formatted_message = format_html("{} - <strong>{} {} {} </strong> - <span style='color: blue'>{}</span>", mensaje.txt_mensaje, nombre, ap_pat, ap_mat, nombre_carrera)
        formatted_messages.append(formatted_message)

    # Unir los mensajes formateados en una cadena
    messages_html = "<br>".join(formatted_messages)

    # Devolver la respuesta HTTP con los mensajes formateados
    return HttpResponse(messages_html)
