'''
Arquivo onde são definidos os modelos que representam entidades no banco de dados

Dica: Aqui eu crio os tipos de usuário e quais dados eles terão
'''
from django.db import models


class Laboratorio(models.Model):
    nome = models.TextField()

    def __unicode__(self):
        return '%s' % self.nome

    def __str__(self):
        return '%s' % self.nome


    class Meta:
        ordering = ('nome',)


class Bancada(models.Model):
    numero = models.IntegerField()
    lab = models.ForeignKey('Laboratorio')

    def __unicode__(self):
        return 'Lab %s - Bancada %s' % (self.lab.nome, self.numero)

    def __str__(self):
        return 'Lab %s - Bancada %s' % (self.lab.nome, self.numero)


    class Meta:
        ordering = ('numero',)


class Professor(models.Model):
    '''
    Classe Professor
    '''
    nome = models.TextField()
    cpf = models.IntegerField()
    tag = models.TextField()
    tipo = models.TextField(default = 'Professor')

    def __unicode__(self):
        return '%s' % self.nome

    def __str__(self):
        return '%s' % self.nome

    class Meta:
        ordering = ('nome',)


class Tecnico(models.Model):
    nome = models.TextField()
    cpf = models.IntegerField()
    tag = models.TextField()
    tipo = models.TextField(default = 'Tecnico')

    def __unicode__(self):
        return '%s' % self.nome

    def __str__(self):
        return '%s' % self.nome

    class Meta:
        ordering = ('nome',)


class Aluno(models.Model):
    nome = models.TextField()
    tipo = models.TextField(default = 'Aluno')
    cpf = models.IntegerField()
    tag = models.TextField()
    lab = models.ForeignKey('Laboratorio', blank=True, null=True)
    bancada = models.ForeignKey('Bancada', blank=True, null=True)
    hora_inicio = models.DateTimeField(blank=True, null=True)
    hora_fim = models.DateTimeField(blank=True, null=True)
    professor_responsavel = models.ForeignKey(to='Professor', blank=True, null=True)

    class Meta:
        ordering = ('nome',)
