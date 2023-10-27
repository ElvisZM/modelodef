from django.shortcuts import render
from .models import Usuario, Tarea, Proyecto, Etiqueta, Asignacion_Tarea, Comentario

# Create your views here.
def index(request):
    return render(request, 'index.html')

def proyecto_list(request):
    proyectos = Proyecto.objects.select_related("creador_proyecto").prefetch_related("proyectos_asignados")
    proyectos = proyectos.all()
    return render(request, 'proyecto/proyecto_list.html', {'proyectos_mostrar':proyectos})

def tarea_list(request):
    tareas = Tarea.objects.select_related("creador", "proyecto").prefetch_related("usuarios_asignados")
    return render(request, 'tarea/tarea_list.html', {'tareas_mostrar':tareas})

def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'gestion_tareas/usuario_list.html', {'usuarios_mostrar':usuarios})

def etiqueta_list(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'gestion_tareas/etiqueta_list.html', {'etiquetas_mostrar':etiquetas})

def asignacion_tarea_list(request):
    asignaciones = Asignacion_Tarea.objects.all()
    return render(request, 'gestion_tareas/asignacion_tarea_list.html', {'asignaciones_mostrar':asignaciones})

def comentario_list(request):
    comentarios = Comentario.objects.all()
    return render(request, 'gestion_tareas/comentario_list.html', {'comentarios_mostrar':comentarios})
