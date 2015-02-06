# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Guest, Event

class EventAdmin(admin.ModelAdmin):
    list_display = ['name']
    fieldsets = [
        (None, {'fields': ['name', 'description', 'enabled', 'register_date']}),
    ]


class GuestAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'code', 'quantity_assigned', 'quantity_confirmed',
                    'confirmed', 'confirmation_date', 'event_id']
    fieldsets = [
        (None, {'fields': ['event_id', 'name', 'last_name', 'code', 'quantity_assigned', 'quantity_confirmed',
                           'confirmed', 'confirmation_date', 'register_date', 'enabled']}),
    ]

admin.site.register(Guest, GuestAdmin)
admin.site.register(Event, EventAdmin)
