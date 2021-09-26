from rest_framework import serializers
from consultas.models import Consulta
from medicos.serializers import MedicoSerializer


class ConsultaSerializer(serializers.HyperlinkedModelSerializer):
    medico = MedicoSerializer(read_only=True)
    horario = serializers.TimeField(format='%H:%M')

    class Meta:
        model = Consulta
        fields = ['id', 'dia', 'horario', 'data_agendamento', 'medico']
