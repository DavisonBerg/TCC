from rest_framework import serializers
from lab_access.models import Usuario, Aluno, Professor, Tecnico, Laboratorio, Bancada

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')


class ProfessorSerializer(UsuarioSerializer):
    class Meta(UsuarioSerializer.Meta):
        model = Professor
        fields = ('__all__')


class TecnicoSerializer(UsuarioSerializer):
    class Meta(UsuarioSerializer.Meta):
        model = Tecnico
        fields = ('__all__')


class AlunoSerializer(UsuarioSerializer):
    class Meta(UsuarioSerializer.Meta):
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
