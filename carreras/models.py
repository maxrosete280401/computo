from django.db import models

# Create your models here.
class Carreras(models.Model):
    nombre = models.CharField(max_length=80)
    status = models.SmallIntegerField()
        
    def __str__(self):
        return self.nombre    
'''
from carreras.models import Carreras
c = Carreras(nombre="ING SISTEMAS",status=1)
c.save()
c = Carreras(nombre="ING TICS",status=1)
c.save()
c = Carreras(nombre="ING INDUSTRIAL",status=1)
c.save()
'''