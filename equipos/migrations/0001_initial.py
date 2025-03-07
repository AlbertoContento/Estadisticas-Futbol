# Generated by Django 5.1.6 on 2025-03-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos_equipos/')),
                ('goles_marcados', models.PositiveIntegerField(default=0)),
                ('goles_contra', models.PositiveIntegerField(default=0)),
                ('asistencias', models.PositiveBigIntegerField(default=0)),
                ('penaltis_marcados', models.PositiveBigIntegerField(default=0)),
                ('tarjetas_amarillas', models.PositiveBigIntegerField(default=0)),
                ('tarjetas_rojas', models.PositiveBigIntegerField(default=0)),
                ('media_posesion', models.FloatField(default=50.0)),
                ('partidos_jugados', models.PositiveBigIntegerField(default=0)),
                ('diferencia_goles', models.PositiveBigIntegerField(default=0)),
                ('ultimo_partido', models.PositiveBigIntegerField(default=0)),
            ],
        ),
    ]
