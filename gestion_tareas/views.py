from django.shortcuts import render

from .models import Usuario, Tarea, Proyecto, Etiqueta, Asignacion_Tarea, Comentario
from datetime import datetime, date

# Create your views here.
def index(request):
    return render(request, 'principal.html')

def proyecto_list(request):
    proyectos = Proyecto.objects.select_related("creador_proyecto").prefetch_related("proyectos_asignados")
    #Por profesor
    #proyectos = (Proyecto.objects.select_related("creador_proyecto").prefetch_related("proyectos_asignados, Prefetch)
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
    
def comentario_texto_anyo(request, texto_comentario, anyo_comentario):
    year = anyo_comentario
    if 1000 <= year <= 9999:
        fecha_inicio = date(year, 1, 1)
        fecha_fin = date(year, 12, 31)
        
    comentarios = Comentario.objects.select_related("autor", "tarea")
    comentarios = comentarios.filter(fecha_comentario__range=(fecha_inicio, fecha_fin), contenido__startswith=texto_comentario)
    return render(request, "comentario/comentario_list.html",{"comentarios_mostrar":comentarios})
    
def etiqueta_proyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(pk=proyecto_id)
    etiquetas = Etiqueta.objects.filter(etiquetas_asociadas__proyecto=proyecto)
    return render(request, 'etiqueta/etiqueta_list.html', {'etiquetas_mostrar':etiquetas})
    
def usuarios_sin_proyecto(request):
    usuarios = Usuario.objects.filter(proyectos_asignados__isnull=True)
    return render(request, 'usuario/usuario_list.html', {'usuarios_mostrar':usuarios})

def mi_error_400(request, exception=None):
    return render(request, 'errores/400.html',None,None,400)

def mi_error_403(request, exception=None):
    return render(request, 'errores/403.html',None,None,403)

def mi_error_404(request, exception=None):
    return render(request, 'errores/404.html',None,None,404)

def mi_error_500(request, exception=None):
    return render(request, 'errores/500.html',None,None,500)
