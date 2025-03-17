# ⚽ Proyecto de Estadísticas de Fútbol

Este proyecto tiene como objetivo ofrecer un sistema para gestionar estadísticas de fútbol a través de un sitio web desarrollado con **Django**. El sistema incluye datos sobre ligas, equipos y jugadores, permitiendo visualizar estadísticas detalladas y realizar acciones de administración.

---

## 🖥️ Características

- **📊 Estadísticas de Ligas**: Información detallada sobre las ligas de fútbol.
- **🏆 Equipos y Jugadores**: Datos individuales de cada equipo y jugador, incluyendo goles, asistencias, y otros indicadores clave de rendimiento.
- **🔧 Administración en Django**: Panel de administración donde se gestionan ligas, equipos y jugadores.
- **🔑 Administración de usuarios**: Panel de administración donde se gestionar usuarios asi como loguearse para poder ver las estadisticas.

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.9.16**
- **Django 5.1.6**
- **MySQL** como base de datos
- Librerías necesarias:
  - `asgiref==3.8.1`
  - `attrs==25.1.0`
  - `beautifulsoup4==4.13.3`
  - `certifi==2025.1.31`
  - `cffi==1.17.1`
  - `charset-normalizer==3.4.1`
  - `cryptography==44.0.2`
  - `Django==5.1.6`
  - `django-debug-toolbar==5.0.1`
  - `django-extensions==3.2.3`
  - `h11==0.14.0`
  - `idna==3.10`
  - `lxml==5.3.1`
  - `mysqlclient==2.2.7`
  - `numpy==2.2.3`
  - `pandas==2.2.3`
  - `pillow==11.1.0`
  - `requests==2.32.3`
  - `selenium==4.29.0`
  - `webdriver-manager==4.0.2`

---

## Cómo Usar ❓

1. Clona el repositorio:

   ```bash
   git clone https://github.com/AlbertoContento/Estadisticas-Futbol.git
    ```

2. Instalación de dependencias

Instalar Python y Virtualenv

Asegúrate de tener Python instalado. Luego, crea un entorno virtual y actívalo:
``` bash
python -m venv venv
venv\Scripts\activate
```
Instalar Django y dependencias necesarias
``` bash

pip install django mysqlclient
```
Para guardar las dependencias en un archivo:
``` bash
pip freeze > requirements.txt
```
Para instalar dependencias en otro entorno:
``` bash

pip install -r requirements.txt
```
3. Instalación y Configuración de MySQL

Instalar MySQL Server

Descarga e instala MySQL Server desde https://dev.mysql.com/downloads/mysql/.

Crear una base de datos y usuario para Django

Abre MySQL desde PowerShell:
``` bash

mysql -u root -p
```
Ejecuta los siguientes comandos SQL:
``` bash

CREATE DATABASE mydb;
CREATE USER 'django_user_db'@'localhost' IDENTIFIED BY 'django_user_pass';
GRANT ALL PRIVILEGES ON mydb.* TO 'django_user_db'@'localhost';
FLUSH PRIVILEGES;
```
4. Configurar Django con MySQL

En el archivo settings.py de tu proyecto Django, agrega la configuración de MySQL:
``` bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'django_user_db',
        'PASSWORD': 'django_user_pass',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}
```
Aplica las migraciones:
``` bash
python manage.py migrate
```
5. Respaldo y Restauración de la Base de Datos

Para hacer un backup de la base de datos:
``` bash
mysqldump -u django_user_db -p mydb > backup.sql
```
Para restaurar el backup:
``` bash
mysql -u django_user_db -p mydb < backup.sql
```
6. Comandos útiles

Crear una aplicación Django
``` bash
python manage.py startapp mi_app
```
Ejecutar el servidor de desarrollo
``` bash
python manage.py runserver
```
Crear un superusuario para el panel de administración
``` bash
python manage.py createsuperuser
```
7. Instalacion de mysqlclient

Instala mysqlclient con:
``` bash
pip install mysqlclient
```

El programa utiliza webbrowser para abrir el navegador y reproducir la musica y threading para comprobar la hora cada segundo

📄 Licencia

🎨 Capturas de Pantalla 
Aquí tienes una vista previa de cómo luce el proyecto:
![Pantalla Principal](https://github.com/AlbertoContento/Estadisticas-Futbol/blob/main/assets/Captura%20de%20pantalla.png)
![Pantalla Principal](https://github.com/AlbertoContento/Estadisticas-Futbol/blob/main/assets/Captura%20de%20pantalla1.png)
