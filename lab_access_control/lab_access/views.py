from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from lab_access.models import Aluno, Professor, Tecnico, Laboratorio, Bancada
from lab_access.serializers import AlunoSerializer,ProfessorSerializer, TecnicoSerializer
from lab_access.serializers import LaboratorioSerializer, BancadaSerializer

class ProfessorListCreate(generics.ListCreateAPIView):
    """
    Lista todos os professores ou cria um novo professor
    """
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class ProfessorView(generics.RetrieveUpdateDestroyAPIView):
    """
    Consulta, atualiza ou deleta um professor
    """

    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    lookup_field = 'tag'


class TecnicoListCreate(generics.ListCreateAPIView):
    """
    Lista todos os técnicos ou cria um novo técnico
    """
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer


class TecnicoView(generics.RetrieveUpdateDestroyAPIView):
    """
    Consulta, atualiza ou deleta um tecnico
    """

    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer
    lookup_field = 'tag'


class AlunoListCreate(generics.ListCreateAPIView):
    """
    Lista todos os alunos ou cria um novo aluno
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class AlunoView(generics.RetrieveUpdateDestroyAPIView):
    """
    Consulta, atualiza ou deleta um Aluno
    """

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    lookup_field = 'tag'


class LaboratorioListCreate(generics.ListCreateAPIView):
    """
    Lista todos os laboratórios ou cria um novo laboratório
    """
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer


class LaboratorioView(generics.RetrieveUpdateDestroyAPIView):
    """
    Consulta, atualiza ou deleta um Laboratorio
    """

    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer


class BancadaListCreate(generics.ListCreateAPIView):
    """
    Lista todos as bancadas ou cria uma nova bancada
    """
    queryset = Bancada.objects.all()
    serializer_class = BancadaSerializer


class BancadaView(generics.RetrieveUpdateDestroyAPIView):
    """
    Consulta, atualiza ou deleta uma Bancada
    """

    queryset = Bancada.objects.all()
    serializer_class = BancadaSerializer


class ValidateAluno(generics.RetrieveAPIView):
    """
    Valida se um aluno tem permissão para lab, bancada e se tem um professor responsável
    """
    serializer_class = AlunoSerializer
    lookup_field = 'tag'
    queryset = Aluno.objects.filter(professor_responsavel__isnull=False, bancada__isnull=False, lab__isnull=False)
