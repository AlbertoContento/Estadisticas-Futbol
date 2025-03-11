from django.shortcuts import render
from django.views.generic import DetailView
from .models import Equipo
from django.http import HttpResponse
from .importar_equipos import importar_estadisticas

class EquipoDetailView(DetailView):
  model = Equipo #Modelo
  template_name = 'equipo_detail.html' # Nombre Plantilla
  context_object_name = 'equipo' # nombre variable en el template

#Ejecutar la importación de equipos
def importar_equipos_view(request):
    # Aquí se ejecuta el script para importar los equipos
    try:
        importar_estadisticas()  # Asegúrate de que tu función importar_estadisticas() esté definida
        return HttpResponse("Equipos importados correctamente.")
    except Exception as e:
        return HttpResponse(f"Error al importar los equipos: {e}")
