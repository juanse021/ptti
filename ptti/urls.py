from django.conf.urls import url
from ptti.views import *

app_name = 'ptti'
urlpatterns = [
    url(r'^$', ingresar, name="index"),
    url(r'^administrador/$', perfiladmin, name="administrador"),
	url(r'^password-reset/$', reset_password, name='reset_password'),
	url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',reset_password_confirm, name='reset_password_confirm'),
    url(r'^ingresar/$', ingresar, name="ingresar"),
    url(r'^privado/$', privado, name="privado"),
    url(r'^crear_administrador/$', crear_administrador, name="crear_administrador"),
    url(r'^editar_administrador/(?P<user_id>[0-9]+)$', editar_administrador, name="editar_administrador"),
    url(r'^cerrar/$', cerrar, name="cerrar"),
    url(r'^estudiante/$', crear_estudiante, name="crear_estudiante"),
    url(r'^estudiante/editar_estudiante/(?P<user_id>[0-9]+)$', editar_estudiante, name="editar_estudiante"),
    url(r'^listar/$', listar, name="listar"),
    url(r'^visualizarestudiante/$', visualizar_estudiante, name="visualizar_estudiante"),
    url(r'^crear_sicologo/$', crear_sicologo, name="crear_sicologo"),
    url(r'^visualizarsicologo/$', visualizar_sicologo, name="visualizar_estudiante"),
    url(r'^visualizarinstitucion/$', visualizar_institucion, name="visualizar_institucion"),
    url(r'^crear_institucion/$', crear_institucion, name="crear_institucion"),
]
