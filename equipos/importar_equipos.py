import pandas as pd
import os
from django.conf import settings
from equipos.models import Equipo, EstadisticasEquipo
from ligas.models import Liga


# Definir rutas de las carpetas
RUTA_ESTADISTICAS = os.path.join(settings.BASE_DIR, "data/estadisticas")
RUTA_CLASIFICACION = os.path.join(settings.BASE_DIR, "data/clasificacion")

# Diccionario de nombres de archivo y ligas
LIGAS = {
    "laliga.csv": "La Liga",
    "premier.csv": "Premier League",
    "seriea.csv": "Serie A",
}

def limpiar_cadena(valor):
    """Elimina caracteres extraños y espacios innecesarios."""
    if isinstance(valor, str):
        return valor.strip().replace('"', '').replace("...", "").replace(" - ", " -")
    return valor

def procesar_archivo(ruta_csv, liga, tipo_datos):
    """Función para procesar los archivos CSV y actualizar la base de datos."""
    if not os.path.exists(ruta_csv):
        print(f"⚠️ No se encontró {ruta_csv}")
        return

    # Cargar el CSV con Pandas
    df = pd.read_csv(ruta_csv)

    for _, fila in df.iterrows():
        nombre_equipo = limpiar_cadena(fila["Equipo"])
        equipo = Equipo.objects.filter(nombre=nombre_equipo, liga=liga).first()

        if not equipo:
            print(f"⚠️ No se encontró el equipo {nombre_equipo} en {liga.nombre}.")
            continue

        # Crear o actualizar estadísticas o clasificación
        if tipo_datos == "estadisticas":
            EstadisticasEquipo.objects.update_or_create(
                equipo=equipo,
                defaults={
                    "partidos_jugados": fila["PJ"],
                    "partidos_ganados": fila["PG"],
                    "partidos_empatados": fila["PE"],
                    "partidos_perdidos": fila["PP"],
                    "goles_a_favor": fila["GF"],
                    "goles_en_contra": fila["GC"],
                    "diferencia_goles": fila["DG"],
                    "puntos": fila["Pts"],
                    "maximo_goleador": limpiar_cadena(fila.get("Máximo Goleador del Equipo", "")),
                    "ultimos_5_partidos": fila.get("Últimos 5", ""),
                },
            )
            print(f"✅ Estadísticas de {equipo.nombre} actualizadas desde {ruta_csv}.")
        elif tipo_datos == "clasificacion":
            EstadisticasEquipo.objects.update_or_create(
                equipo=equipo,
                defaults={
                    "asistencias": fila.get("Ass", 0),
                    "penaltis_marcados": fila.get("TP", 0),
                    "tarjetas_amarillas": fila.get("TA", 0),
                    "tarjetas_rojas": fila.get("TR", 0),
                    "media_posesion": fila.get("Pos.", 0),
                },
            )
            print(f"✅ Clasificación de {equipo.nombre} actualizada desde {ruta_csv}.")

def importar_estadisticas():
    for archivo, nombre_liga in LIGAS.items():
        # Buscar la liga
        liga = Liga.objects.filter(nombre=nombre_liga).first()
        if not liga:
            print(f"⚠️ No se encontró la liga {nombre_liga} en la base de datos.")
            continue

        # Procesar archivo de estadísticas
        ruta_estadisticas_csv = os.path.join(RUTA_ESTADISTICAS, archivo)
        procesar_archivo(ruta_estadisticas_csv, liga, "estadisticas")

        # Procesar archivo de clasificación
        ruta_clasificacion_csv = os.path.join(RUTA_CLASIFICACION, archivo)
        procesar_archivo(ruta_clasificacion_csv, liga, "clasificacion")

    print("🚀 Importación de estadísticas y clasificación finalizada.")


if __name__ == "__main__":
    importar_estadisticas()
