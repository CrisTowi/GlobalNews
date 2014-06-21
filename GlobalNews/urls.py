from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'Principal.views.index', name='index'),

    url(r'login/$', 'Principal.views.login', name='login'),
    url(r'logout/$', 'Principal.views.logout', name='logout'),

    url(r'perfil/$', 'Principal.views.perfil', name='perfil'),
    url(r'publicacion/$', 'Principal.views.publicacion', name='publicacion'),

    url(r'lista/reportes/$', 'Principal.views.lista_reportes', name='lista_reportes'),
    url(r'lista/usuarios/$', 'Principal.views.lista_usuarios', name='lista_usuarios'),
    url(r'lista/mensajes/$', 'Principal.views.lista_mensajes', name='lista_mensajes'),

    url(r'nuevo/post/$', 'Principal.views.nuevo_post', name='nuevo_post'),
    url(r'nuevo/usuario/$', 'Principal.views.nuevo_usuario', name='nuevo_usuario'),

)
