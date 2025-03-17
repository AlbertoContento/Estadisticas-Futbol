from django.contrib import admin
from jugadores.models import Jugador


@admin.register(Jugador)
class JugadoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'equipo', 'posicion', 'edad', 'pais', 'goles', 'asistencias', 'goles_asistencias', 'tarjetas_amarillas', 'tarjetas_rojas', 'partidos_jugados', 'minutos_jugados')
    search_fields = ('nombre', 'equipo', 'posicion', 'pais')
    list_filter = ('equipo', 'posicion', 'pais')
