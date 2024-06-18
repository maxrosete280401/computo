from django.db import models
from carreras.models import  Carreras

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=80)
    ap_pat = models.CharField(max_length=80)
    ap_mat = models.CharField(max_length=80)
    usu = models.CharField(max_length=80)
    passw = models.CharField(max_length=80)
    fecha_nac = models.DateField()
    carrera = models.ForeignKey(Carreras,on_delete=models.PROTECT)
    status = models.SmallIntegerField()
    
def __str__(self):
    return self.usu
    
'''
from persona.models import Persona
from carreras.models import Carreras

c = Carreras.objects.get(id=1)

persona1 = Persona(nombre="Juan", ap_pat="Lopez", ap_mat="Perez", usu="juan1", passw="pass1", fecha_nac="1990-01-01", carrera=c, status=1)

persona2 = Persona(nombre="Jose", ap_pat="Camarena", ap_mat="Ramirez", usu="jose1", passw="pass2", fecha_nac="1990-01-01", carrera=c, status=1)

c = Carreras.objects.get(id=2)

persona3 = Persona(
    nombre="Laura",
    ap_pat="García",
    ap_mat="Hernández",
    usu="laura1",
    passw="pass5",
    fecha_nac="1992-05-15",
    carrera=c,
    status=1
)

persona4 = Persona(
    nombre="Carlos",
    ap_pat="Martínez",
    ap_mat="Sánchez",
    usu="carlos1",
    passw="pass6",
    fecha_nac="1988-12-03",
    carrera=c,
    status=1
)

c = Carreras.objects.get(id=3)

persona7 = Persona(
    nombre="Mariana",
    ap_pat="Fernández",
    ap_mat="López",
    usu="mariana1",
    passw="pass7",
    fecha_nac="1995-09-20",
    carrera=c,
    status=1
)

persona8 = Persona(
    nombre="Daniel",
    ap_pat="Hernández",
    ap_mat="González",
    usu="daniel1",
    passw="pass8",
    fecha_nac="1987-07-10",
    carrera=c,
    status=1
)
'''