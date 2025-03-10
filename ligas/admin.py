from django.contrib import admin
from .models import Liga


@admin.register(Liga)
class LigaAdmin(admin.ModelAdmin):
  list_display = ("nombre", "abreviatura", "logo", "id_fbref")
