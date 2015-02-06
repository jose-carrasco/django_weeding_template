# -*- coding: utf-8 -*-
from django.db import models


class Guest(models.Model):
    class Meta:
        verbose_name = "Invitado"
        verbose_name_plural = "Invitados"

    event_id = models.ForeignKey('Event', verbose_name='Evento')
    name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=100)
    email = models.CharField('Correo electrónico', max_length=100)
    code = models.CharField('Código', max_length=5)
    quantity_assigned = models.IntegerField('Boletos asignados', default=1)
    quantity_confirmed = models.IntegerField('Boletos confirmados', default=0)
    confirmed = models.BooleanField('¿Ha confirmado?', default=False)
    confirmation_date = models.DateTimeField('Fecha de confirmación', null=True, blank=True)
    enabled = models.BooleanField('Habilitado', default=True)
    active = models.BooleanField(default=True)
    register_date = models.DateTimeField('Fecha de registro')

    def __unicode__(self):
        return self.name + " " + self.last_name

class Event(models.Model):
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    name = models.CharField('Nombre', max_length=200)
    description = models.CharField('Descripción', max_length=500)
    enabled = models.BooleanField('Habilitado', default=True)
    active = models.BooleanField(default=True)
    register_date = models.DateTimeField('Fecha de registro')

    def __unicode__(self):
        return self.name