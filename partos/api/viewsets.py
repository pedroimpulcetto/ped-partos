from rest_framework import viewsets
from partos.api.serializers import PartosSerializer
from partos.models import Partos


class PartosViewSet(viewsets.ModelViewSet):
    serializer_class = PartosSerializer
    queryset = Partos.objects.all()
