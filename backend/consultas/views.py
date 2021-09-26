from django.utils import timezone
from rest_framework import viewsets
from django_filters import FilterSet
from django_filters import DateFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.forms.fields import IntegerField
from medicar.utils import MultipleValueFilter
from consultas.serializers import ConsultaSerializer
from consultas.serializers import AgendaSerializer
from consultas.models import Consulta
from consultas.models import Agenda


class ConsultaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        now = timezone.localtime()
        return Consulta.objects.filter(agenda__dia__gte=now).exclude(
            agenda__dia=now, horario__hour__lte=now.hour,
            horario__minute__lte=now.minute).order_by(
                'agenda__dia', 'horario')


class AgendaFilterSet(FilterSet):
    medico = MultipleValueFilter(field_class=IntegerField)
    especialidade = MultipleValueFilter(
        method='medico_field_in', field_class=IntegerField)
    data_inicio = DateFilter('dia', lookup_expr='gte')
    data_final = DateFilter('dia', lookup_expr='lte')

    class Meta:
        model = Agenda
        fields = ['especialidade', 'medico']

    def medico_field_in(self, queryset, name, value):
        lookup = {
            f'medico__{name}__in': value
        }
        return queryset.filter(**lookup)


class AgendaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AgendaSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = AgendaFilterSet

    def get_queryset(self):
        now = timezone.localtime()
        queryset = Agenda.objects.filter(dia__gte=now).order_by('dia')
        ids_to_exlude = [
            agenda.id for agenda in queryset if not agenda.horarios_disponiveis()]
        return queryset.exclude(id__in=ids_to_exlude)
