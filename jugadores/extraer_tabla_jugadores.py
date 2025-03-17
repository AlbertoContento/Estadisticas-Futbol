import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from io import StringIO
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Diccionario con los equipos y sus URLs en fbref
urls_equipos = {
    "Liverpool": "https://fbref.com/es/equipos/822bd0ba/Estadisticas-de-Liverpool",
    "Arsenal": "https://fbref.com/es/equipos/18bb7c10/Estadisticas-de-Arsenal",
    "Nottingham Forest": "https://fbref.com/es/equipos/e4a775cb/Estadisticas-de-Nottingham-Forest",
    "Chelsea": "https://fbref.com/es/equipos/cff3d9bb/Estadisticas-de-Chelsea",
    "Manchester City": "https://fbref.com/es/equipos/b8fd03ef/Estadisticas-de-Manchester-City",
    "Newcastle United": "https://fbref.com/es/equipos/b2b47a98/Estadisticas-de-Newcastle-United",
    "Brighton and Hove Albion": "https://fbref.com/es/equipos/d07537b9/Estadisticas-de-Brighton-and-Hove-Albion",
    "Aston Villa": "https://fbref.com/es/equipos/8602292d/Estadisticas-de-Aston-Villa",
    "Bournemouth": "https://fbref.com/es/equipos/4ba7cbea/Estadisticas-de-Bournemouth",
    "Fulham": "https://fbref.com/es/equipos/fd962109/Estadisticas-de-Fulham",
    "Crystal Palace": "https://fbref.com/es/equipos/47c64c55/Estadisticas-de-Crystal-Palace",
    "Brentford": "https://fbref.com/es/equipos/cd051869/Estadisticas-de-Brentford",
    "Tottenham Hotspur": "https://fbref.com/es/equipos/361ca564/Estadisticas-de-Tottenham-Hotspur",
    "Manchester United": "https://fbref.com/es/equipos/19538871/Estadisticas-de-Manchester-United",
    "Everton": "https://fbref.com/es/equipos/d3fd31cc/Estadisticas-de-Everton",
    "West Ham United": "https://fbref.com/es/equipos/7c21e445/Estadisticas-de-West-Ham-United",
    "Wolverhampton Wanderers": "https://fbref.com/es/equipos/8cec06e1/Estadisticas-de-Wolverhampton-Wanderers",
    "Ipswich Town": "https://fbref.com/es/equipos/b74092de/Estadisticas-de-Ipswich-Town",
    "Leicester City": "https://fbref.com/es/equipos/a2d435b3/Estadisticas-de-Leicester-City",
    "Southampton": "https://fbref.com/es/equipos/33c895d4/Estadisticas-de-Southampton",
    "Barcelona": "https://fbref.com/es/equipos/206d90db/Estadisticas-de-Barcelona",
    "Real Madrid": "https://fbref.com/es/equipos/53a2f082/Estadisticas-de-Real-Madrid",
    "Atletico Madrid": "https://fbref.com/es/equipos/db3b9613/Estadisticas-de-Atletico-Madrid",
    "Athletic Club": "https://fbref.com/es/equipos/2b390eca/Estadisticas-de-Athletic-Club",
    "Villarreal": "https://fbref.com/es/equipos/2a8183b3/Estadisticas-de-Villarreal",
    "Real Betis": "https://fbref.com/es/equipos/fc536746/Estadisticas-de-Real-Betis",
    "Mallorca": "https://fbref.com/es/equipos/2aa12281/Estadisticas-de-Mallorca",
    "Rayo Vallecano": "https://fbref.com/es/equipos/98e8af82/Estadisticas-de-Rayo-Vallecano",
    "Celta Vigo": "https://fbref.com/es/equipos/f25da7fb/Estadisticas-de-Celta-Vigo",
    "Sevilla": "https://fbref.com/es/equipos/ad2be733/Estadisticas-de-Sevilla",
    "Real Sociedad": "https://fbref.com/es/equipos/e31d1cd9/Estadisticas-de-Real-Sociedad",
    "Getafe": "https://fbref.com/es/equipos/7848bd64/Estadisticas-de-Getafe",
    "Girona": "https://fbref.com/es/equipos/9024a00a/Estadisticas-de-Girona",
    "Osasuna": "https://fbref.com/es/equipos/03c57e2b/Estadisticas-de-Osasuna",
    "Espanyol": "https://fbref.com/es/equipos/a8661628/Estadisticas-de-Espanyol",
    "Valencia": "https://fbref.com/es/equipos/dcc91a7b/Estadisticas-de-Valencia",
    "Leganes": "https://fbref.com/es/equipos/7c6f2c78/Estadisticas-de-Leganes",
    "Alaves": "https://fbref.com/es/equipos/8d6fd021/Estadisticas-de-Alaves",
    "Las Palmas": "https://fbref.com/es/equipos/0049d422/Estadisticas-de-Las-Palmas",
    "Valladolid": "https://fbref.com/es/equipos/17859612/Estadisticas-de-Valladolid",
    "Internazionale": "https://fbref.com/es/equipos/d609edc0/Estadisticas-de-Internazionale",
    "Napoli": "https://fbref.com/es/equipos/d48ad4ff/Estadisticas-de-Napoli",
    "Atalanta": "https://fbref.com/es/equipos/922493f3/Estadisticas-de-Atalanta",
    "Juventus": "https://fbref.com/es/equipos/e0652b02/Estadisticas-de-Juventus",
    "Lazio": "https://fbref.com/es/equipos/7213da33/Estadisticas-de-Lazio",
    "Bologna": "https://fbref.com/es/equipos/1d8099f8/Estadisticas-de-Bologna",
    "Roma": "https://fbref.com/es/equipos/cf74a709/Estadisticas-de-Roma",
    "Fiorentina": "https://fbref.com/es/equipos/421387cf/Estadisticas-de-Fiorentina",
    "Milan": "https://fbref.com/es/equipos/dc56fe14/Estadisticas-de-Milan",
    "Udinese": "https://fbref.com/es/equipos/04eea015/Estadisticas-de-Udinese",
    "Torino": "https://fbref.com/es/equipos/105360fe/Estadisticas-de-Torino",
    "Genoa": "https://fbref.com/es/equipos/658bf2de/Estadisticas-de-Genoa",
    "Como": "https://fbref.com/es/equipos/28c9c3cd/Estadisticas-de-Como",
    "Cagliari": "https://fbref.com/es/equipos/c4260e09/Estadisticas-de-Cagliari",
    "Hellas Verona": "https://fbref.com/es/equipos/0e72edf2/Estadisticas-de-Hellas-Verona",
    "Lecce": "http://fbref.com/es/equipos/ffcbe334/Estadisticas-de-Lecce",
    "Parma": "https://fbref.com/es/equipos/eab4234c/Estadisticas-de-Parma",
    "Empoli": "https://fbref.com/es/equipos/a3d88bd8/Estadisticas-de-Empoli",
    "Venezia": "https://fbref.com/es/equipos/af5d5982/Estadisticas-de-Venezia",
    "Monza": "https://fbref.com/es/equipos/21680aa4/Estadisticas-de-Monza"
}

