from rest_framework import serializers
from consultas.models import Consulta
from medicos.serializers import MedicoSerializer


class ConsultaSerializer(serializers.HyperlinkedModelSerializer):
    medico = serializers.SerializerMethodField()
    dia = serializers.SerializerMethodField()
    horario = serializers.TimeField(format='%H:%M')

    class Meta:
        model = Consulta
        fields = ['id', 'dia', 'horario', 'data_agendamento', 'medico']

    def get_medico(self, instance):
        serializer = MedicoSerializer(instance.agenda.medico, context=self.context)
        return serializer.data

    def get_dia(self, instance):
        return instance.agenda.dia
