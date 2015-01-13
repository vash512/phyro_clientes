from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns=patterns('perfiles.views',
    url(r'^$','index_perfil'),
    url(r'^proyectos/$','proyectos_view'),
    #url(r'^tag/(?P<tag>[\w\-]+)/$','tag_aviso'),
    #url(r'^(?P<perfil>[\w\-]+)/$','perfil_view'),
)

if settings.DEBUG:
    urlpatterns+=patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root':settings.MEDIA_ROOT,} ),
    )

    urlpatterns+=patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root':settings.STATICFILES_DIRS,} ),
    )