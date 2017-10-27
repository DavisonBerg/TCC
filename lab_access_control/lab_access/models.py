'''
Arquivo onde são definidos os modelos que representam entidades no banco de dados

Dica: Aqui eu crio os tipos de usuário e quais dados eles terão
'''
from django.db import models


class Laboratorio(models.Model):
    nome = models.TextField()

    class Meta:
        ordering = ('nome',)


class Bancada(models.Model):
    numero = models.IntegerField()
    lab = models.ForeignKey('Laboratorio')

    class Meta:
        ordering = ('numero',)


class Professor(models.Model):
    '''
    Classe Professor
    '''
    nome = models.TextField()
    cpf = models.IntegerField()
    tag = models.TextField()

    class Meta:
        ordering = ('nome',)


class Tecnico(models.Model):
    nome = models.TextField()
    cpf = models.IntegerField()
    tag = models.TextField()

    class Meta:
        ordering = ('nome',)


class Aluno(models.Model):
    nome = models.TextField()
    cpf = models.IntegerField()
    tag = models.TextField()
    lab = models.ForeignKey('Laboratorio', blank=True, null=True)
    bancada = models.ForeignKey('Bancada', blank=True, null=True)
    hora_inicio = models.DateTimeField(blank=True, null=True)
    hora_fim = models.DateTimeField(blank=True, null=True)
    professor_responsavel = models.ForeignKey('Professor', blank=True, null=True)

    class Meta:
        ordering = ('nome',)
