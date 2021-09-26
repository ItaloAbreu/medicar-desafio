from rest_framework import viewsets
from rest_framework import filters
from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from django.forms.fields import IntegerField
from medicar.utils import MultipleValueFilter
from medicos.serializers import EspecialidadeSerializer
from medicos.serializers import MedicoSerializer
from medicos.models import Especialidade
from medicos.models import Medico


class EspecialidadeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']


class MedicoFilterSet(FilterSet):
    especialidade = MultipleValueFilter(field_class=IntegerField)

    class Meta:
        model = Medico
        fields = ['especialidade']


class MedicoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filter_class = MedicoFilterSet
    search_fields = ['nome']
