from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField

TIPO_DE_DOCUMENTO = (
	("C.C", "Cedula de ciudadania"),
	("T.I", "Tarjeta de identidad"),
)

TIPO_DE_GENERO = (
	("M", "Masculino"),
	("F", "Femenino")
)

class FormularioAdministrador(UserCreationForm):
    TIPO_USUARIO = (
        ("A", "Administrador"),
    )
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    tipo_usuario = forms.ChoiceField(choices = TIPO_USUARIO,  widget=forms.Select(), required=True)
    tipo_genero = forms.ChoiceField(choices = TIPO_DE_GENERO,  widget=forms.Select(), required=True)
    tipo_documento = forms.ChoiceField(choices = TIPO_DE_DOCUMENTO,  widget=forms.Select(), required=True)
    documento = forms.CharField(required=True)
    direccion = forms.CharField(required=True)
    telefono  = forms.CharField(required=True)
    fecha_nacimiento = forms.DateField(widget=forms.SelectDateWidget(years=[y for y in range(1990,2017)]),required=True)

    class Meta:
        model = Administrador
        fields = ('username','email','first_name','last_name','tipo_usuario','tipo_genero','tipo_documento','documento','direccion','telefono','fecha_nacimiento','password1', 'password2')

    def save(self, commit=True):
        user = super(FormularioAdministrador, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class EditarAdministrador(UserChangeForm):
    fecha_nac   = forms.DateField(label='Fecha nacimiento',widget=forms.SelectDateWidget(years=[y for y in range(1990,2017)]),required=True)
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Administrador
        fields = ('username','email','first_name','last_name','tipo_usuario','tipo_genero','tipo_documento','documento','direccion','telefono','fecha_nacimiento','password')

    def save(self, commit=True):
        user = super(EditarAdministrador, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(EditarAdministrador, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['username'].required = False
            self.fields['username'].widget.attrs['disabled'] = 'disabled'

    def clean_username(self):
        instance = getattr(self, 'instance', None)
        if instance:
            try:
                self.changed_data.remove('username')
            except ValueError:
                pass
            return instance.username
        else:
            return self.cleaned_data.get('username', None)

    def clean_password(self):
        instance = getattr(self, 'instance', None)
        if instance:
            try:
                self.changed_data.remove('password')
            except ValueError:
                pass
            return instance.password
        else:
            return self.cleaned_data.get('password', None)

class FormularioEstudiante(UserCreationForm):
    TIPO_USUARIO = (
        ("E", "Estudiante"),
    )
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    tipo_usuario = forms.ChoiceField(choices = TIPO_USUARIO,  widget=forms.Select(), required=True)
    tipo_genero = forms.ChoiceField(choices = TIPO_DE_GENERO,  widget=forms.Select(), required=True)
    tipo_documento = forms.ChoiceField(choices = TIPO_DE_DOCUMENTO,  widget=forms.Select(), required=True)
    documento = forms.CharField(required=True)
    direccion = forms.CharField(required=True)
    telefono  = forms.CharField(required=True)
    fecha_nacimiento = forms.DateField(widget=forms.SelectDateWidget(years=[y for y in range(1990,2017)]),required=True)

    class Meta:
        model = Estudiante
        fields = ('username','email','first_name','last_name','tipo_usuario','tipo_genero','tipo_documento','documento','direccion','telefono','fecha_nacimiento','password1', 'password2')

    def save(self, commit=True):
        user = super(FormularioEstudiante, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class EditarEstudiante(UserChangeForm):
    fecha_nac   = forms.DateField(label='Fecha nacimiento',widget=forms.SelectDateWidget(years=[y for y in range(1990,2017)]),required=True)
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Estudiante
        fields = ('username','email','first_name','last_name','tipo_usuario','tipo_genero','tipo_documento','documento','direccion','telefono','fecha_nacimiento','password')

    def save(self, commit=True):
        user = super(EditarEstudiante, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(EditarEstudiante, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['username'].required = False
            self.fields['username'].widget.attrs['disabled'] = 'disabled'

    def clean_username(self):
        instance = getattr(self, 'instance', None)
        if instance:
            try:
                self.changed_data.remove('username')
            except ValueError:
                pass
            return instance.username
        else:
            return self.cleaned_data.get('username', None)

    def clean_password(self):
        instance = getattr(self, 'instance', None)
        if instance:
            try:
                self.changed_data.remove('password')
            except ValueError:
                pass
            return instance.password
        else:
            return self.cleaned_data.get('password', None)


class FormularioSicologo(UserCreationForm):
    TIPO_USUARIO = (
        ("S", "Sicologo"),
    )
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    tipo_usuario = forms.ChoiceField(choices = TIPO_USUARIO,  widget=forms.Select(), required=True)
    tipo_genero = forms.ChoiceField(choices = TIPO_DE_GENERO,  widget=forms.Select(), required=True)
    tipo_documento = forms.ChoiceField(choices = TIPO_DE_DOCUMENTO,  widget=forms.Select(), required=True)
    documento = forms.CharField(required=True)
    direccion = forms.CharField(required=True)
    telefono  = forms.CharField(required=True)
    fecha_nacimiento = forms.DateField(widget=forms.SelectDateWidget(years=[y for y in range(1990,2017)]),required=True)

    class Meta:
        model = Sicologo
        fields = ('username','email','first_name','last_name','tipo_usuario','tipo_genero','tipo_documento','documento','direccion','telefono','fecha_nacimiento','password1', 'password2')

    def save(self, commit=True):
        user = super(FormularioSicologo, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class InstitucionFormulario(ModelForm):
	class Meta:
		model = Institucion
		fields = ('nit', 'nombre', 'direccion', 'telefono', 'ciudad', 'sitio_web')

class GrupoFormulario(ModelForm):
	class Meta:
		model = Grupo
		fields = ('institucion', 'nombre', 'grado', 'jornada')
