from django.conf.urls import patterns, include, url
from rest_framework import routers
from django.contrib import admin
from Principal.views import UsuarioViewSet, NotaViewSet, ReporteUsuarioViewSet,ReporteNotaViewSet,SeccionViewSet
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'notas', NotaViewSet)
router.register(r'reportesusuario', ReporteUsuarioViewSet)
router.register(r'reportesnota', ReporteNotaViewSet)
router.register(r'secciones', SeccionViewSet)


urlpatterns = patterns('',

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'Principal.views.index', name='index'),

    url(r'login/$', 'Principal.views.login', name='login'),
    url(r'logout/$', 'Principal.views.logout', name='logout'),

    url(r'perfil/$', 'Principal.views.perfil', name='perfil'),
    url(r'publicacion/$', 'Principal.views.publicacion', name='publicacion'),

    url(r'lista/post/$', 'Principal.views.lista_publicaciones', name='lista_publicaciones'),
    url(r'lista/post/seccion/$', 'Principal.views.lista_publicaciones_seccion', name='lista_publicaciones_seccion'),
    url(r'lista/reportes/post$', 'Principal.views.lista_reportes', name='lista_reportes'),
    url(r'lista/reportes/usuario$', 'Principal.views.lista_reportes_usuario', name='lista_reportes_usuario'),
    url(r'lista/usuarios/$', 'Principal.views.lista_usuarios', name='lista_usuarios'),
    url(r'lista/mensajes/$', 'Principal.views.lista_mensajes', name='lista_mensajes'),
    url(r'lista/seguidos/$', 'Principal.views.lista_seguidos', name='lista_seguidos'),
    url(r'lista/seguidores/$', 'Principal.views.lista_seguidores', name='lista_seguidores'),


    url(r'nuevo/post/$', 'Principal.views.nuevo_post', name='nuevo_post'),
    url(r'nuevo/usuario/$', 'Principal.views.nuevo_usuario', name='nuevo_usuario'),

    url(r'editar/post/$', 'Principal.views.editar_post', name='editar_post'),
    url(r'editar/usuario/$', 'Principal.views.editar_perfil', name='editar_perfil'),

)
