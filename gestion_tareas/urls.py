from django.urls import path
from . import views

urlpatterns = [
    path('usuario', views.usuario_list, name='usuario_list'),
    path('tarea', views.tarea_list, name='tarea_listl'),
    path('proyecto', views.proyecto_list, name='proyecto_list'),
    path('etiqueta', views.etiqueta_list, name='etiqueta_list'),
    path('asignaciontarea', views.asignacion_tarea_list, name='asignacion_tarea_list'),
    path('comentario', views.comentario_list, name='comentario_list'),
]
