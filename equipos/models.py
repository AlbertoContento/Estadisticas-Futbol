from django.db import models
from ligas.models import Liga

# Create your models here.
class Equipo(models.Model):
  nombre = models.CharField(max_length=50, unique=True)
  liga = models.ForeignKey(Liga, on_delete=models.CASCADE, related_name='equipos')#si se borra una liga se borran los equipos
  logo = models.ImageField(upload_to='logos_equipos/', blank=True, null=True)

  # 📊 Estadísticas generales del equipo
  partidos_jugados = models.PositiveIntegerField(default=0)
  partidos_ganados = models.PositiveIntegerField(default=0)
  partidos_empatados = models.PositiveIntegerField(default=0)
  partidos_perdidos = models.PositiveIntegerField(default=0)
  goles_favor = models.PositiveIntegerField(default=0)
  goles_contra = models.PositiveIntegerField(default=0)
  diferencia_goles = models.IntegerField(default=0)
  puntos = models.PositiveIntegerField(default=0)
  asistencias = models.PositiveBigIntegerField(default=0)
  penaltis_marcados = models.PositiveBigIntegerField(default=0)
  tarjetas_amarillas = models.PositiveBigIntegerField(default=0)
  tarjetas_rojas= models.PositiveBigIntegerField(default=0)
  media_posesion = models.FloatField(default=50.0)  # Porcentaje medio de posesión (ej. 55.3)
  partidos_jugados = models.PositiveBigIntegerField(default=0)
  ultimos_5_partidos = models.CharField(max_length=10, default='')

  def __str__(self):
    return self.nombre