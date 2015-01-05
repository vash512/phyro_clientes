from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns=patterns('clientes.views',
    url(r'^$','index'),
    url(r'^logout/$','log_out'),
    url(r'^registro/$','registro'),
    #url(r'^tag/','errorLogin'),


    #url(r'^tag/(?P<tag>[\w\-]+)/$','tag_aviso'),
    #url(r'^(?P<aviso>[\w\-]+)/$','aviso'),
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