from django.shortcuts import render
from .models import Usuario, Tarea, Proyecto, Etiqueta, Asignacion_Tarea, Comentario

# Create your views here.
def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'gestion_tareas/usuario_list.html', {'usuarios_mostrar':usuarios})
def tarea_list(request):
    tareas = Tarea.objects.all()
    return render(request, 'gestion_tareas/tarea_list.html', {'tareas_mostrar':tareas})
def proyecto_list(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'gestion_tareas/proyecto_list.html', {'proyectos_mostrar':proyectos})
def etiqueta_list(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'gestion_tareas/etiqueta_list.html', {'etiquetas_mostrar':etiquetas})
def asignacion_tarea_list(request):
    asignaciones = Asignacion_Tarea.objects.all()
    return render(request, 'gestion_tareas/asignacion_tarea_list.html', {'asignaciones_mostrar':asignaciones})
def comentario_list(request):
    comentarios = Comentario.objects.all()
    return render(request, 'gestion_tareas/comentario_list.html', {'comentarios_mostrar':comentarios})
