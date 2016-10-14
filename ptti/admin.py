from django.contrib import admin

from .models import Usuario, Institucion, Grupo, Administrador, Sicologo, Estudiante


admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Sicologo)
admin.site.register(Estudiante)
admin.site.register(Institucion)
admin.site.register(Grupo)
# Register your models here.
