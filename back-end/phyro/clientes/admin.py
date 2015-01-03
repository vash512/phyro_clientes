from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from clientes.models import Cliente, Proyecto, Etapa, Requerimiento, Tarea, Preferencia, RequerimientoUsuario

class ProyectoAdmin(SummernoteModelAdmin):
    model = Proyecto

admin.site.register(Cliente)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Etapa)
admin.site.register(Requerimiento)
admin.site.register(Tarea)
admin.site.register(Preferencia)
admin.site.register(RequerimientoUsuario)