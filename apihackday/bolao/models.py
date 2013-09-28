from django.db import models


class Apostador(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    facebook_id = models.IntegerField(null=True)
    boloes = models.ManyToManyField('Bolao')


class Bolao(models.Model):
    titulo = models.CharField(max_length=255)
    time_1 = models.CharField(max_length=255)
    time_2 = models.CharField(max_length=255)
    resultado_time_1 = models.IntegerField(null=True)
    resultado_time_2 = models.IntegerField(null=True)
    admin = models.ForeignKey(Apostador)
    encerrado = models.BooleanField(default=False)


class Aposta(models.Model):
    bolao = models.ForeignKey(Bolao)
    valor_time_1 = models.IntegerField(null=True)
    valor_time_2 = models.IntegerField(null=True)
    status_aposta = models.BooleanField(default=False)