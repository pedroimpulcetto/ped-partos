from rest_framework import serializers
from partos.models import Partos


class PartosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partos
        fields = '__all__'
