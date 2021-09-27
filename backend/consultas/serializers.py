from rest_framework import serializers
from consultas.models import Consulta
from consultas.models import Agenda
from medicos.serializers import MedicoSerializer


class ConsultaSerializer(serializers.ModelSerializer):
    medico = serializers.SerializerMethodField(read_only=True)
    dia = serializers.SerializerMethodField(read_only=True)
    horario = serializers.TimeField(format='%H:%M')
    agenda_id = serializers.IntegerField(write_only=True)
    usuario_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Consulta
        fields = ['id', 'agenda_id', 'usuario_id', 'dia',
                  'horario', 'data_agendamento', 'medico']

    def get_medico(self, instance):
        serializer = MedicoSerializer(
            instance.agenda.medico, context=self.context)
        return serializer.data

    def get_dia(self, instance):
        return instance.agenda.dia


class AgendaSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer(read_only=True)
    horarios = serializers.SerializerMethodField()

    class Meta:
        model = Agenda
        fields = ['id', 'medico', 'dia', 'horarios']

    def get_horarios(self, instance):
        queryset = instance.horarios_disponiveis()
        horarios = queryset.values_list('horario', flat=True)
        field = serializers.ListField(
            child=serializers.TimeField(format='%H:%M'))
        return field.to_representation(horarios)
