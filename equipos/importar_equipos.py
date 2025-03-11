import os
import pandas as pd
from django.conf import settings
from django.core.files import File
from equipos.models import Equipo, EstadisticasEquipo
from ligas.models import Liga
from unidecode import unidecode  # Importamos la función unidecode


# Definir rutas de las carpetas
RUTA_CLASIFICACION = os.path.join(settings.BASE_DIR, "data/clasificacion")
RUTA_ESTADISTICA = os.path.join(settings.BASE_DIR, "data/estadisticas")

# Diccionario de nombres de archivo y ligas
LIGAS = {
  "La_Liga.csv": "La Liga",
  "Premier_League.csv": "Premier League",
  "Serie_A.csv": "Serie A",
}

def limpiar_cadena(valor):
  """Elimina caracteres extraños y espacios innecesarios."""
  if isinstance(valor, str):
    return valor.strip().replace('"', '').replace("...", "").replace(" - ", " -")
  return valor

def comprobar_dataframe(df):
  """Comprueba si el DataFrame tiene datos."""
  if df.empty:
    print(f"⚠️ El DataFrame está vacío o no tiene datos válidos.")
    return False
  print(f"✔️ DataFrame cargado con {len(df)} filas.")
  return True

def crear_o_buscar_equipo(nombre_equipo, liga):
  """Crea o busca un equipo en la base de datos."""
  nombre_equipo = limpiar_cadena(nombre_equipo)
  equipo, created = Equipo.objects.get_or_create(nombre=nombre_equipo, liga=liga)
  print(f"{'🆕' if created else '🔄'} Equipo {'creado' if created else 'encontrado'}: {equipo.nombre}")
  return equipo

def procesar_archivo(ruta_csv, liga, tipo_datos):
  """Procesa los archivos CSV y actualiza la base de datos."""
  print(f"📄 Procesando archivo: {ruta_csv}...")
  print(f"🆙🆙🆙🆙🆙{tipo_datos}")

  if not os.path.exists(ruta_csv):
    print(f"⚠️ No se encontró {ruta_csv}")
    return

  df = pd.read_csv(ruta_csv)
  if not comprobar_dataframe(df):
    return
  # Iterar sobre las filas del CSV
  for _, fila in df.iterrows(): 
    nombre_equipo = fila["Equipo"]
    equipo = crear_o_buscar_equipo(nombre_equipo, liga)
    print("Columnas del DataFrame:", df.columns.tolist())
    if tipo_datos == "clasificacion":
      print("Actualizando clasificacion")
      ultimos_5 = fila.get("Últimos 5", "").strip()
      if len(ultimos_5) > 14:
        ultimos_5 = ultimos_5[:14]
      EstadisticasEquipo.objects.update_or_create(
        equipo=equipo,
        defaults={
          "partidos_jugados": fila.get("PJ", 0),
          "partidos_ganados": fila.get("PG", 0),
          "partidos_empatados": fila.get("PE", 0),
          "partidos_perdidos": fila.get("PP", 0),
          "goles_a_favor": fila.get("GF", 0),
          "goles_en_contra": fila.get("GC", 0),
          "diferencia_goles": fila.get("DG", 0),
          "puntos": fila.get("Pts", 0),
          "maximo_goleador": limpiar_cadena(fila.get("Máximo Goleador del Equipo", "")),
          "ultimos_5_partidos": ultimos_5,
        },
      )
      print(f"✅ Clasificacion actualizada para {equipo.nombre}")

    if tipo_datos == "estadisticas":
      print("Actualizando estadisticas")
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
      print(f"✅ Estadisticas actualizadas para {equipo.nombre}")

def importar_estadisticas():
  """Importa estadísticas y clasificación para todas las ligas."""
  print("🚀 Iniciando importación de datos...")

  for archivo, nombre_liga in LIGAS.items():
    liga = Liga.objects.filter(nombre=nombre_liga).first()
    if not liga:
      print(f"⚠️ No se encontró la liga {nombre_liga} en la base de datos.")
      continue

    # Procesar archivo de clasificación
    ruta_clasificacion_csv = os.path.join(RUTA_CLASIFICACION, archivo)
    procesar_archivo(ruta_clasificacion_csv, liga, "clasificacion")
    # Procesar archivo de estadisticas
    ruta_estadisticas_csv = os.path.join(RUTA_ESTADISTICA, archivo)
    procesar_archivo(ruta_estadisticas_csv, liga, "estadisticas")

  # Asignar logos a los equipos
  asignar_logos_equipos()
  print("✅ Importación finalizada.")

def asignar_logos_equipos():
  '''Asigna los logos a los equipos desde la carpeta logos_equipos'''
  ruta_base = os.path.join(settings.MEDIA_ROOT, 'logos_equipos')  # Ruta a los logos
  # Iteramos sobre todas las ligas
  for liga in Liga.objects.all():
      print(liga.nombre)
      
      # Convertimos el nombre de la liga a minúsculas y reemplazamos los espacios por guiones bajos
      nombre_liga = liga.nombre.lower().replace(" ", "_")
      print(nombre_liga) 
      
      # Creamos la ruta completa para la carpeta de la liga
      ruta_liga = os.path.join(ruta_base, nombre_liga)
      print(ruta_liga)
      
      if os.path.exists(ruta_liga):  # Verificamos si existe la carpeta de la liga
          # Iteramos sobre los equipos de la liga
          for equipo in Equipo.objects.filter(liga=liga):
              # Preparamos el nombre del equipo (sin tildes y en minúsculas)
              nombre_equipo = unidecode(equipo.nombre.lower().replace(" ", "_"))
              
              # Ruta del logo del equipo
              ruta_logo = os.path.join(ruta_liga, f"{nombre_equipo}.png")
              print(f"Verificando logo para {equipo.nombre}: {ruta_logo}")
              
              if os.path.exists(ruta_logo):  # Si existe el logo
                  # Si el logo aún no está asignado, lo asignamos
                  if not equipo.logo:  # Solo asignamos si el logo está vacío
                      with open(ruta_logo, "rb") as f:
                          equipo.logo.save(f"{nombre_equipo}.png", File(f), save=False)  # Guardamos el logo en el modelo sin guardar el objeto completo
                          equipo.save()  # Guardamos el objeto completo
                          print(f"✅ Logo asignado a {equipo.nombre}")
                  else:
                      print(f"⚠️ El logo ya está asignado a {equipo.nombre}")
              else:
                  print(f"❌ No se encontró logo para {equipo.nombre}")
      else:
          print(f"❌ No se encontró carpeta para la liga {liga.nombre}")

if __name__ == "__main__":
    importar_estadisticas()
