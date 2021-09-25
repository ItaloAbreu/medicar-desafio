from rest_framework import viewsets
from rest_framework import filters
from medicos.serializers import EspecialidadeSerializer
from medicos.models import Especialidade


class EspecialidadeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']
