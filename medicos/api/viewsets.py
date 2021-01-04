from rest_framework import viewsets
from medicos.api.serializers import MedicosSerializer
from medicos.models import Medicos


class MedicosViewSet(viewsets.ModelViewSet):
    serializer_class = MedicosSerializer
    queryset = Medicos.objects.all()
