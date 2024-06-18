from django.db import models
from persona.models import Persona
# Create your models here.

class Mensajes(models.Model):
    txt_mensaje = models.CharField(max_length=80)
    persona = models.ForeignKey(Persona,on_delete=models.PROTECT)
    status = models.SmallIntegerField()
    
def __str__(self):
    return self.txt_mensaje

'''
from mensajes.models import Mensajes
from persona.models import Persona

p1 = Persona.objects.get(id=3)
p2 = Persona.objects.get(id=4)
p3 = Persona.objects.get(id=5)
p4 = Persona.objects.get(id=6)
p5 = Persona.objects.get(id=7)
p6 = Persona.objects.get(id=8)

msg1 = Mensajes(txt_mensaje = "MSG Numero 1", persona = p1, status = 1)
msg2 = Mensajes(txt_mensaje = "MSG Numero 2", persona = p2, status = 1)
msg3 = Mensajes(txt_mensaje = "MSG Numero 3", persona = p3, status = 1)
msg4 = Mensajes(txt_mensaje = "MSG Numero 4", persona = p4, status = 1)
msg5 = Mensajes(txt_mensaje = "MSG Numero 5", persona = p5, status = 1)
msg6 = Mensajes(txt_mensaje = "MSG Numero 6", persona = p6, status = 1)

msg1.save()
msg2.save()
msg3.save()
msg4.save()
msg5.save()
msg6.save()
'''
