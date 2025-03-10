from django.db import models

# Create your models here.
class Liga(models.Model):
  nombre = models.CharField(max_length=50, unique=True)
  abreviatura = models.CharField(max_length=10, unique=True)
  logo = models.ImageField(upload_to='logos_ligas/', blank=True, null=True)
  id_fbref= models.CharField(max_length=100, blank=True, null=True)  # Esta columna debe existir

  def __str__(self):
    return self.nombre