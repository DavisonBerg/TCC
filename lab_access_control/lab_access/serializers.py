from rest_framework import serializers
from lab_access.models import Aluno
from lab_access.models import Professor
from lab_access.models import Tecnico

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
