from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    usuario = models.ForeignKey(User, unique=True, blank=True, null=True)
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='asets/items/u', blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    preferencias = models.ManyToManyField("Preferencia", blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    correo = models.EmailField(unique=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    def __unicode__(self):
        return "%s"%self.usuario

class Telefono(models.Model):
    cliente = models.ForeignKey(Cliente)
    telefono = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=245, blank=True, null=True) 
    def __unicode__(self):
        return "%s %s"%(self.cliente, self.telefono)

class Proyecto(models.Model):
    cliente = models.ForeignKey(User, blank=True, null=True)
    titulo = models.CharField(max_length=50)
    eslogan = models.CharField(max_length=255)
    descripcion = models.TextField(help_text="Descripcion Detallada, Sera el inicio de su documentacion, recomendamos dedicarle tiempo")
    mantra_interno = models.CharField(max_length=255, blank=True, null=True)
    mantra_externo = models.CharField(max_length=255, blank=True, null=True)
    imagen_corporativa = models.FileField(upload_to='items/imagen', blank=True, null=True)
    logo = models.ImageField(upload_to='items/logos', blank=True, null=True)
    requerimientos = models.ManyToManyField("Requerimiento")
    inicioD = models.DateField(verbose_name="Fecha Inicial Disponible")
    finalP = models.DateField(verbose_name="Fecha Final Deseada")
    presupuesto = models.CharField(max_length=50, verbose_name="Presupuesto Aproximado")
    def __unicode__(self):
        return self.titulo

class Etapa(models.Model):
    proyecto = models.ForeignKey("Proyecto")
    titulo = models.CharField(max_length=245)
    descripcion = models.TextField()
    nivel = models.CharField(max_length=50)
    def __unicode__(self):
        return "%s - %s %s"%(self.proyecto, self.titulo,
                            self.nivel)

class RequerimientoUsuario(models.Model):
    etapa = models.ForeignKey(Etapa)
    requerimiento = models.TextField()
    realizado = models.BooleanField()

class Tarea(models.Model):
    etapa = models.ForeignKey("Etapa")
    realizada = models.BooleanField()
    nivel = models.CharField(max_length=50)
    prioridad = models.CharField(max_length=50)
    descripcion = models.TextField()
    fechaTermino = models.DateField()
    resultados = models.TextField()

    def __unicode__(self):
        return "Tareas de %s"%self.etapa.proyecto
    

class Preferencia(models.Model):
    preferencia = models.CharField(max_length=50)
    def __unicode__(self):
        return self.preferencia

class Requerimiento(models.Model):
    requerimiento = models.CharField(max_length=50)
    def __unicode__(self):
        return self.requerimiento