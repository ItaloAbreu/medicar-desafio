from rest_framework import viewsets
from rest_framework import filters
from medicos.serializers import EspecialidadeSerializer
from medicos.serializers import MedicoSerializer
from medicos.models import Especialidade
from medicos.models import Medico


class EspecialidadeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']


class MedicoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']
