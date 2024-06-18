from django.contrib import admin

# Register your models here.


from .models import Carreras, Persona, Mensajes
# Register your models here.

admin.site.register(Carreras)
admin.site.register(Persona)
admin.site.register(Mensajes)
