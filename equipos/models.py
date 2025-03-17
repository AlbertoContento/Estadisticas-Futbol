from django.db import models
from ligas.models import Liga

<<<<<<< HEAD
# Create your models here.
=======
#Modelo Equipo
>>>>>>> recuperacion
class Equipo(models.Model):
  nombre = models.CharField(max_length=50, unique=True)
  liga = models.ForeignKey(Liga, on_delete=models.CASCADE, related_name='equipos')#si se borra una liga se borran los equipos
  logo = models.ImageField(upload_to='logos_equipos/', blank=True, null=True)
<<<<<<< HEAD

  # 📊 Estadísticas generales del equipo
  partidos_jugados = models.PositiveIntegerField(default=0)
  partidos_ganados = models.PositiveIntegerField(default=0)
  partidos_empatados = models.PositiveIntegerField(default=0)
  partidos_perdidos = models.PositiveIntegerField(default=0)
  goles_favor = models.PositiveIntegerField(default=0)
  goles_contra = models.PositiveIntegerField(default=0)
=======
  
  def __str__(self):
    return self.nombre
  

  # 📊 Estadísticas generales del equipo
class EstadisticasEquipo(models.Model):
  equipo = models.OneToOneField(Equipo, on_delete=models.CASCADE, related_name='estadisticas')
  partidos_jugados = models.PositiveIntegerField(default=0)
  partidos_ganados = models.IntegerField(default=0)
  partidos_empatados = models.PositiveIntegerField(default=0)
  partidos_perdidos = models.PositiveIntegerField(default=0)
  goles_a_favor = models.PositiveIntegerField(default=0)
  goles_en_contra = models.PositiveIntegerField(default=0)
>>>>>>> recuperacion
  diferencia_goles = models.IntegerField(default=0)
  puntos = models.PositiveIntegerField(default=0)
  asistencias = models.PositiveBigIntegerField(default=0)
  penaltis_marcados = models.PositiveBigIntegerField(default=0)
  tarjetas_amarillas = models.PositiveBigIntegerField(default=0)
  tarjetas_rojas= models.PositiveBigIntegerField(default=0)
  media_posesion = models.FloatField(default=50.0)  # Porcentaje medio de posesión (ej. 55.3)
<<<<<<< HEAD
  partidos_jugados = models.PositiveBigIntegerField(default=0)
  ultimos_5_partidos = models.CharField(max_length=10, default='')

  def __str__(self):
    return self.nombre
=======
  ultimos_5_partidos = models.CharField(max_length=20, default='', blank=True, null=True)
  maximo_goleador = models.CharField(max_length=255, default='')


  def __str__(self):
    return f"Estadísticas de {self.equipo.nombre}"
  
  #Creamos esta propiedad para porder acceder como si fuera un atributo obj.ultimos_5_partidos_list
  @property
  def ultimos_5_partidos_list(self):
    """
    Devuelve una lista con los resultados de los últimos 5 partidos,
    separando la cadena por espacios.
    """
    return self.ultimos_5_partidos.split() if self.ultimos_5_partidos else []
>>>>>>> recuperacion
