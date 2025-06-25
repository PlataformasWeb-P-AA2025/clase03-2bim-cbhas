from django.forms import ModelForm
from django import forms
from administrativo.models import Matricula, Estudiante

class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = ['estudiante', 'modulo', 'comentario']



class MatriculaEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MatriculaEditForm, self).__init__(*args, **kwargs)
        self.initial['estudiante'] = self.instance.estudiante
        self.fields["estudiante"].widget = forms.widgets.HiddenInput()
        self.initial['modulo'] = self.instance.modulo
        self.fields["modulo"].widget = forms.widgets.HiddenInput()

    class Meta:
        model = Matricula
        fields = ['estudiante', 'modulo', 'comentario']
        widgets = {
            'comentario': forms.Textarea(attrs={
                'rows': 4,
                'cols': 40,
                'placeholder': 'Escribe aquí tu comentario...'
            }),}


class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'cedula', 'edad', 'tipo_estudiante']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'cedula': forms.TextInput(attrs={'placeholder': 'Cédula'}),
            'edad': forms.NumberInput(attrs={'placeholder': 'Edad'}),
            'tipo_estudiante': forms.Select(),
        }