def setup_driver():
    """
    Configura e instala automáticamente el ChromeDriver utilizando webdriver-manager.
    """
    options = Options()
    # options.add_argument("--headless")       # Modo headless
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")  # Evita problemas con el uso compartido de memoria
    options.add_argument("--remote-debugging-port=9222")  # Permite depuración remota
    options.add_argument("--enable-unsafe-swiftshader")  # Opcional: para evitar advertencias de WebGL
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def leer_tablas(url, driver):
    """
    Utiliza Selenium para abrir la URL, esperar a que cargue la tabla y obtener el HTML.
    Luego extrae las tablas HTML usando pd.read_html y las retorna.
    """
    try:
        driver.get(url)
        # Espera hasta que aparezca algún elemento <table> (hasta 30 segundos)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )
        html = driver.page_source
        tablas = pd.read_html(StringIO(html))
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
    Recorre el diccionario de URLs, utiliza Selenium para extraer las tablas de cada URL,
    e imprime la primera tabla (o la tabla de interés) en la consola.
    """
    driver = setup_driver()
    for equipo, url in urls_equipos.items():
        print(f"Extrayendo datos para {equipo} desde {url}")
        tablas = leer_tablas(url, driver)

        if tablas:
            # Cojemos la tabla 9 de estadísticas de jugadores
            tabla_jugadores = tablas[9]
            print(f"🆙{tabla_jugadores}")
            nombre_archivo = f"data/jugadores/{equipo.replace(' ', '_')}_jugadores.csv"
            tabla_jugadores.to_csv(nombre_archivo, index=False)
            print(f"Datos de {equipo} guardados en {nombre_archivo}")
        else:
            print(f"No se pudo extraer la tabla para {equipo}.")
        # Espera 5 segundos antes de pasar al siguiente equipo
        time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    extraer_datos()
