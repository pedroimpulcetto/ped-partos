from django.db import models
from uuid import uuid4

# Create your models here.


class Medicos(models.Model):

    ESPECIALIDADES = [
        ('Ginecologia e Obstetrícia', 'Ginecologia e Obstetrícia'),
        ('Pediatria', 'Pediatria'),
        ('Anestesiologia', 'Anestesiologia')
    ]

    id_medico = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    primeiro_nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    crm = models.IntegerField()
    especialidade = models.CharField(choices=ESPECIALIDADES, max_length=255)

    def __str__(self, ):
        return f'{self.primeiro_nome} - {self.crm} - {self.especialidade}'
