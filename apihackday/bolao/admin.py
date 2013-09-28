#encoding: utf-8

from django.contrib import admin
from models import Apostador


class ApostadorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Apostador, ApostadorAdmin)