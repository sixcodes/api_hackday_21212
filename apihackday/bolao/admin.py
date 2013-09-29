#encoding: utf-8

from django.contrib import admin
from models import Bolao, Aposta


class BolaoAdmin(admin.ModelAdmin):
    list_display = ["titulo", "time_1", "time_2", "admin", "encerrado"]
    pass


class ApostaAdmin(admin.ModelAdmin):
    list_display = ["bolao", "owner", "valor_time_1", "valor_time_2", "status_aposta"]
    pass


admin.site.register(Bolao, BolaoAdmin)
admin.site.register(Aposta, ApostaAdmin)