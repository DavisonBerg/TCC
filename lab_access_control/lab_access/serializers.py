from rest_framework import serializers
from lab_access.models import Aluno, Professor, Tecnico, Laboratorio, Bancada


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('__all__')


class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
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