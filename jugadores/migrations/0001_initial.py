<<<<<<< HEAD
# Generated by Django 5.1.6 on 2025-03-17 11:56
=======
# Generated by Django 5.1.6 on 2025-03-17 12:42
>>>>>>> recuperacion

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('posicion', models.CharField(max_length=50)),
                ('edad', models.PositiveIntegerField()),
                ('pais', models.CharField(max_length=50)),
<<<<<<< HEAD
                ('goles', models.PositiveSmallIntegerField(default=0)),
=======
                ('goles', models.IntegerField(default=0)),
>>>>>>> recuperacion
                ('asistencias', models.PositiveSmallIntegerField(default=0)),
                ('goles_asistencias', models.PositiveSmallIntegerField(default=0)),
                ('tarjetas_amarillas', models.PositiveSmallIntegerField(default=0)),
                ('tarjetas_rojas', models.PositiveSmallIntegerField(default=0)),
                ('partidos_jugados', models.PositiveSmallIntegerField(default=0)),
                ('minutos_jugados', models.PositiveIntegerField(default=0)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lista_jugadores', to='equipos.equipo')),
            ],
<<<<<<< HEAD
=======
            options={
                'verbose_name': 'Jugadore',
            },
>>>>>>> recuperacion
        ),
    ]
