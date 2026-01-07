from django import forms 
from .models import Articulo
from .models import FraseInspiradora

class FormularioCrearArticulo(forms.ModelForm):

	class Meta:
		model = Articulo
		fields = ('titulo','categoria','contenido','imagen')

class FormularioModificarArticulo(forms.ModelForm):

	class Meta:
		model = Articulo
		fields = ('titulo','categoria','contenido','imagen')


class FraseForm(forms.ModelForm):
    class Meta:
        model = FraseInspiradora
        fields = ['texto', 'autor']