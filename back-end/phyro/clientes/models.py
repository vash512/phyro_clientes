from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver

from actions import Normalizador


class Cliente(models.Model):
    usuario = models.ForeignKey(User, unique=True, blank=True, null=True)
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='asets/items/u', blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    preferencias = models.ManyToManyField("Preferencia", blank=True, null=True)
    otraPref = models.CharField(verbose_name="Otras Preferencias", max_length=255, blank=True, null=True, 
                                help_text="Escriva otras preferencias separadas por comas")
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
    borrador = models.BooleanField(verbose_name="Marca la casilla si solo es un borrador", default=True)
    cliente = models.ForeignKey(User, blank=True, null=True)
    titulo = models.CharField(max_length=255)
    eslogan = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(help_text="Descripcion Detallada, Sera el inicio de su documentacion, recomendamos dedicarle tiempo", blank=True, null=True)
    mantra_interno = models.CharField(max_length=255, blank=True, null=True)
    mantra_externo = models.CharField(max_length=255, blank=True, null=True)
    imagen_corporativa = models.FileField(upload_to='items/imagen', blank=True, null=True)
    logo = models.ImageField(upload_to='items/logos', blank=True, null=True)
    requerimientos = models.ManyToManyField("Requerimiento", blank=True, null=True)
    otrRec = models.CharField(verbose_name="Otros Requerimientos", max_length=255, blank=True, null=True, 
                                help_text="Escriva otros requerimientos separados por comas")
    inicioD = models.DateField(verbose_name="Fecha Inicial Disponible", blank=True, null=True)
    finalP = models.DateField(verbose_name="Fecha Final Deseada", blank=True, null=True)
    presupuesto = models.CharField(max_length=50, verbose_name="Presupuesto Aproximado", blank=True, null=True)
    def __unicode__(self):
        return self.titulo

class UrlProyecto(models.Model):
    proyecto = models.ForeignKey('Proyecto')
    url = models.CharField(max_length=225)
    def __unicode__(self):
        return self.url

def update_UrlProyecto(sender, instance, **kwargs):
    if instance.cliente:
        proyecto = None
        urlNormal = Normalizador(instance.titulo)
        try:
            proyecto =UrlProyecto.objects.get(proyecto=instance)
        except:
            pass
        if proyecto:
            proyecto.url = urlNormal
            proyecto.save()
        else:
            aux=urlNormal
            count=2
            while (UrlProyecto.objects.filter(proyecto__cliente=instance.cliente, url=aux).exists()):
                aux="%s%s"%(urlNormal,count)
                count = count + 1
            urlNormal=aux
            proyecto = UrlProyecto()
            proyecto.proyecto = instance
            proyecto.url = urlNormal
            proyecto.save()


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

'''class PresupuestoPendiente(models.Model):
    proyecto = models.ForeignKey(Proyecto)
    registro = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "PresupuestoPendiente"
        verbose_name_plural = "PresupuestosPendientes"

    def __unicode__(self):
        pass
    '''

post_save.connect(update_UrlProyecto, sender=Proyecto, dispatch_uid="update_url_proyectos")