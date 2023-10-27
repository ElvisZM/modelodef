from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    
    path('proyecto/listar', views.proyecto_list, name='proyecto_list'),
    
    path('tarea/listar', views.tarea_list, name='tarea_list'),
    
    path('usuario', views.usuario_list, name='usuario_list'),
    
    path('etiqueta', views.etiqueta_list, name='etiqueta_list'),
    
    path('asignaciontarea', views.asignacion_tarea_list, name='asignacion_tarea_list'),
    
    path('comentario', views.comentario_list, name='comentario_list'),
]
