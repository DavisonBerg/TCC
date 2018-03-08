from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.reverse import reverse
from lab_access.models import Aluno, Laboratorio, Bancada, Usuario
from lab_access.serializers import AlunoSerializer
from lab_access.serializers import LaboratorioSerializer, BancadaSerializer, UsuarioSerializer


class UsuarioListCreate(generics.ListCreateAPIView):
    """
    Lista todos os usuarios ou cria um novo usuario
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioView(generics.RetrieveUpdateDestroyAPIView):
    """
    Consulta, atualiza ou deleta um usuario
    """

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


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

'''
class ValidateAluno(generics.RetrieveAPIView):
    """
    Valida se um aluno tem permissão para lab, bancada e se tem um professor responsável
    """
    serializer_class = AlunoSerializer
    lookup_field = 'tag'
    queryset = Aluno.objects.filter(professor_responsavel__isnull=False, bancada__isnull=False, lab__isnull=False)
'''


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
        serializer = AlunoSerializer(usuario, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'aluno': aluno})
        serializer.save()
        return redirect('alunos')


class UsuariosViewHTML(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pages/usuarios.html'

    def get(self, request):
        queryset = Usuario.objects.all()
        return Response({'title': 'Usuarios', 'usuarios': queryset})


class UsuarioDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='pages/usuario-details.html'

    def get(self, request, pk):
        usuario = get_object_or_404(Usuario, pk=pk)
        serializer = UsuarioSerializer(usuario)

        url_redirect = 'usuarios'
        if usuario.tipo == 'professor':
            url_redirect = 'professores'
        elif usuario.tipo == 'tecnico':
            url_redirect = 'tecnicos'
        return Response({'serializer': serializer, 'usuario': usuario, 'url_redirect': url_redirect})

    def post(self, request, pk):
        usuario = get_object_or_404(Usuario, pk=pk)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'usuario': usuario})
        serializer.save()
        if usuario.tipo == 'professor':
            return redirect('professores')
        elif usuario.tipo == 'tecnico':
            return redirect('tecnicos')
        else:
            return redirect('usuarios')


class UsuarioNew(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='pages/usuario-new.html'

    def get(self, request, *args, **kwargs):
        serializer = UsuarioSerializer()
        return Response({'serializer': serializer, 'url': reverse('usuario_new'), 'url_redirect': 'usuarios'})

    def post(self, request, *args, **kwargs):
        usuario = Usuario()
        serializer = UsuarioSerializer(usuario, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'usuario': usuario})
        serializer.save()
        return redirect('usuarios')


class ProfessorViewHTML(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pages/usuarios.html'

    def get(self, request):
        queryset = Usuario.objects.filter(tipo__in=[Usuario.PROFESSOR])
        return Response({'title': 'Professores', 'usuarios': queryset})


class TecnicoViewHTML(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pages/usuarios.html'

    def get(self, request):
        queryset = Usuario.objects.filter(tipo__in=[Usuario.TECNICO])
        return Response({'title': 'Tecnicos', 'usuarios': queryset})
