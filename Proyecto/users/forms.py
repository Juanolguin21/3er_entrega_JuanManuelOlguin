from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from Neoprenos.models import UserProfile


class UserUpdateForm(forms.ModelForm):
    avatar = forms.ChoiceField(
        choices=[
            ('😊', 'Sonriente'),
            ('😎', 'Con gafas de sol'),
            ('🥳', 'Fiesta'),
            ('😢', 'Triste'),
            ('😡', 'Enojado')
        ],
        label='Elija un emoticono como avatar'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar']  

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, error_messages={'required': 'Este campo es obligatorio.'})
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput, error_messages={'required': 'Este campo es obligatorio.'})
    avatar = forms.ChoiceField(choices=[
        ('😊', 'Sonriente'),
        ('😎', 'Con gafas de sol'),
        ('🥳', 'Fiesta'),
        ('😢', 'Triste'),
        ('😡', 'Enojado')
    ], label='Elija un emoticono como avatar')
       
        
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
    
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        if commit:
            user.save()
            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.avatar = self.cleaned_data['avatar']  
            profile.save()  
        return user