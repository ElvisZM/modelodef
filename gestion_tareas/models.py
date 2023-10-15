from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    correo_electronico = models.CharField(max_length=200, unique=True)
    contraseña = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(default=timezone.now)
    
    
class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    OPCIONES_ESTADO = [
        ("PENDIENTE","PENDIENTE"),
        ("PROGRESO","PROGRESO"),
        ("COMPLETADA","COMPLETADA"),
    ]
    estado = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="PENDIENTE")
    completada = models.BooleanField()
    fecha_creacion = models.DateField()
    hora_vencimiento = models.TimeField()
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="creador")
    usuarios_asignados = models.ManyToManyField(Usuario, through='Asignacion_Tarea', related_name="usuarios_asignados")
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    proyectos_asignados = models.ManyToManyField(Usuario, related_name="proyectos_asignados")
    creador_proyecto = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="creador_proyecto")
    tarea = models.ForeignKey(Tarea, on_delete = models.CASCADE)
    
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    etiquetas_asociadas = models.ManyToManyField(Tarea)

class Asignacion_Tarea(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    observaciones = models.TextField()
    fecha_asignacion = models.DateTimeField(default=timezone.now)
    
    
class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(default=timezone.now)
    autor = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    tarea = models.OneToOneField(Tarea, on_delete=models.CASCADE)
