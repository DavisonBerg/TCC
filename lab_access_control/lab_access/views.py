from django.shortcuts import render
from rest_framework import generics
from lab_access.models import Aluno, Professor, Tecnico
from lab_access.serializers import AlunoSerializer,ProfessorSerializer, TecnicoSerializer

class ProfessorList(generics.ListAPIView):
    """
    Lista de todos os professores
    """
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class ProfessorCreate(generics.CreateAPIView):
    """
    Criar um novo professor
    """
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class ProfessorUpdate(generics.UpdateAPIView):
    """
    Atualiza um professor
    """
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class ProfessorDelete(generics.DestroyAPIView):
    """
    Apaga um professor
    """
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class TecnicoList(generics.ListAPIView):
    """
    Lista de todos os técnicos
    """
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer

class TecnicoCreate(generics.CreateAPIView):
    """
    Cria um novo técnico
    """
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer

class TecnicoUpdate(generics.UpdateAPIView):
    """
    Atualiza um técnico
    """
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer

class TecnicoDelete(generics.DestroyAPIView):
    """
    Apaga um técnico
    """
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer

class AlunoList(generics.ListAPIView):
    """
    Lista de todos os alunos no laboratório
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoCreate(generics.CreateAPIView):
    """
    Cria um novo aluno
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoUpdate(generics.UpdateAPIView):
    """
    Atualiza um novo aluno
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoDelete(generics.DestroyAPIView):
    """
    Apaga um aluno
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
