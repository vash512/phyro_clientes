from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns=patterns('perfiles.views',
    url(r'^$','index_perfil'),
    url(r'^edit/$','editar_view'),
    url(r'^proyectos/$','proyectos_view'),
    url(r'^proyectos/nuevo/$','proyecto_nuevo'),
    url(r'^(?P<proyecto>[\w\-]+)/$','proyecto_view'),
    url(r'^(?P<proyecto>[\w\-]+)/edit$','proyecto_editar'),
    #url(r'^tag/(?P<tag>[\w\-]+)/$','tag_aviso'),
    #url(r'^(?P<perfil>[\w\-]+)/$','perfil_view'),
)
