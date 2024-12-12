from django import forms

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