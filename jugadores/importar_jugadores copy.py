import os
import pandas as pd
from jugadores.models import Jugador
from equipos.models import Equipo  # Importa el modelo de Equipo

# Definir rutas de las carpetas
RUTA_NOMBRE_EQUIPOS = os.path.join("C:\\Users\\ALBERTILLO\\Desktop\\MASTER\\PROYECTOS\\PROYECTO - Estadisticas Futbol\\data")
RUTA_JUGADORES = os.path.join("C:\\Users\\ALBERTILLO\\Desktop\\MASTER\\PROYECTOS\\PROYECTO - Estadisticas Futbol\\data\\jugadores")

# Extraer nombres de equipos a partir del archivo nombres_equipos.csv
def extraer_nombres_equipos():
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

def importar_jugadores():
    """Importa los jugadores de los archivos CSV en la carpeta de jugadores a la base de datos."""
    nombres_equipos_array = extraer_nombres_equipos()
    for nombre_equipo in nombres_equipos_array:
        print("🔍 Buscando archivo:", nombre_equipo)
        ruta_csv = os.path.join(RUTA_JUGADORES, nombre_equipo)
        if not os.path.exists(ruta_csv):
            print(f"⚠️ No se encontró {ruta_csv}")
            continue

        print(f"📄 Procesando archivo: {ruta_csv}...")
        try:
            df = pd.read_csv(ruta_csv, encoding="utf-8")
        except UnicodeDecodeError:
            print(f"❌ Error de codificación en {ruta_csv}, intentando con 'latin-1'...")
            df = pd.read_csv(ruta_csv, encoding="latin-1")

        if not comprobar_dataframe(df):
            continue

        for _, fila in df.iterrows():
            print(f"Jugador: {fila['Jugador']} - Equipo: {nombre_equipo}")
            # Buscar el equipo en la base de datos
            equipos = Equipo.objects.all()
            for equipo in equipos:
                jugador, creado = Jugador.objects.update_or_create(
                    nombre=fila["Jugador"],
                    equipo=equipo.nombre,  # Se asigna la instancia del equipo ya existente
                    defaults={
                        "posicion": fila.get("Posc", "-"),
                        "edad": fila.get("Edad", 0),
                        "pais": fila.get("País", "-"),  # Asignar el valor de pais aquí
                        "goles": fila.get("Gls", 0),
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
            print(f"✅ Jugadores importados para {nombre_equipo}")
