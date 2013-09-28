#encoding: utf-8

from django.contrib import admin
from models import Bolao, Aposta


class BolaoAdmin(admin.ModelAdmin):
    pass


class ApostaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Bolao, BolaoAdmin)
admin.site.register(Aposta, ApostaAdmin)