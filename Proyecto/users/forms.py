from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from Neoprenos.models import UserProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(error_messages={'required': 'Este campo es obligatorio.'})
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, error_messages={'required': 'Este campo es obligatorio.'})
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput, error_messages={'required': 'Este campo es obligatorio.'})
    first_name = forms.CharField(label='Nombre', max_length=30, required=True, error_messages={'required': 'Este campo es obligatorio.'})
    last_name = forms.CharField(label='Apellido', max_length=30, required=True, error_messages={'required': 'Este campo es obligatorio.'})

    class Meta:
        model= User
        fields = ["username","email","password1","password2","first_name","last_name"]
        help_text = {k: "" for k in fields }
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Ya existe un usuario con este correo electrónico.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden.")
        return password2