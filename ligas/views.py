from django.views.generic import ListView, DetailView
from .models import Liga
from django.contrib.auth.mixins import LoginRequiredMixin


class LigaListView(LoginRequiredMixin, ListView):
  model = Liga #Modelo
  template_name = 'ligas/ligas_list.html' # Nombre Plantilla
  context_object_name = 'ligas' # nombre variable en el template

class LigaDetailView(LoginRequiredMixin, DetailView):
  model = Liga #Modelo
  template_name = 'ligas/liga_detail.html' # Nombre Plantilla
  context_object_name = 'liga' # nombre variable en el template