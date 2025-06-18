from django.forms import ModelForm
from .models import Estudiante, Pais


class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'cedula']

class PaisForm(ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre', 'capital', 'numero_provincia', 'numero_habitantes']