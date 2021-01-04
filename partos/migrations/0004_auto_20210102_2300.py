# Generated by Django 3.1.4 on 2021-01-02 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0002_auto_20210102_2258'),
        ('partos', '0003_auto_20210102_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partos',
            name='nome_anestesista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nome_anestesista', to='medicos.medicos'),
        ),
        migrations.AlterField(
            model_name='partos',
            name='nome_go',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nome_go', to='medicos.medicos'),
        ),
        migrations.AlterField(
            model_name='partos',
            name='nome_go_aux1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nome_go_aux1', to='medicos.medicos'),
        ),
        migrations.AlterField(
            model_name='partos',
            name='nome_pediatra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nome_pediatra', to='medicos.medicos'),
        ),
    ]
