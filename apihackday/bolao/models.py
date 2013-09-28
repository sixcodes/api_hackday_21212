from django.contrib.auth.models import User
from django.db import models


class Bolao(models.Model):
    titulo = models.CharField(max_length=255)
    time_1 = models.CharField(max_length=255)
    time_2 = models.CharField(max_length=255)
    resultado_time_1 = models.IntegerField(null=True)
    resultado_time_2 = models.IntegerField(null=True)
    admin = models.ForeignKey(User)
    encerrado = models.BooleanField(default=False)


class Aposta(models.Model):
    bolao = models.ForeignKey(Bolao)
    valor_time_1 = models.IntegerField(null=True)
    valor_time_2 = models.IntegerField(null=True)
    status_aposta = models.BooleanField(default=False)