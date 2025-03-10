import pandas as pd


# URLs de las ligas
URLS_LIGAS = {
    "La Liga": "https://fbref.com/es/comps/12/Estadisticas-de-La-Liga",
    "Serie A": "https://fbref.com/es/comps/11/Estadisticas-de-Serie-A",
    "Premier League": "https://fbref.com/es/comps/9/Estadisticas-de-Premier-League"
}

def leer_tablas(url):
    """
    Lee las tablas HTML desde una URL y retorna una lista de DataFrames.
    """
    try:
        tablas = pd.read_html(url)
        if tablas:
            print(f"Se han leído {len(tablas)} tablas desde la URL: {url}")
            return tablas
        else:
            print(f"No se encontraron tablas en la URL: {url}")
            return None
    except Exception as e:
        print(f"Error al leer las tablas desde la URL {url}: {e}")
        return None

def extraer_datos():
    """
    Extrae los datos de las ligas especificadas y las guarda en archivos CSV.
    """
    for liga, url in URLS_LIGAS.items():
        tablas = leer_tablas(url)
        if tablas:
            # Guardar las dos primeras tablas en dos DataFrames diferentes
            tabla_clasificacion = tablas[0]
            tabla_estadisticas = tablas[2]
            # Guardar los datos en archivos
            nombre_archivo = f"data/clasificacion/{liga.replace(' ', '_')}_clasificacion.csv"
            nombre_archivo2 = f"data/estadisticas/{liga.replace(' ', '_')}_estadisticas.csv"
            tabla_estadisticas.to_csv(nombre_archivo2, index=False)
            tabla_clasificacion.to_csv(nombre_archivo, index=False)
            print(f"Datos de {liga} guardados en {nombre_archivo}")
        else:
            print(f"No se pudieron extraer los datos de {liga}")

if __name__ == "__main__":
    extraer_datos()
