Configuración de Django con MySQL en Windows

Este documento contiene los pasos necesarios para configurar Django con MySQL en Windows, incluyendo la instalación de dependencias, configuración de la base de datos y comandos útiles.

1. Instalación de dependencias

Instalar Python y Virtualenv

Asegúrate de tener Python instalado. Luego, crea un entorno virtual y actívalo:

python -m venv venv
venv\Scripts\activate

Instalar Django y dependencias necesarias

pip install django mysqlclient

Para guardar las dependencias en un archivo:

pip freeze > requirements.txt

Para instalar dependencias en otro entorno:

pip install -r requirements.txt

2. Instalación y Configuración de MySQL

Instalar MySQL Server

Descarga e instala MySQL Server desde https://dev.mysql.com/downloads/mysql/.

Crear una base de datos y usuario para Django

Abre MySQL desde PowerShell:

mysql -u root -p

Ejecuta los siguientes comandos SQL:

CREATE DATABASE mydb;
CREATE USER 'django_user_db'@'localhost' IDENTIFIED BY 'django_user_pass';
GRANT ALL PRIVILEGES ON mydb.* TO 'django_user_db'@'localhost';
FLUSH PRIVILEGES;

3. Configurar Django con MySQL

En el archivo settings.py de tu proyecto Django, agrega la configuración de MySQL:

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

Aplica las migraciones:

python manage.py migrate

4. Respaldo y Restauración de la Base de Datos

Para hacer un backup de la base de datos:

mysqldump -u django_user_db -p mydb > backup.sql

Para restaurar el backup:

mysql -u django_user_db -p mydb < backup.sql

5. Comandos útiles

Crear una aplicación Django

python manage.py startapp mi_app

Ejecutar el servidor de desarrollo

python manage.py runserver

Crear un superusuario para el panel de administración

python manage.py createsuperuser

6. Solución de errores comunes

Error: django.db.utils.OperationalError: (2002, "Can't connect to MySQL server")

Asegúrate de que MySQL está ejecutándose.

Verifica que la configuración en settings.py es correcta.

Error: ModuleNotFoundError: No module named 'MySQLdb'

Instala mysqlclient con:

pip install mysqlclient

Este archivo se recomienda mantener actualizado con cualquier cambio en la configuración de tu proyecto.