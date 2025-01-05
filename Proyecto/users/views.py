from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from users.forms import UserRegisterForm  
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required
from Neoprenos.models import UserProfile



def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido {username}")
                return render(request,"Neoprenos/inicio.html")  
            else:
                messages.error(request, "USUARIO O CONTRASEÑA INCORRECTA")
        
        
        messages.error(request, "Por favor corrige los errores en el formulario.")

    else:
        form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu cuenta ha sido creada, puedes iniciar sesión.')
            return redirect('Login')  
        else:
            
            messages.error(request, 'Por favor corrige los errores en el formulario.')

    else:
        form = UserRegisterForm()

    return render(request, 'users/registro.html', {'form': form})
  


@login_required
def update_user(request):
    user = request.user

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()  # Guarda el usuario
            # Actualiza el perfil del usuario según el emoticono seleccionado
            profile = user.userprofile  # Obtiene el UserProfile
            profile.avatar = form.cleaned_data['avatar']
            profile.save()  # Guarda el perfil de usuario
            messages.success(request, 'Tu perfil ha sido actualizado.')
            return redirect('portfolio')  # Redirigir a la vista del perfil
    else:
        form = UserUpdateForm(instance=user)  # Muestra el formulario con los datos actuales

    return render(request, 'users/update_user.html', {'form': form}) 

