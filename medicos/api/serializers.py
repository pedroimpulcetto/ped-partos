from rest_framework import serializers
from medicos.models import Medicos


class MedicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicos
        fields = '__all__'
