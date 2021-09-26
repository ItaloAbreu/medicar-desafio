from django.utils import timezone
from rest_framework import viewsets
from consultas.serializers import ConsultaSerializer
from consultas.models import Consulta


class ConsultaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        now = timezone.localtime()
        return Consulta.objects.filter(dia__gte=now).exclude(
            dia=now, horario__hour__lte=now.hour,
            horario__minute__lte=now.minute).order_by(
                'dia', 'horario')
