# Generated by Django 3.1.4 on 2021-01-02 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicos',
            old_name='primero_nome',
            new_name='primeiro_nome',
        ),
    ]