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
from clientes.models import Cliente
from clientes.forms import PerfilRegistroForm

#otros
from actions import Archivador




def index(request):
    usuario=request.user
    if usuario.is_anonymous():
        if request.method=='POST':
            formulario=AuthenticationForm(request.POST)
            #solicitud de login por post
            if formulario.is_valid:
                usuariof=request.POST['username']
                clavef=request.POST['password']
                acceso=authenticate(username=usuariof,password=clavef)
                if acceso is not None:
                    if acceso.is_active:
                        login(request,acceso)
                        #Pantalla del Perfil
                        return HttpResponseRedirect('/%s'%usuariof)
                    else:
                        error="Posiblemente tu usuario este baneado o desactivado, comunicate con el administrador"
                else:
                    error="El usuario no existe, verifique que este bien escrito"
            else:
                error="Datos invalidos en el formulario"
            ctx={'formulario':formulario, 'error':error}
            return render_to_response('home/login.html', ctx,
                          context_instance=RequestContext(request))
        else:
            #Login
            formulario=AuthenticationForm()
            ctx={'formulario':formulario}
            return render_to_response('home/login.html', ctx,
                          context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/%s'%usuario.username)
        #Pantalla del Perfil
'''        try:
            perfil=Cliente.objects.get(usuario=usuario)
        except :
            perfil=None
        ctx={'usuario':usuario, 'perfil':perfil}
        return render_to_response('home/index.html', ctx,
                          context_instance=RequestContext(request))'''

@login_required(login_url='/')
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

def registro(request):
    usuario=request.user
    if not usuario.is_anonymous():
        return HttpResponseRedirect('/')
    else:
        registrado=False
        if request.method=='POST':
            fRegistro=PerfilRegistroForm(request.POST)
            fUsuario=UserCreationForm(request.POST)
            if fUsuario.is_valid() and fRegistro.is_valid():
                usuario=fUsuario.save()
                perfil=fRegistro.save()
                perfil.usuario=usuario
                perfil.save()
                registrado=True

        else:
            fRegistro=PerfilRegistroForm()
            fUsuario=UserCreationForm()
        ctx={"registro":fRegistro, "fUsuario":fUsuario, "registrado":registrado}
        return render_to_response('home/registro.html', ctx,
                          context_instance=RequestContext(request))

def perfil_view(request):
    return render_to_response('home/login.html',
                          context_instance=RequestContext(request))

def proyectos_view(request):
    return render_to_response('home/login.html',
                          context_instance=RequestContext(request))