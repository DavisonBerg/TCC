from rest_framework import serializers
from lab_access.models import Aluno, Laboratorio, Bancada, Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('__all__')


class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratorio
        fields = ('__all__')


class BancadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bancada
        fields = ('__all__')
