from django.db import models

# Aqui eu crio os tipos de usuário e quais dados eles terão

class Professor(models.Model):
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

    class Meta:
        ordering = ('nome',)
