<<<<<<< HEAD
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, ListView
# from .forms import RegistrationForm, LoginForm

=======
from pyexpat.errors import messages
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView
from django.contrib.auth.models import User
from core.forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
>>>>>>> recuperacion

#Vamos a mostrar en la home las ultimas publicaciones
class HomeView(TemplateView):
    template_name = "general/home.html"

<<<<<<< HEAD
# #FORMVIEW: vista para formulario
# class LoginView(FormView):
#     template_name = "general/login.html"
#     form_class = LoginForm

#     def form_valid(self, form):#Fomulario es valido
#         usuario = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=usuario, password=password)#Guardamos usuario y contraseña si el usuario existe en nuestra BD
#         if user is not None:#Si el user no es None
#             login(self.request, user)#Logueamos al usuario
#             messages.add_message(self.request, messages.SUCCESS, f'Bienvenido de nuevo {user.username}')
#             return HttpResponseRedirect(reverse('home'))#una vez logueado le redirigimos a la home
#         else:#si el usuario es None, mandamos mensaje de error
#             messages.add_message(
#                 self.request, messages.ERROR, 'Usuario no válido o contraseña no válida')
#             return super(LoginView, self).form_invalid(form)#Devolvemos que el login es invalido


# #CREATEVIEW: para poder registrar usuarios
# class RegisterView(CreateView):
#     model = User
#     template_name = "general/register.html"
#     success_url = reverse_lazy('login')#Pagina que mostrar despues de registrar
#     form_class = RegistrationForm#le pasamos el formulario

#     def form_valid(self, form):
#         messages.add_message(self.request, messages.SUCCESS, "Usuario creado correctamente.")
#         return super(RegisterView, self).form_valid(form)


# class LegalView(TemplateView):
#     template_name = "general/legal.html"


# class ContactView(TemplateView):
#     template_name = "general/contact.html"

=======
#FORMVIEW: vista para formulario
class LoginView(FormView):
    template_name = "general/login.html"
    form_class = LoginForm

    def form_valid(self, form):#Fomulario es valido
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=usuario, password=password)#Guardamos usuario y contraseña si el usuario existe en nuestra BD
        if user is not None:#Si el user no es None
            login(self.request, user)#Logueamos al usuario
            messages.add_message(self.request, messages.SUCCESS, f'Bienvenido de nuevo {user.username}')
            return HttpResponseRedirect(reverse('home'))#una vez logueado le redirigimos a la home
        else:#si el usuario es None, mandamos mensaje de error
            messages.add_message(
                self.request, messages.ERROR, 'Usuario no válido o contraseña no válida')
            return super(LoginView, self).form_invalid(form)#Devolvemos que el login es invalido

#CREATEVIEW: para poder registrar usuarios
class RegisterView(CreateView):
    model = User  # Modelo de la base de datos que vamos a crear (Usuario)
    template_name = "general/register.html"  # Ruta del template HTML para el formulario
    form_class = RegisterForm  # Especificamos el formulario que usaremos
    success_url = reverse_lazy("home")  # Redirige a "home" tras el registro

    def form_valid(self, form):
        """Método que se ejecuta cuando el formulario es válido"""
        response = super().form_valid(form)  # Llama al método original para guardar el usuario
        messages.add_message(self.request, messages.SUCCESS, "Usuario registrado correctamente")  # Agrega mensaje de éxito
        return response
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        print("Errores del formulario:", form.errors)  # Imprime los errores en la consola
        messages.add_message(self.request, messages.ERROR, "Error al registrar el usuario")
        return response

class LegalView(TemplateView):
    template_name = "general/legal.html"

class ContactView(TemplateView):
    template_name = "general/contact.html"

#FUNCION PARA CERRAR SESION
@login_required#protege las vistas de usuarios que no esten autenticados
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, "Se ha cerrado sesión correctamente.")
    return HttpResponseRedirect(reverse('home'))
>>>>>>> recuperacion
