# Generated by Django 5.1.7 on 2025-03-14 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Liga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('abreviatura', models.CharField(max_length=10, unique=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos_ligas/')),
                ('id_fbref', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
