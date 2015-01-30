# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def hotels(request):
    return HttpResponse("Hoteles")

def giftstable(request):
    return HttpResponse("Mesa de regalos")

def confirm(request):
    return HttpResponse("Confirma tu reservacion")

def photos(request):
    return HttpResponse("Comparte tus fotos con nosotros")

# Create your views here.
