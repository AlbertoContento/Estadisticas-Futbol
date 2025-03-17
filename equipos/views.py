from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Equipo
from django.http import HttpResponse
from .importar_equipos import importar_estadisticas
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


class EquipoListView(LoginRequiredMixin, ListView):
    model = Equipo  # Modelo
    template_name = 'equipo_list.html'  # Nombre Plantilla
    context_object_name = 'equipos'  # Nombre variable en el template
    def get_queryset(self):
        return Equipo.objects.all().order_by('-estadisticas__puntos')

class EquipoDetailView(LoginRequiredMixin, DetailView):
    model = Equipo  # Modelo
    template_name = 'equipo_detail.html'  # Nombre Plantilla
    context_object_name = 'equipo'  # Nombre variable en el template

# Ejecutar la importación de equipos
def importar_equipos_view(request):
    # Aquí se ejecuta el script para importar los equipos
    try:
        importar_estadisticas()  # Asegúrate de que tu función importar_estadisticas() esté definida
        return HttpResponse("Equipos importados correctamente.")
    except Exception as e:
        return HttpResponse(f"Error al importar los equipos: {e}")
