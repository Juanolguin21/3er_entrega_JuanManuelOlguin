from django import forms
from .models import neoprenos

class BuscarProductoForm(forms.Form):
    query = forms.CharField(
        label="Buscar producto",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Escribe el nombre del producto...',
            'class': 'form-control'
        })
    )
    

    
 # Asegúrate de importar tu modelo

class AltaProductoForm(forms.ModelForm):
    class Meta:
        model = neoprenos  # Sustituye con el nombre correcto de tu modelo
        fields = ['marca', 'modelo', 'serie', 'tipo']  # Enumera los campos que deseas incluir

        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modelo'}),
            'serie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Serie'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo'}),
        }
        
class ModificacionProductoForm(forms.ModelForm):
    class Meta:
        model = neoprenos  # Asegúrate de usar el modelo correcto
        fields = ['marca', 'modelo', 'serie', 'tipo']  # Enumera los campos que deseas incluir

        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modelo'}),
            'serie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Serie'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo'}),
        }
        
