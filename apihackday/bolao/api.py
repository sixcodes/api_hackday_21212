#encoding: utf-8
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import SessionAuthentication
from tastypie.resources import ModelResource
from models import Apostador


class ApostadorResource(ModelResource):
    class Meta:
        queryset = Apostador.objects.all()
        resource_name = 'apostador'
        authorization = DjangoAuthorization()
        authentication = SessionAuthentication()