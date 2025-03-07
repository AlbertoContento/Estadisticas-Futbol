futbol_stats/              # Directorio del proyecto
│── .git/                  # Carpeta de Git (tras inicializar el repo)
│── venv/                  # Entorno virtual de Python
│── requirements.txt        # Dependencias del proyecto
│── .gitignore              # Archivos a ignorar en Git
│── manage.py               # Script de administración de Django
│── config/                 # Configuración global del proyecto
│   │── __init__.py
│   │── settings.py         # Configuración de Django (Base de datos, etc.)
│   │── urls.py             # Rutas del proyecto
│   │── wsgi.py             # Servidor WSGI
│   └── asgi.py             # Servidor ASGI (opcional)
│── core/                   # Aplicación principal del proyecto
│   │── migrations/         # Migraciones de la base de datos
│   │── templates/          # HTML, CSS, Bootstrap
│   │── static/             # Archivos estáticos (CSS, JS, imágenes)
│   │── models.py           # Modelos de la base de datos
│   │── views.py            # Lógica de las vistas
│   │── urls.py             # Rutas de la aplicación
│   │── admin.py            # Panel de administración de Django
│   └── forms.py            # Formularios de Django
|__equipos/
│   │── migrations/         # Migraciones de la base de datos
│   │── templates/          # HTML, CSS, Bootstrap
│   │── models.py           # Modelos de la base de datos
│   │── views.py            # Lógica de las vistas
│   │── admin.py            # Panel de administración de Django
│   └── forms.py 
|__ligas/
│   │── migrations/         # Migraciones de la base de datos
│   │── templates/          # HTML, CSS, Bootstrap
│   │── models.py           # Modelos de la base de datos
│   │── views.py            # Lógica de las vistas
│   │── admin.py            # Panel de administración de Django
│   └── forms.py 
|__jugadores/
│   │── migrations/         # Migraciones de la base de datos
│   │── templates/          # HTML, CSS, Bootstrap
│   │── models.py           # Modelos de la base de datos
│   │── views.py            # Lógica de las vistas
│   │── admin.py            # Panel de administración de Django
│   └── forms.py 
└── db.sqlite3              # Base de datos (cambiaremos a MySQL)
