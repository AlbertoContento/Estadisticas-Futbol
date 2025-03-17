<<<<<<< HEAD
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Jugador

class JugadorDetailView(DetailView):
  model = Jugador
  template_name = 'jugador_detail.html'
  context_object_name = 'jugador'
=======
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Jugador
from .importar_jugadores import importar_jugadores
from django.contrib.auth.mixins import LoginRequiredMixin


class JugadorDetailView(LoginRequiredMixin, DetailView):
  model = Jugador
  template_name = 'jugador_detail.html'
  context_object_name = 'jugador'

  # Ejecutar la importación de jugadores
def importar_jugadores_view(request):
    # Aquí se ejecuta el script para importar los equipos
    try:
        importar_jugadores()  # Asegúrate de que tu función importar_estadisticas() esté definida
        return HttpResponse("Jugadores importados correctamente.")
    except Exception as e:
        return HttpResponse(f"Error al importar los jugadores: {e}")
>>>>>>> recuperacion
