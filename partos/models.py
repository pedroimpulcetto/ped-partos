from django.db import models
from uuid import uuid4

from medicos.models import Medicos

# Create your models here.


class Partos(models.Model):

    VIA_PARTO = [
        ('Cesárea', 'Cesárea'),
        ('Vaginal', 'Vaginal')
    ]

    SEXO_RN = [
        ('M', 'Masculino'),
        ('F', 'Feminino')
    ]

    TIPO_ANESTESIA = [
        ('PD', 'Peridural'),
        ('R', 'Raqui'),
        ('G', 'Geral')
    ]

    id_parto = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    posto_de_saude_pre_natal = models.CharField(max_length=255)
    primeiro_nome_paciente = models.CharField(max_length=255)
    sobrenome_paciente = models.CharField(max_length=255)
    data_hora_internacao = models.DateTimeField(editable=True)
    data_hora_nascimento = models.DateTimeField(editable=True)
    via_parto = models.CharField(choices=VIA_PARTO, max_length=50)
    nome_go = models.ForeignKey(
        Medicos, on_delete=models.CASCADE, blank=False, null=False, related_name='nome_go')
    nome_go_aux1 = models.ForeignKey(
        Medicos, on_delete=models.CASCADE, blank=False, null=False, related_name='nome_go_aux1')
    nome_go_aux2 = models.CharField(max_length=255)
    nome_pediatra = models.ForeignKey(
        Medicos, on_delete=models.CASCADE, blank=False, null=False, related_name='nome_pediatra')
    nome_anestesista = models.ForeignKey(
        Medicos, on_delete=models.CASCADE, blank=False, null=False, related_name='nome_anestesista')
    tipo_anestesia = models.CharField(choices=TIPO_ANESTESIA, max_length=255)
    observacoes = models.CharField(max_length=255)
    sexo_rn = models.CharField(choices=SEXO_RN, max_length=1)
    peso_nascimento_rn = models.FloatField()
    idade_gestacional = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
