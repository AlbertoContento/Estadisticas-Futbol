from django.db import models


class Jugador(models.Model):
  nombre = models.CharField(max_length=100)
  equipo = models.ForeignKey('equipos.Equipo', on_delete=models.CASCADE, related_name='lista_jugadores')
  posicion = models.CharField(max_length=50)
  edad = models.PositiveIntegerField()
  pais = models.CharField(max_length=50)

  # 📊 Estadísticas individuales del jugador
<<<<<<< HEAD
  goles = models.PositiveSmallIntegerField(default=0)
=======
  goles = models.IntegerField(default=0)
>>>>>>> recuperacion
  asistencias = models.PositiveSmallIntegerField(default=0)
  goles_asistencias = models.PositiveSmallIntegerField(default=0)
  tarjetas_amarillas = models.PositiveSmallIntegerField(default=0)
  tarjetas_rojas = models.PositiveSmallIntegerField(default=0)
  partidos_jugados = models.PositiveSmallIntegerField(default=0)
  minutos_jugados = models.PositiveIntegerField(default=0)

<<<<<<< HEAD
  def __str__(self):
    return self.nombre
=======
  class Meta:
    verbose_name = "Jugadore"
>>>>>>> recuperacion
