from django.db import models


class Jugador(models.Model):
  nombre = models.CharField(max_length=100)
  equipo = models.ForeignKey('equipos.Equipo', on_delete=models.CASCADE, related_name='lista_jugadores')
  posicion = models.CharField(max_length=50)
  edad = models.PositiveIntegerField()
  pais = models.CharField(max_length=50)

  # 📊 Estadísticas individuales del jugador
  goles = models.IntegerField(default=0)
  asistencias = models.PositiveSmallIntegerField(default=0)
  goles_asistencias = models.PositiveSmallIntegerField(default=0)
  tarjetas_amarillas = models.PositiveSmallIntegerField(default=0)
  tarjetas_rojas = models.PositiveSmallIntegerField(default=0)
  partidos_jugados = models.PositiveSmallIntegerField(default=0)
  minutos_jugados = models.PositiveIntegerField(default=0)


  class Meta:
    verbose_name = "Jugadore"
