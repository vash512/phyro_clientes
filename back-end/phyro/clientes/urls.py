from django.conf.urls import patterns, url, include

urlpatterns=patterns('clientes.views',
    url(r'^$','index'),
    #url(r'^tag/','sin_permisos'),
    #url(r'^tag/','errorLogin'),


    #url(r'^tag/(?P<tag>[\w\-]+)/$','tag_aviso'),
    #url(r'^(?P<aviso>[\w\-]+)/$','aviso'),
)