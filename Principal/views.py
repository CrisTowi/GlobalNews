from django.shortcuts import render
from django.http import HttpResponseRedirect

#Listas
def lista_reportes(request):
	ctx = {}
	return render(request, 'reportes.html', ctx)

def lista_usuarios(request):
	ctx = {}
	return render(request, 'usuarios_admin.html', ctx)

def lista_mensajes(request):
	ctx = {}
	return render(request, 'lista_mensajes.html', ctx)

def lista_seguidos(request):
	ctx = {'nombre_vista': 'Lista de Seguidores'}
	return render(request, 'lista_seguidos.html', ctx)

def lista_seguidores(request):
	ctx = {'nombre_vista': 'Lista de Seguidores'}
	return render(request, 'lista_seguidores.html', ctx)

def lista_publicaciones(request):
	ctx = {'nombre_vista': 'Lista de Publicaciones'}
	return render(request, 'lista_publicaciones.html', ctx)

def lista_publicaciones_seccion(request):
	ctx = {'nombre_vista': 'Lista de Publicaciones en Seccion'}
	return render(request, 'lista_publicaciones_seccion.html', ctx)	

#Muestran info
def index(request):
	ctx = {}
	return render(request, 'index.html', ctx)

def perfil(request):
	ctx = {}
	return render(request, 'perfil.html', ctx)

def publicacion(request):
	ctx = {}
	return render(request, 'publicacion.html', ctx)


#Formularios
def nuevo_post(request):
	ctx = {}
	return render(request, 'nuevo_post.html', ctx)

def nuevo_usuario(request):
	ctx = {}
	return render(request, 'nuevo_usuario.html', ctx)

def editar_post(request):
	ctx = {}
	return render(request, 'editar_post.html', ctx)

#Sesiones
def login(request):
	ctx = {}
	return render(request, 'login.html', ctx)

def logout(request):

	return HttpResponseRedirect('/login/')
