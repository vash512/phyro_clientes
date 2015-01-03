from django.contrib import admin
from clientes.models import Cliente, Proyecto, Etapa, Requerimiento, Tarea, Preferencia, RequerimientoUsuario

admin.site.register(Cliente)
admin.site.register(Proyecto)
admin.site.register(Etapa)
admin.site.register(Requerimiento)
admin.site.register(Tarea)
admin.site.register(Preferencia)
admin.site.register(RequerimientoUsuario)