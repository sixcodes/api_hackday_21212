#encoding: utf-8
from django.contrib.auth.models import User
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie.authentication import SessionAuthentication, Authentication
from tastypie.resources import ModelResource
from models import Bolao

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


class BolaoResource(ModelResource):
    class Meta:
        queryset = Bolao.objects.all()
        authorization = default_authorization
        authentication = default_authentication