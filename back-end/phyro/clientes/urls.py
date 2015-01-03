from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

urlpatterns=patterns('home.views',
    #HOME
    #estaticos
    url(r'^lo-que-hacemos/$', 'loqueHacemos'),
    url(r'^lo-que-hacemos/ux-ui-design/$', 'uxDesign'),
    url(r'^lo-que-hacemos/ecommerce/$', 'eCommerce'),
    url(r'^lo-que-hacemos/websites/$', 'webSites'),
    url(r'^lo-que-hacemos/marketing-online/$', 'marketingOnline'),
    url(r'^lo-que-hacemos/aplicaciones-web/$', 'appWeb'),
    #secciones
    url(r'^nuestro-trabajo/$', 'portafolio'),
    url(r'^contacto/$', 'contacto'),
    url(r'^about-us/$', 'aboutUS'),
    url(r'^expo-guadalajara/$', 'landing'),
)