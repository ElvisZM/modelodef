from django.contrib import admin
from .models import Usuario, Tarea, Proyecto, Etiqueta, Asignacion_Tarea, Comentario
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Tarea)
admin.site.register(Proyecto)
admin.site.register(Etiqueta)
admin.site.register(Asignacion_Tarea)
admin.site.register(Comentario)
