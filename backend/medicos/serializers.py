from rest_framework import serializers
from medicos.models import Especialidade
from medicos.models import Medico


class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ['id', 'nome']


class MedicoSerializer(serializers.HyperlinkedModelSerializer):
    especialidade = EspecialidadeSerializer(read_only=True)

    class Meta:
        model = Medico
        fields = ['id', 'crm', 'nome', 'especialidade']
