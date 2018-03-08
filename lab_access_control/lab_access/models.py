'''
Arquivo onde são definidos os modelos que representam entidades no banco de dados

Dica: Aqui eu crio os tipos de usuário e quais dados eles terão
'''
from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

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

class Usuario(models.Model):
    '''
    Representa um usuário do laboratório
    '''
    PROFESSOR = 'professor'
    TECNICO = 'tecnico'

    USER_TYPES = (
        (PROFESSOR, _('Professor')),
        (TECNICO, _('Tecnico')),
    
    )

    nome = models.TextField()
    cpf = models.IntegerField()
    tag = models.TextField()
    tipo = models.CharField(_('Função'), choices=USER_TYPES, default=PROFESSOR, max_length=50)

    def __unicode__(self):
        return '%s' % self.nome

    def __str__(self):
        return '%s' % self.nome

    class Meta:
        ordering = ('tipo','nome',)


class Aluno(models.Model):
    nome = models.TextField()
    cpf = models.IntegerField()
    tag = models.TextField()
    lab = models.ForeignKey('Laboratorio', blank=True, null=True)
    bancada = models.ForeignKey('Bancada', blank=True, null=True)
    hora_inicio = models.DateTimeField(blank=True, null=True)
    hora_fim = models.DateTimeField(blank=True, null=True)
    '''
    professor_responsavel = models.ForeignKey(to='Professor', blank=True, null=True)
    '''
    class Meta:
        ordering = ('nome',)
