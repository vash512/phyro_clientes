# -*- coding: utf-8 -*-
from actions import Archivador
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect as redirect301



def index_view(request):
    #Archivador('home/index.html', 'index', {})
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def perfil(request):
    return render_to_response('loquehacemos/lo-que-hacemos.html',
                          context_instance=RequestContext(request))