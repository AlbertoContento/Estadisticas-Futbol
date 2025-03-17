from django.contrib import admin
from .models import Liga


@admin.register(Liga)
class LigaAdmin(admin.ModelAdmin):
<<<<<<< HEAD
  list_display = ("nombre", "abreviatura", "logo", "id_fbref")
=======
  list_display = ("nombre", "abreviatura", "logo", "id_fbref", "lista_equipos")
  search_fields = ("nombre", "abreviatura", "logo")
  list_filter = ("nombre", "abreviatura")
  
  def lista_equipos(self, obj):
    return ", ".join([equipo.nombre for equipo in obj.equipos.all()])  # Lista de nombres

  lista_equipos.short_description = "Equipos en la Liga"  # Cabecera de la columna
>>>>>>> recuperacion
