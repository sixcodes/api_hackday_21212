# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Apostador.twitter'
        db.add_column(u'bolao_apostador', 'twitter',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Apostador.twitter'
        db.delete_column(u'bolao_apostador', 'twitter')


    models = {
        u'bolao.apostador': {
            'Meta': {'object_name': 'Apostador'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'})
        }
    }

    complete_apps = ['bolao']