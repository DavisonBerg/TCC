from django.shortcuts import render
from rest_framework import generics
from lab_access.models import Aluno
from lab_access.serializers import AlunoSerializer
from lab_access.models import Professor
from lab_access.serializers import ProfessorSerializer
from lab_access.models import Tecnico
from lab_access.serializers import TecnicoSerializer

class ProfessorList(generics.ListAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class TecnicoList(generics.ListAPIView):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer

class AlunoList(generics.ListAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
