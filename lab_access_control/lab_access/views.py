from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from lab_access.models import Aluno, Professor, Tecnico, Laboratorio, Bancada
from lab_access.serializers import AlunoSerializer,ProfessorSerializer, TecnicoSerializer
from lab_access.serializers import LaboratorioSerializer, BancadaSerializer

class ProfessorList(generics.ListAPIView):
    """
    Lista de todos os professores
    """
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class ProfessorRetrieve(generics.RetrieveAPIView):
    """
    Consulta um professor
    """

    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    lookup_field = 'tag'


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


class TecnicoRetrieve(generics.RetrieveAPIView):
    """
    Consulta um tecnico
    """

    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer
    lookup_field = 'tag'


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


class AlunoRetrieve(generics.RetrieveAPIView):
    """
    Consulta um Aluno
    """

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    lookup_field = 'tag'


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


class LaboratorioList(generics.ListAPIView):
    """
    Lista todos os laboratórios do sistema
    """
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer


class LaboratorioRetrieve(generics.RetrieveAPIView):
    """
    Consulta um Laboratorio
    """

    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer


class LaboratorioCreate(generics.CreateAPIView):
    """
    Cria um novo laboratório
    """
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer


class LaboratorioUpdate(generics.UpdateAPIView):
    """
    Atualiza um Laboratorio
    """
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer


class LaboratorioDelete(generics.DestroyAPIView):
    """
    Apaga um Laboratorio
    """
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer


class BancadaList(generics.ListAPIView):
    """
    Lista todos as bancadas do sistema
    """
    queryset = Bancada.objects.all()
    serializer_class = BancadaSerializer


class BancadaRetrieve(generics.RetrieveAPIView):
    """
    Consulta uma Bancada
    """

    queryset = Bancada.objects.all()
    serializer_class = BancadaSerializer


class BancadaCreate(generics.CreateAPIView):
    """
    Cria uma nova Bancada
    """
    queryset = Bancada.objects.all()
    serializer_class = BancadaSerializer


class BancadaUpdate(generics.UpdateAPIView):
    """
    Atualiza uma Bancada
    """
    queryset = Bancada.objects.all()
    serializer_class = BancadaSerializer


class BancadaDelete(generics.DestroyAPIView):
    """
    Apaga uma Bancada
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
