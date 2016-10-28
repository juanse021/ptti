
from .models import *
#from django.contrib.auth.models import get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.core.urlresolvers import reverse


from .form import *

def index(request):
	return render(request, "index.html")

@login_required(login_url='/ingresar')
def administrador(request):
	return render(request, "administrador.html")

def perfiladmin(request):
    #return render(request, "vistaadministrador.html")
	#usuarios = Administrador.objects.all()
	if request.user.tipo_usuario != 'A':		
		return HttpResponseRedirect('/')
	else:
		return render(request,'vistaadministrador.html',)

@login_required(login_url='/ingresar')
def listar(request):
    usuarios = Administrador.objects.all()
    return render(request, "listar_a.html", {'usuarios':usuarios})

def ingresar(request):
    if not request.user.is_anonymous():
        if request.user.is_superuser:
            return HttpResponseRedirect('/privado')
        if request.user.tipo_usuario == 'A':
            return HttpResponseRedirect('/administrador')
        if request.user.tipo_usuario == 'S':
            return render(request, "vistasicologo.html")
        if request.user.tipo_usuario == 'E':
            return render(request, "vistaestudiante.html")
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST or None)
        if formulario.is_valid:
            clave = request.POST['password']
            email = request.POST['username']
            usuario = Usuario.objects.filter(email=email)
            if len(usuario) == 1:
                usuario = Usuario.objects.filter(email=email)
                acceso = authenticate(username=usuario[0].username, password=clave)
            else:
            	acceso = authenticate(username=email, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    if request.user.is_superuser:
                        return HttpResponseRedirect('/privado')
                    if request.user.tipo_usuario == 'A':
                        return HttpResponseRedirect('/administrador')
                    if request.user.tipo_usuario == 'S':
                        return render(request, "vistasicologo.html")
                    if request.user.tipo_usuario == 'E':
                        return render(request, "vistaestudiante.html")
                else:
                    return render(request,'noactivo.html')
            else:
                return render(request,'nousuario.html',{'formulario':formulario})
    else:
        formulario = AuthenticationForm()
    return render(request,'ingresar.html',{'formulario':formulario})

@login_required(login_url='/ingresar')
def privado(request):
    #usuario = request.user
    if request.user.is_superuser:
         return render(request,'privado.html')
    elif request.user.tipo_usuario == 'A':
        return HttpResponseRedirect('/administrador')
    elif request.user.tipo_usuario == 'S':
        return render(request, "vistasicologo.html")
    elif request.user.tipo_usuario == 'E':
        return render(request, "vistaestudiante.html")

@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def administrador(request):
	usuarios = Administrador.objects.all()
	return render(request,'administrador.html',{'usuarios':usuarios})

@login_required(login_url='/login/')
def visualizar_estudiante(request):
    usuarios = Estudiante.objects.all()
    return render(request,'visualizar_estudiante.html',{'usuarios':usuarios})

@login_required(login_url='/login/')
def visualizar_sicologo(request):
    usuarios = Sicologo.objects.all()
    return render(request,'visualizar_sicologo.html',{'usuarios':usuarios})

@login_required(login_url='/login')
def visualizar_institucion(request):
    institucion = Institucion.objects.all()
    return render(request, 'visualizar_institucion.html', {'institucion':institucion})

@login_required(login_url='/login/')
def crear_administrador(request):
    if request.method=='POST':
        formulario = FormularioAdministrador(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/administrador')
    else:
        formulario = FormularioAdministrador()
    return render(request, 'crear_administrador.html', {'formulario':formulario})

@login_required(login_url='/login/')
def editar_administrador(request, user_id):
    user = get_object_or_404(Usuario, pk=user_id)
    if request.method=='POST':
        formulario = EditarAdministrador(request.POST, instance=user)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/administrador')
    else:
        formulario = EditarAdministrador(instance=user)
    return render(request, 'editar_administrador.html', {'formulario':formulario})

@login_required(login_url='/login/')
def crear_estudiante(request):
    if request.method == 'POST':
        formulario = FormularioEstudiante(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/visualizarestudiante')
    else:
        formulario = FormularioEstudiante()
    return render(request, 'crear_estudiante.html', {'formulario':formulario})

@login_required(login_url='/login/')
def editar_estudiante(request, user_id):
    user = get_object_or_404(Usuario, pk=user_id)
    if request.method =="POST":
        formulario = EditarEstudiante(request.POST, instance = user)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/visualizarestudiante')
        else:
            formulario = EditarEstudiante(instance=user)
    return render(request, 'editar_estudiante.html', {'formulario':formulario})

@login_required(login_url='/login')
def crear_sicologo(request):
    if request.method == 'POST':
        formulario = FormularioSicologo(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/visualizarsicologo')
    else:
        formulario = FormularioSicologo()
    return render(request, 'crear_sicologo.html', {'formulario': formulario})

#def editar_sicologo

@login_required(login_url='/login')
def crear_institucion(request):
    if request.method == 'POST':
        formulario = InstitucionFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/administrador')
    else:
        formulario = InstitucionFormulario()
    return render(request, 'crear_institucion.html', {'formulario':formulario})

def reset_password(request):
    return password_reset(request, template_name='password_reset_form.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt',
        post_reset_redirect=reverse('ptti:index'))

def reset_password_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='password_reset_confirm.html',uidb64=uidb64, token=token, post_reset_redirect=reverse('ptti:index'))
