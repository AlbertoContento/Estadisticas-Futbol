from django.shortcuts import render
from django.views.generic import DetailView
from .models import Equipo


class EquipoDetailView(DetailView):
  model = Equipo #Modelo
  template_name = 'equipo_detail.html' # Nombre Plantilla
  context_object_name = 'equipo' # nombre variable en el template