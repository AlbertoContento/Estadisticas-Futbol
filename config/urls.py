from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from core.views import HomeView, LoginView, logout_view
from ligas.views import LigaListView, LigaDetailView
from equipos.views import EquipoListView, EquipoDetailView, importar_equipos_view
from jugadores.views import importar_jugadores_view
from core.views import ContactView, LegalView
from core.views import RegisterView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('contacto/', ContactView.as_view(), name='contacto'),
    path('legal/', LegalView.as_view(), name='legal'),
    path('registrar/', RegisterView.as_view(), name='registrar'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('ligas/', LigaListView.as_view(), name='liga_list'), #rutas app ligas
    path('ligas/<int:pk>/', LigaDetailView.as_view(), name='liga_detail'), #rutas app ligas
    path('importar-equipos/', importar_equipos_view, name='importar_equipos'),#Ruta para importar equipos
    path('importar-jugadores/', importar_jugadores_view, name='importar_jugadores'),#Ruta para importar jugadores
    path('equipos/<int:pk>/', EquipoDetailView.as_view(), name='equipo_detail'),#rutas app equipos/jugadores
    path('lista-equipos/', EquipoListView.as_view(), name='equipo_list'),#rutas app jugadores
    ]


# Agregar manejo de archivos estáticos y media en desarrollo
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
