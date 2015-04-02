# -*- coding: utf-8 -*-
from django.core import serializers
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
    if request.method == 'POST':
        try:
            name = request.POST['name']
            phone = request.POST['phone']
            email = request.POST['email']
            message = request.POST['message']
            attend = request.POST['attend']
            attend_message = u"Sí" if attend else u"No"
            data = {
                    "name": name,
                    "phone": phone,
                    "email": email,
                    "message": message,
                    "attend": attend_message
            }
            from mandrill_mail import send_mail
            send_mail(data)
            response['status'] = 1
            response['message'] = u"¡Muchas gracias por enviar tu respuesta!"
        except Exception, e:
            print e
            response['status'] = 0
            response['message'] = u"Lo sentimos, no se pudo completar el envío, por favor intenta nuevamente."
        print response
        import json

        return HttpResponse(json.dumps(response))
    else:
        return HttpResponse("No data")

# Create your views here.
