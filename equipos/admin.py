from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from equipos.models import Equipo
from equipos.models import EstadisticasEquipo

@admin.register(Equipo)
class EquiposAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'liga', 'logo')

@admin.register(EstadisticasEquipo)
class EestadisticasEquipoAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'partidos_jugados', 'partidos_ganados', 'partidos_empatados', 'partidos_perdidos', 'goles_a_favor', 'goles_en_contra', 'diferencia_goles', 'puntos', 'asistencias', 'penaltis_marcados', 'tarjetas_amarillas', 'tarjetas_rojas', 'media_posesion', 'ultimos_5_partidos', 'maximo_goleador')
>>>>>>> recuperacion
