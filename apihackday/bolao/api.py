#encoding: utf-8
from django.contrib.auth.models import User
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie.authentication import SessionAuthentication, Authentication
from tastypie.resources import ModelResource
from tastypie import fields
from models import Bolao, Aposta

default_authorization = DjangoAuthorization()
default_authentication = SessionAuthentication()

# Comente essas linhas para ligar a autenticaçao/permissoes
default_authentication = Authentication()
default_authorization = Authorization()


class ApostadorResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        authorization = default_authorization
        authentication = default_authentication
        excludes = ["password", "is_staff", "is_active", "is_superuser", ]


class ApostaResource(ModelResource):
    apostador = fields.ForeignKey(ApostadorResource, 'owner', null=True, blank=True, full=True)

    class Meta:
        queryset = Aposta.objects.all()
        authorization = default_authorization
        authentication = default_authentication

    def obj_create(self, bundle, **kwargs):
        return super(ApostaResource, self).obj_create(bundle, owner=bundle.request.user)


class BolaoResource(ModelResource):
    apostas = fields.ToManyField(ApostaResource, 'apostas', null=True, blank=True, full=True)

    class Meta:
        queryset = Bolao.objects.all()
        authorization = default_authorization
        authentication = default_authentication

    def get_object_list(self, request):
        user = request.user
        if user.is_authenticated():
            return (user.participa_em.all() | Bolao.objects.filter(admin=user)).distinct()

    def obj_create(self, bundle, **kwargs):
        return super(BolaoResource, self).obj_create(bundle, admin=bundle.request.user)
