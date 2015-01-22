from django.forms import ModelForm, CheckboxSelectMultiple
from clientes.models import Cliente, Proyecto

class PerfilEdicionForm(ModelForm):
    class Meta:
        model = Cliente
        widgets = {'preferencias': CheckboxSelectMultiple}
        exclude = ["usuario"]

class PerfilRegistroForm(ModelForm):
    class Meta:
        model = Cliente
        widgets = {'preferencias': CheckboxSelectMultiple}
        fields = ["correo", "nombre", "preferencias", "descripcion"]

class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        exclude = ["cliente"]
        widgets = {'requerimientos': CheckboxSelectMultiple}

class ProyectoEdicionForm(ModelForm):
    class Meta:
        model = Proyecto
        exclude = ["cliente", "titulo"]
        widgets = {'requerimientos': CheckboxSelectMultiple}