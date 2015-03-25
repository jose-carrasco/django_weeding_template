# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from myEvent import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^hoteles', views.hotels, name='hotels'),
    url(r'^mesa_de_regalos', views.giftstable, name='giftstable'),
    url(r'^confirmacion', views.confirm, name='confirm'),
    url(r'^comparte_tus_fotos', views.photos, name='photos'),
    url(r'^register', views.register, name='register'),
)