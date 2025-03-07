from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, ListView
# from .forms import RegistrationForm, LoginForm


#Vamos a mostrar en la home las ultimas publicaciones
class HomeView(TemplateView):
    template_name = "general/home.html"

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

