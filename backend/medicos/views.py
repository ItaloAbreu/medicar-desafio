from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from medicos.serializers import EspecialidadeSerializer
from medicos.models import Especialidade


class EspecialidadeViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Especialidade.objects.all()
        serializer = EspecialidadeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Especialidade.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = EspecialidadeSerializer(user)
        return Response(serializer.data)
