# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.serializers.json import DjangoJSONEncoder

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

def register(request):
    response = {}
    try:
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        attend = request.POST['attend']
        attend_message = u"Sí" if attend else u"No"
        response['status'] = 1
        response['message'] = "sucess"
    except:
        response['status'] = 1
        response['message'] = u"Lo sentimos, no se pudo completar la confirmación, por favor intenta nuevamente."

    print response
    return json.dumps(response), 200

# Create your views here.
