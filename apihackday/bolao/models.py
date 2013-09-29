from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from mail import sendmail


class Bolao(models.Model):
    titulo = models.CharField(max_length=255)
    time_1 = models.CharField(max_length=255)
    time_2 = models.CharField(max_length=255)
    resultado_time_1 = models.IntegerField(null=True, blank=True)
    resultado_time_2 = models.IntegerField(null=True, blank=True)
    admin = models.ForeignKey(User)
    encerrado = models.BooleanField(default=False)
    participantes = models.ManyToManyField(User, related_name="participa_em", null=True, blank=True)

    def __repr__(self):
        return self.titulo

    __unicode__ = __repr__


class Aposta(models.Model):
    bolao = models.ForeignKey(Bolao, related_name='apostas')
    valor_time_1 = models.IntegerField(null=True)
    valor_time_2 = models.IntegerField(null=True)
    status_aposta = models.BooleanField(default=False)
    owner = models.ForeignKey(User)


@receiver(models.signals.post_save, sender=Bolao)
def bolao_encerrado(sender, **kwargs):
    bolao = kwargs["instance"]
    if bolao.encerrado:
        context = {"titulo_bolao": bolao.titulo, "link_resultado_bolao": "http://localhost:8000/api/v1/bolao/{}".format(bolao.id)}
        vencedores = []
        to = []
        for aposta in bolao.apostas.all():
            aposta.status_aposta = False
            if aposta.valor_time_1 == bolao.resultado_time_1 and aposta.valor_time_2 == bolao.resultado_time_2:
                aposta.status_aposta = True
                vencedores.append(aposta.owner.get_full_name())

            to.append(aposta.owner.email)
            aposta.save()

        context["vencedores"] = vencedores
        print context
        sendmail("Resultado do Bolao: {}".format(bolao.titulo), to, "mail/result-win.html", category="resultado", **context)