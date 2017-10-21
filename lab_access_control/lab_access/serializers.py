from rest_framework import serializers
from lab_access.models import Aluno, Professor, Tecnico, Laboratorio, Bancada


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('id','nome','cpf','tag')


class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = ('id','nome','cpf','tag')


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('id','nome','cpf','tag')


class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratorio
        fields = ('id','nome')


class BancadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bancada
        fields = ('id', 'numero', 'lab')