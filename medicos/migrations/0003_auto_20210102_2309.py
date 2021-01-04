# Generated by Django 3.1.4 on 2021-01-02 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0002_auto_20210102_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicos',
            name='especialidade',
            field=models.CharField(choices=[('Ginecologia e Obstetrícia', 'GO'), ('Pediatria', 'PED'), ('Anestesiologia', 'AN')], max_length=255),
        ),
    ]
