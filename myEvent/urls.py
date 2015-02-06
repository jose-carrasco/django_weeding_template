# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings

from myEvent import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^hoteles', views.hotels, name='hotels'),
    url(r'^mesa_de_regalos', views.giftstable, name='giftstable'),
    url(r'^confirmacion', views.confirm, name='confirm'),
    url(r'^comparte_tus_fotos', views.photos, name='photos'),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )