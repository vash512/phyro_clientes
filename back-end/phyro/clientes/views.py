# -*- coding: utf-8 -*-
from actions import Archivador
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect as redirect301
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout



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
                        ctx={'usuario':usuario}
                        return render_to_response('home/index.html', ctx,
                          context_instance=RequestContext(request))
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
        #Pantalla del Perfil
        ctx={'usuario':usuario}
        return render_to_response('home/index.html', ctx,
                          context_instance=RequestContext(request))