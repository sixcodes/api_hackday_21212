#encoding: utf-8
from django.contrib.auth.models import User
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import SessionAuthentication
from tastypie.resources import ModelResource


class ApostadorResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        authorization = DjangoAuthorization()
        authentication = SessionAuthentication()