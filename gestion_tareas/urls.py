from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    
    path('proyecto/listar', views.proyecto_list, name='proyecto_list'),
    
    path('proyecto/<int:proyecto_id>/tareas', views.proyecto_tareas_list, name='tarea_list'),
    
    path('tarea/<int:tarea_id>/usuarios', views.usuario_asignado_tarea_list, name='usuario_list'),
    
    path('tareas/<str:texto_tarea>',views.tareas_texto_concreto, name='tarea_list'),
    
    path('proyectos/completados-entre-fechas/<str:fecha_inicio>/<str:fecha_fin>', views.proyectos_completados_entre_fechas, name='proyectos_completados_entre_fechas'),
    
    path('proyecto/<int:proyecto_id>/ultimo-usuario-comentario',views.ultimo_usuario_comentario_tarea_proyecto, name='ultimo_usuario_comentario_tarea_proyecto'),
    
    
    
    path('etiqueta', views.etiqueta_list, name='etiqueta_list'),
    
    path('asignaciontarea', views.asignacion_tarea_list, name='asignacion_tarea_list'),
    
    path('comentario', views.comentario_list, name='comentario_list'),
]
