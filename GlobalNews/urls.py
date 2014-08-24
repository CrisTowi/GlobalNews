from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'Principal.views.index', name='index'),

    url(r'login/$', 'Principal.views.login', name='login'),
    url(r'logout/$', 'Principal.views.logout', name='logout'),

    url(r'perfil/$', 'Principal.views.perfil', name='perfil'),
    url(r'publicacion/$', 'Principal.views.publicacion', name='publicacion'),

    url(r'lista/post/$', 'Principal.views.lista_publicaciones', name='lista_publicaciones'),
    url(r'lista/post/seccion/$', 'Principal.views.lista_publicaciones_seccion', name='lista_publicaciones_seccion'),
    url(r'lista/reportes/$', 'Principal.views.lista_reportes', name='lista_reportes'),
    url(r'lista/usuarios/$', 'Principal.views.lista_usuarios', name='lista_usuarios'),
    url(r'lista/mensajes/$', 'Principal.views.lista_mensajes', name='lista_mensajes'),
    url(r'lista/seguidos/$', 'Principal.views.lista_seguidos', name='lista_seguidos'),
    url(r'lista/seguidores/$', 'Principal.views.lista_seguidores', name='lista_seguidores'),


    url(r'nuevo/post/$', 'Principal.views.nuevo_post', name='nuevo_post'),
    url(r'nuevo/usuario/$', 'Principal.views.nuevo_usuario', name='nuevo_usuario'),

    url(r'editar/post/$', 'Principal.views.editar_post', name='editar_post'),
    url(r'editar/usuario/$', 'Principal.views.editar_perfil', name='editar_perfil'),

)
