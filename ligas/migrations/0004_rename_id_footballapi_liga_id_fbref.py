# Generated by Django 5.1.6 on 2025-03-10 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ligas', '0003_rename_id_fbref_liga_id_footballapi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='liga',
            old_name='id_footballAPI',
            new_name='id_fbref',
        ),
    ]
