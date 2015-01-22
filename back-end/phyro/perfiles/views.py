# -*- coding: utf-8 -*-
#http y redireccionamientos
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect as redirect301

#autentificacion
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

#modelos y formularios
from clientes.models import Cliente, Proyecto, UrlProyecto
from clientes.forms import PerfilEdicionForm, ProyectoForm, ProyectoEdicionForm

#otros
from actions import Normalizador

def perfUs(usuario):
    try:
        perfil=Cliente.objects.get(usuario=usuario)
    except :
        perfil=None
    return perfil

def urlProyecto(proyecto):
    try:
        url=UrlProyecto.objects.get(proyecto=proyecto)
    except :
        url=None
    if url:
        return url.url
    else:
        return None

def proyetoUrl(url, usuario):
    try:
        url=UrlProyecto.objects.get(url=url, proyecto__cliente=usuario)
    except :
        url=None
    if url:
        return url
    else:
        return False

@login_required(login_url='/')
def index_perfil(request, perfil):
    usuario=request.user
    if "%s"%usuario.username == "%s"%perfil:
        ctx={'usuario':usuario, 'perfil':perfUs(usuario)}
        return render_to_response('perfil/index.html', ctx,
                          context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')

@login_required(login_url='/')
def editar_view(request, perfil):
    usuario=request.user
    mensaje=None
    if "%s"%usuario.username == "%s"%perfil:
        perfil=perfUs(usuario)
        if perfil:
        #formulario de lientes instanciado por el perfil
            if 'actualizar' in request.POST:
                formPerfil=PerfilEdicionForm(request.POST, request.FILES, instance=perfil)
                if formPerfil.is_valid():
                    perfil=formPerfil.save()
                    mensaje="Datos Actualizados Correctamente"
                    formPerfil=PerfilEdicionForm(instance=perfil)
            else:
                formPerfil=PerfilEdicionForm(instance=perfil)

            ctx={'usuario':usuario, 'perfil':perfil, 'formPerfil':formPerfil, 'mensaje':mensaje}
            return render_to_response('perfil/editarPerfil.html', ctx,
                          context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

@login_required(login_url='/')
def proyectos_view(request, perfil):
    usuario=request.user
    if "%s"%usuario.username == "%s"%perfil:
        perfil=perfUs(usuario)
        proyectos=UrlProyecto.objects.filter(proyecto__cliente=usuario)
        ctx={'usuario':usuario, 'perfil':perfil, 'proyectos':proyectos}
        return render_to_response('perfil/listaProyectos.html', ctx,
                          context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')

@login_required(login_url='/')
def proyecto_nuevo(request, perfil):
    usuario=request.user
    tituloRepetido=False
    titulo=None
    url=False
    if "%s"%usuario.username == "%s"%perfil:
        perfil=perfUs(usuario)
        if perfil:
        #formulario de lientes instanciado por el perfil
            if 'guardar' in request.POST:
                formProyecto=ProyectoForm(request.POST, request.FILES)
                if formProyecto.is_valid():
                    titulo=formProyecto.cleaned_data['titulo']
                    if not Proyecto.objects.filter(cliente=usuario, titulo=titulo).exists():
                        proyecto=formProyecto.save()
                        proyecto.cliente = usuario
                        proyecto.save()
                        url=urlProyecto(proyecto)
                    else:
                        tituloRepetido=True
                        titulo = Normalizador(titulo)
            else:
                formProyecto=ProyectoForm()

            ctx={'usuario':usuario, 'perfil':perfil, 'formProyecto':formProyecto,
                 'tituloRepetido':tituloRepetido, 'titulo':titulo, 'url':url}
            return render_to_response('perfil/proyectoNuevo.html', ctx,
                          context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

@login_required(login_url='/')
def proyecto_view(request, perfil, proyecto):
    usuario=request.user
    if "%s"%usuario.username == "%s"%perfil:
        proyecto = proyetoUrl(proyecto, usuario)
        ctx={'usuario':usuario, 'perfil':perfUs(usuario), 'proyecto':proyecto}
        return render_to_response('perfil/proyecto.html', ctx,
                          context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')

@login_required(login_url='/')
def proyecto_editar(request, perfil, proyecto):
    usuario=request.user
    mensaje=None
    if "%s"%usuario.username == "%s"%perfil:
        proyecto = proyetoUrl(proyecto, usuario)
        proyecto=proyecto.proyecto
        if not proyecto:
            return HttpResponseRedirect('/%s/proyectos/'%usuario.username)
        else:
            if 'actualizar' in request.POST:

                formProyecto=ProyectoEdicionForm(request.POST, request.FILES, instance=proyecto)
                if formProyecto.is_valid():
                    proyecto=formProyecto.save()
                    mensaje='Los Cambios guardados con exito'
                    formProyecto=ProyectoEdicionForm(instance=proyecto)
            else:
                formProyecto=ProyectoEdicionForm(instance=proyecto)
            ctx={'usuario':usuario, 'perfil':perfUs(usuario), 'proyecto':proyecto,
                 'mensaje':mensaje, 'formProyecto':formProyecto}
            return render_to_response('perfil/editarProyecto.html', ctx,
                          context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')