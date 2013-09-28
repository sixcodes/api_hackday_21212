from django.db import models

# Create your models here.


class Apostador(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()