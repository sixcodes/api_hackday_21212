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
        context = {"titulo_bolao": bolao.titulo, "link_resultado_bolao": "http://localhost:8000/bolao/{}".format(bolao.id)}
        vencedores = []
        to = []
        for aposta in bolao.apostas.all():
            aposta.status_aposta = False
            if str(aposta.valor_time_1) == str(bolao.resultado_time_1) and str(aposta.valor_time_2) == str(bolao.resultado_time_2):
                aposta.status_aposta = True
                vencedores.append(aposta.owner.get_full_name())

            to.append(aposta.owner.email)
            aposta.save()

        context["vencedores"] = vencedores
        print context
        sendmail("Resultado do Bolao: {}".format(bolao.titulo), to, "mail/result-win.html", category="resultado", **context)


@receiver(models.signals.post_save, sender=Aposta)
def nova_aposta(sender, **kwargs):

    if not kwargs["created"]:
        return

    aposta = kwargs['instance']
    bolao = aposta.bolao
    context = {"time_1": bolao.time_1, "valor_1": aposta.valor_time_1,
               "time_2": bolao.time_2, "valor_2": aposta.valor_time_2,
               "apostador": aposta.owner.get_full_name(), "link_bolao": "http://localhost:8000/bolao/{}".format(bolao.id)}

    to = [aposta.owner.email for aposta in bolao.apostas.all()]
    print "to=", to
    sendmail("Nova Aposta: Bolao {}".format(bolao.titulo), to, "mail/nova-aposta.html", category="nova-aposta", **context)
