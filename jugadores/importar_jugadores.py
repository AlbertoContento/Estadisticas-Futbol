import os
import pandas as pd
from jugadores.models import Jugador
from equipos.models import Equipo  # Importa el modelo de Equipo

# Definir rutas de las carpetas
RUTA_NOMBRE_EQUIPOS = os.path.join(
    "C:\\Users\\ALBERTILLO\\Desktop\\MASTER\\PROYECTOS\\PROYECTO - Estadisticas Futbol\\data"
)
RUTA_JUGADORES = os.path.join(
    "C:\\Users\\ALBERTILLO\\Desktop\\MASTER\\PROYECTOS\\PROYECTO - Estadisticas Futbol\\data\\jugadores"
)

def extraer_nombres_equipos():
    """Extrae los nombres de archivo (por ejemplo, 'Celta_Vigo_jugadores.csv') desde nombres_equipos.csv."""
    array_nombres_equipos = []
    with open(os.path.join(RUTA_NOMBRE_EQUIPOS, "nombres_equipos.csv"), "r", encoding="utf-8") as f:
        for linea in f:
            array_nombres_equipos.append(linea.strip())
    print(f"Se han encontrado {len(array_nombres_equipos)} equipos en el archivo nombres_equipos.csv.")
    return array_nombres_equipos

def comprobar_dataframe(df):
    """Comprueba si el DataFrame tiene datos."""
    if df.empty:
        print("⚠️ El DataFrame está vacío o no tiene datos válidos.")
        return False
    print(f"✔️ DataFrame cargado con {len(df)} filas.")
    return True

def normalizar_nombre_equipo(nombre_archivo):
    """
    Dado el nombre del archivo, obtiene el nombre del equipo esperado.
    Ejemplo: "Celta_Vigo_jugadores.csv" -> "Celta Vigo"
    """
    # Elimina el sufijo (ajusta según corresponda)
    nombre = nombre_archivo.replace("_jugadores.csv", "")
    # Reemplaza los guiones bajos por espacios
    nombre = nombre.replace("_", " ").strip()
    #Estos equipos tienen diferente nombre lo hacemos manual
    if nombre == "Brighton and Hove Albion":
        nombre = "Brighton"
    if nombre == "Internazionale":
        nombre = "Inter"
    if nombre == "Nottingham Forest":
        nombre = "Nott'ham Forest"
    if nombre == "Manchester United":
        nombre = "Manchester Utd"
    if nombre == "Real Betis":
        nombre = "Betis"
    if nombre == "Wolverhampton Wanderers":
        nombre = "Wolves"
    if nombre == "Newcastle United":
        nombre = "Newcastle Utd"
    if nombre == "West Ham United":
        nombre = "West Ham"
    if nombre == "Tottenham Hotspur":
        nombre = "Tottenham"
    return nombre

def importar_jugadores():
    """Importa los jugadores de los archivos CSV en la carpeta de jugadores a la base de datos."""
    nombres_archivos = extraer_nombres_equipos()
    for nombre_archivo in nombres_archivos:
        print("🔍 Buscando archivo:", nombre_archivo)
        ruta_csv = os.path.join(RUTA_JUGADORES, nombre_archivo)
        if not os.path.exists(ruta_csv):
            print(f"⚠️ No se encontró {ruta_csv}")
            continue

        print(f"📄 Procesando archivo: {ruta_csv}...")

        try:
            df = pd.read_csv(ruta_csv, encoding="utf-8")
            print(f"✔️ Archivo {ruta_csv} cargado correctamente.")
        except UnicodeDecodeError:
            print(f"❌ Error de codificación en {ruta_csv}, intentando con 'latin-1'...")
            df = pd.read_csv(ruta_csv, encoding="latin-1")

        if not comprobar_dataframe(df):
            continue

        # Determinar el nombre del equipo a partir del nombre del archivo
        nombre_equipo_bd = normalizar_nombre_equipo(nombre_archivo)
        print(f"🔍 Buscando equipo en la base de datos: {nombre_equipo_bd}...")        
        equipo_obj = Equipo.objects.get(nombre__iexact=nombre_equipo_bd)

        try:
            equipo_obj = Equipo.objects.get(nombre__iexact=nombre_equipo_bd)
        except Equipo.DoesNotExist:
            print(f"⚠️ El equipo '{nombre_equipo_bd}' no existe en la base de datos. Se omitirá este archivo.")
            continue
        # Procesar cada jugador en el CSV usando el equipo obtenido
        for _, fila in df.iterrows():
            print(f"Jugador: {fila['Jugador']} - Equipo: {equipo_obj.nombre}")

            edad_modificada = fila.get("Edad", 0)
            if edad_modificada == "N/A":
                edad_modificada = 0
            else:
                edad_modificada = int(edad_modificada.split("-")[0])

            jugador, creado = Jugador.objects.update_or_create(
                nombre=fila["Jugador"],
                equipo=equipo_obj,  # Se pasa la instancia del equipo
                defaults={
                    "posicion": fila.get("Posc", "-"),
                    "edad": edad_modificada,
                    "pais": fila.get("País", "-"),
                    "goles": fila.get("Gls.", 0),
                    "asistencias": fila.get("Ass", 0),
                    "goles_asistencias": fila.get("G+A", 0),
                    "tarjetas_amarillas": fila.get("TA", 0),
                    "tarjetas_rojas": fila.get("TR", 0),
                    "partidos_jugados": fila.get("PJ", 0),
                    "minutos_jugados": fila.get("Mín", 0),
                },
            )
            if creado:
                print(f"✅ Jugador {jugador} creado correctamente")
            else:
                print(f"✅ Jugador {jugador} actualizado correctamente")
        print(f"✅ Jugadores importados para {equipo_obj.nombre}")
    print("✅FINALIZACINO DE IMPORTACION✅")
