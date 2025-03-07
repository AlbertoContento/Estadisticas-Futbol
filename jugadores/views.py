from django.shortcuts import render
from django.views.generic import DetailView
from .models import Jugador

class JugadorDetailView(DetailView):
  model = Jugador
  template_name = 'jugador_detail.html'
  context_object_name = 'jugador'