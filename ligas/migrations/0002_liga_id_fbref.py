# Generated by Django 5.1.6 on 2025-03-09 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='liga',
            name='id_fbref',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
