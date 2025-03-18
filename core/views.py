from pyexpat.errors import messages
from urllib import request
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView
from django.contrib.auth.models import User
from core.forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


#Vamos a mostrar en la home las ultimas publicaciones
class HomeView(TemplateView):
    template_name = "general/home.html"

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
        """Método que se ejecuta cuando el formulario es inválido"""
        response = super().form_invalid(form)
        print("Errores del formulario:", form.errors)  # Imprime los errores en la consola
        messages.add_message(self.request, messages.ERROR, "Error al registrar el usuario")
        return response

class LegalView(TemplateView):
    template_name = "general/legal.html"

class ContactView(TemplateView):
    template_name = "general/contact.html"
    logos_laliga = [
        '/media/logos_equipos/la_liga/alaves.png',
        '/media/logos_equipos/la_liga/Barcelona.png',
        '/media/logos_equipos/la_liga/atletico_madrid.png',
        '/media/logos_equipos/la_liga/athletic_club.png',
        '/media/logos_equipos/la_liga/betis.png',
        '/media/logos_equipos/la_liga/celta_vigo.png',
        '/media/logos_equipos/la_liga/espanyol.png',
        '/media/logos_equipos/la_liga/getafe.png',
        '/media/logos_equipos/la_liga/girona.png',
        '/media/logos_equipos/la_liga/las_palmas.png',
        '/media/logos_equipos/la_liga/leganes.png',
        '/media/logos_equipos/la_liga/mallorca.png',
        '/media/logos_equipos/la_liga/osasuna.png',
        '/media/logos_equipos/la_liga/rayo_vallecano.png',
        '/media/logos_equipos/la_liga/real_madrid.png',
        '/media/logos_equipos/la_liga/real_sociedad.png',
        '/media/logos_equipos/la_liga/sevilla.png',
        '/media/logos_equipos/la_liga/valencia.png',
        '/media/logos_equipos/la_liga/valladolid.png',
        '/media/logos_equipos/la_liga/villarreal.png',
    ]
    logos_premier = [
        '/media/logos_equipos/premier_league/arsenal.png',
        '/media/logos_equipos/premier_league/aston_villa.png',
        '/media/logos_equipos/premier_league/bournemouth.png',
        '/media/logos_equipos/premier_league/brentford.png',
        '/media/logos_equipos/premier_league/brighton.png',
        '/media/logos_equipos/premier_league/chelsea.png',
        '/media/logos_equipos/premier_league/crystal_palace.png',
        '/media/logos_equipos/premier_league/everton.png',
        '/media/logos_equipos/premier_league/fulham.png',
        '/media/logos_equipos/premier_league/ipswich_town.png',
        '/media/logos_equipos/premier_league/leicester_city.png',
        '/media/logos_equipos/premier_league/liverpool.png',
        '/media/logos_equipos/premier_league/manchester_city.png',
        '/media/logos_equipos/premier_league/manchester_utd.png',
        '/media/logos_equipos/premier_league/newcastle_utd.png',
        '/media/logos_equipos/premier_league/nottham_forest.png',
        '/media/logos_equipos/premier_league/southampton.png',
        '/media/logos_equipos/premier_league/tottenham.png',
        '/media/logos_equipos/premier_league/west_ham.png',
        '/media/logos_equipos/premier_league/wolves.png',
    ]
    logos_serie_a = [
        '/media/logos_equipos/serie_a/atalanta.png',
        '/media/logos_equipos/serie_a/bologna.png',
        '/media/logos_equipos/serie_a/cagliari.png',
        '/media/logos_equipos/serie_a/como.png',
        '/media/logos_equipos/serie_a/empoli.png',
        '/media/logos_equipos/serie_a/fiorentina.png',
        '/media/logos_equipos/serie_a/genoa.png',
        '/media/logos_equipos/serie_a/hellas_verona.png',
        '/media/logos_equipos/serie_a/inter.png',
        '/media/logos_equipos/serie_a/juventus.png',
        '/media/logos_equipos/serie_a/lazio.png',
        '/media/logos_equipos/serie_a/lecce.png',
        '/media/logos_equipos/serie_a/milan.png',
        '/media/logos_equipos/serie_a/monza.png',
        '/media/logos_equipos/serie_a/napoli.png',
        '/media/logos_equipos/serie_a/parma.png',
        '/media/logos_equipos/serie_a/roma.png',
        '/media/logos_equipos/serie_a/torino.png',
        '/media/logos_equipos/serie_a/udinese.png',
        '/media/logos_equipos/serie_a/venezia.png',
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logos_laliga'] = self.logos_laliga
        context['logos_premier'] = self.logos_premier
        context['logos_serie_a'] = self.logos_serie_a
        return context

#FUNCION PARA CERRAR SESION
@login_required#protege las vistas de usuarios que no esten autenticados
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, "Se ha cerrado sesión correctamente.")
    return HttpResponseRedirect(reverse('home'))
