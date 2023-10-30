from django.shortcuts import render
from .models import Usuario, Tarea, Proyecto, Etiqueta, Asignacion_Tarea, Comentario
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def proyecto_list(request):
    proyectos = Proyecto.objects.select_related("creador_proyecto").prefetch_related("proyectos_asignados")
    proyectos = proyectos.all()
    return render(request, 'proyecto/proyecto_list.html', {'proyectos_mostrar':proyectos})

def proyecto_tareas_list(request, proyecto_id):
    tareas = Tarea.objects.select_related("creador", "proyecto").prefetch_related("usuarios_asignados")
    tareas = tareas.filter(proyecto__id=proyecto_id).order_by("-fecha_creacion")
    return render(request, 'tarea/tarea_list.html', {'tareas_mostrar':tareas})

def usuario_asignado_tarea_list(request, tarea_id):
    asignaciones = Asignacion_Tarea.objects.filter(tarea__id=tarea_id).order_by('fecha_asignacion')
    usuarios_asignados = [asignacion.usuario for asignacion in asignaciones]
    return render(request, 'usuario/usuario_list.html', {'usuarios_mostrar':usuarios_asignados})

def tareas_texto_concreto(request, texto_tarea):
    tareas = Tarea.objects.select_related("creador", "proyecto").prefetch_related("usuarios_asignados")
    tareas = tareas.filter(asignacion_tarea__observaciones__contains=texto_tarea)
    return render(request, 'tarea/tarea_list.html',{"tareas_mostrar":tareas})
    
def proyectos_completados_entre_fechas(request, fecha_inicio, fecha_fin):
    fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
    proyectos = Proyecto.objects.select_related("creador_proyecto").prefetch_related("proyectos_asignados")
    proyectos = proyectos.filter(
        fecha_inicio__gte=fecha_inicio,
        fecha_finalizacion__lte=fecha_fin,
    )
    return render(request, 'proyecto/proyecto_list.html', {'proyectos_mostrar':proyectos})

def ultimo_usuario_comentario_tarea_proyecto(request, proyecto_id):
    ultimo_comentario = Comentario.objects.select_related("autor", "tarea")
    ultimo_comentario = ultimo_comentario.filter(tarea__proyecto=proyecto_id).order_by("-fecha_comentario").first()
    if ultimo_comentario:
        ultimo_usuario_comentario = ultimo_comentario.autor
    else:
        ultimo_usuario_comentario=None
        
    return render(request, "comentario/comentario_list.html",{"ultimo_usuario_comentario":ultimo_usuario_comentario})
    
    
    


def etiqueta_list(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'gestion_tareas/etiqueta_list.html', {'etiquetas_mostrar':etiquetas})

def asignacion_tarea_list(request):
    asignaciones = Asignacion_Tarea.objects.all()
    return render(request, 'gestion_tareas/asignacion_tarea_list.html', {'asignaciones_mostrar':asignaciones})

def comentario_list(request):
    comentarios = Comentario.objects.all()
    return render(request, 'gestion_tareas/comentario_list.html', {'comentarios_mostrar':comentarios})
