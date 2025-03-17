import os


# Definir rutas de las carpetas
RUTA_JUGADORES = os.path.join("C:\\Users\\ALBERTILLO\\Desktop\\MASTER\\PROYECTOS\\PROYECTO - Estadisticas Futbol\\data")

def extraer_nombres_equipos():
    """Extrae los nombres de los equipos de los archivos CSV en la carpeta de jugadores."""
    nombres_equipos = set()
    for archivo in os.listdir(RUTA_JUGADORES):
        if archivo.endswith(".csv"):
            #Guardamos el nombre del archiv completo
            nombres_equipos.add(archivo)
    return nombres_equipos

def guardar_nombre_csv():
    """Guarda los nombres de los equipos en un archivo CSV."""
    nombres_equipos = extraer_nombres_equipos()
    nombre_archivo = os.path.join(RUTA_JUGADORES, "nombres_equipos.csv")
    with open(nombre_archivo, "w") as f:
        for nombre_equipo in nombres_equipos:
            f.write(f"{nombre_equipo}\n")
    print(f"Se han guardado los nombres de los equipos en {nombre_archivo}.")
    return nombre_archivo

if __name__ == "__main__":
    nombre_archivo = guardar_nombre_csv()
    print(f"Se han encontrado {nombre_archivo} archivos CSV en la carpeta de jugadores.")
