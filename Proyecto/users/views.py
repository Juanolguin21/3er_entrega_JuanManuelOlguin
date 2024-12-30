from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from users.forms import UserRegisterForm  


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


# Vista de registro
def register(request):

      msg_register= ""
      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  form.save()
                  return render(request,"Neoprenos/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
            msg_register= "ERROR EN LOS DATOS INGRESADOS"
      
      form = UserRegisterForm()     

      return render(request,"users/registro.html" ,  {"form":form, "msg_register":msg_register})
  

