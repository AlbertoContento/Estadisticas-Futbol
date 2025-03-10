import subprocess
import time
import os
import django

# Establecer la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# Ejecutar el servidor de Django en un subproceso
def run_server():
    subprocess.Popen(["python", "manage.py", "runserver"])

# Ejecutar el comando de importación
def import_data():
    time.sleep(2)  # Espera que el servidor se inicie
    subprocess.call(["python", "manage.py", "importar_equipos"])

if __name__ == "__main__":
    run_server()
    import_data()