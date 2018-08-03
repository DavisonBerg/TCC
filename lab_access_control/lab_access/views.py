from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.reverse import reverse
from lab_access.models import Aluno, Professor, Tecnico, Laboratorio, Bancada
from lab_access.serializers import AlunoSerializer, ProfessorSerializer, TecnicoSerializer
from lab_access.serializers import LaboratorioSerializer, BancadaSerializer


class RetrieveAll(generics.RetrieveAPIView):
    """
    Get any person by tag
    """
    def get(self, request, tag):
        try:
            professor = get_object_or_404(Professor, tag=tag)
            if professor:
                serializer = ProfessorSerializer(professor)
                return Response(serializer.data)
        except:
            pass
        try:
            aluno = get_object_or_404(Aluno, tag=tag)
            if aluno:
                serializer = AlunoSerializer(aluno)
                return Response(serializer.data)
        except:
            pass
        try:
            tecnico = get_object_or_404(Tecnico, tag=tag)
            if tecnico:
                serializer = TecnicoSerializer(tecnico)
                return Response(serializer.data)
        except:
            pass

        return Response(status=status.HTTP_404_NOT_FOUND)


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


class ProfessorViewHTML(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pages/professores.html'

    def get(self, request):
        queryset = Professor.objects.all()
        return Response({'title': 'Professores', 'professores': queryset})


class ProfessorDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='pages/professor-details.html'

    def get(self, request, pk):
        professor = get_object_or_404(Professor, pk=pk)
        serializer = ProfessorSerializer(professor)

        url_redirect = 'professores'
        return Response({'serializer': serializer, 'professor': professor, 'url_redirect': url_redirect})

    def post(self, request, pk):
        professor = get_object_or_404(Professor, pk=pk)
        serializer = ProfessorSerializer(professor, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'professor': professor})
        serializer.save()
        return redirect('professores')


class ProfessorNew(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='pages/professor-new.html'

    def get(self, request, *args, **kwargs):
        serializer = ProfessorSerializer()
        return Response({'serializer': serializer, 'url': reverse('professor_new'), 'url_redirect': 'professores'})

    def post(self, request, *args, **kwargs):
        professor = Professor()
        serializer = ProfessorSerializer(professor, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'professor': professor})
        serializer.save()
        return redirect('professores')

class TecnicoViewHTML(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pages/tecnicos.html'

    def get(self, request):
        queryset = Tecnico.objects.all()
        return Response({'title': 'Tecnicos', 'tecnicos': queryset})

class TecnicoDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='pages/tecnico-details.html'

    def get(self, request, pk):
        tecnico = get_object_or_404(Tecnico, pk=pk)
        serializer = TecnicoSerializer(tecnico)

        url_redirect = 'tecnicos'
        return Response({'serializer': serializer, 'tecnico': tecnico, 'url_redirect': url_redirect})

    def post(self, request, pk):
        tecnico = get_object_or_404(Tecnico, pk=pk)
        serializer = TecnicoSerializer(tecnico, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'tecnico': tecnico})
        serializer.save()
        return redirect('tecnicos')

class TecnicoNew(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='pages/tecnico-new.html'

    def get(self, request, *args, **kwargs):
        serializer = TecnicoSerializer()
        return Response({'serializer': serializer, 'url': reverse('tecnico_new'), 'url_redirect': 'tecnicos'})

    def post(self, request, *args, **kwargs):
        tecnico = Tecnico()
        serializer = TecnicoSerializer(tecnico, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'tecnico': tecnico})
        serializer.save()
        return redirect('tecnicos')

class AlunosViewHTML(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pages/alunos.html'

    def get(self, request):
        queryset = Aluno.objects.all()
        return Response({'title': 'Alunos', 'alunos': queryset})


class AlunoDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='pages/aluno-details.html'

    def get(self, request, pk):
        aluno = get_object_or_404(Aluno, pk=pk)
        serializer = AlunoSerializer(aluno)

        url_redirect = 'alunos'
        return Response({'serializer': serializer, 'aluno': aluno, 'url_redirect': url_redirect})

    def post(self, request, pk):
        aluno = get_object_or_404(Aluno, pk=pk)
        serializer = AlunoSerializer(aluno, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'aluno': aluno})
        serializer.save()
        return redirect('alunos')


class AlunoNew(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='pages/aluno-new.html'

    def get(self, request, *args, **kwargs):
        serializer = AlunoSerializer()
        return Response({'serializer': serializer, 'url': reverse('aluno_new'), 'url_redirect': 'alunos'})

    def post(self, request, *args, **kwargs):
        aluno = Aluno()
        serializer = AlunoSerializer(aluno, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'aluno': aluno})
        serializer.save()
        return redirect('alunos')
