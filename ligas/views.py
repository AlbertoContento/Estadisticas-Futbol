from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Liga
<<<<<<< HEAD


class LigaListView(ListView):
=======
from django.contrib.auth.mixins import LoginRequiredMixin


class LigaListView(LoginRequiredMixin, ListView):
>>>>>>> recuperacion
  model = Liga #Modelo
  template_name = 'ligas/ligas_list.html' # Nombre Plantilla
  context_object_name = 'ligas' # nombre variable en el template

<<<<<<< HEAD
class LigaDetailView(DetailView):
=======
class LigaDetailView(LoginRequiredMixin, DetailView):
>>>>>>> recuperacion
  model = Liga #Modelo
  template_name = 'ligas/liga_detail.html' # Nombre Plantilla
  context_object_name = 'liga' # nombre variable en el template