from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from core.views import HomeView
from ligas.views import LigaListView, LigaDetailView
from equipos.views import EquipoDetailView
from jugadores.views import JugadorDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    # path('', ContactView.as_view(), name='contacto'),
    # path('', LegalView.as_view(), name='legal'),
    # path('', RegisterView.as_view(), name='registrar'),
    # path('', LoginView.as_view(), name='login'),
    # path('', LogoutView.as_view(), name='logout'),
    path('ligas/', LigaListView.as_view(), name='liga_list'), #rutas app ligas
    path('ligas/<int:pk>/', LigaDetailView.as_view(), name='liga_detail'), #rutas app ligas
    path('equipos/', EquipoDetailView.as_view(), name='equipo_detail'),#rutos app equipos
    path('jugadores/', JugadorDetailView.as_view(), name='jugador_detail'),#rutas app jugadores
    ]


# Agregar manejo de archivos estáticos y media en desarrollo
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)