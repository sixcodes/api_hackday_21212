#encoding: utf-8

from django.contrib import admin
from models import Apostador, Bolao, Aposta


class ApostadorAdmin(admin.ModelAdmin):
    pass


class BolaoAdmin(admin.ModelAdmin):
    pass


class ApostaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Apostador, ApostadorAdmin)
admin.site.register(Bolao, BolaoAdmin)
admin.site.register(Aposta, ApostaAdmin)