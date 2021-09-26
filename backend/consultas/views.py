from django.utils import timezone
from rest_framework import viewsets
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


class AgendaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AgendaSerializer

    def get_queryset(self):
        now = timezone.localtime()
        return Agenda.objects.filter(dia__gte=now).order_by('dia')
