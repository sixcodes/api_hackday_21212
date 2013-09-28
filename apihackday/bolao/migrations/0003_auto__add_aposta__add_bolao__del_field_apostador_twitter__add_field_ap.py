# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Aposta'
        db.create_table(u'bolao_aposta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bolao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bolao.Bolao'])),
            ('valor_time_1', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('valor_time_2', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('status_aposta', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'bolao', ['Aposta'])

        # Adding model 'Bolao'
        db.create_table(u'bolao_bolao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('time_1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('time_2', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('resultado_time_1', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('resultado_time_2', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('admin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bolao.Apostador'])),
            ('encerrado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'bolao', ['Bolao'])

        # Deleting field 'Apostador.twitter'
        db.delete_column(u'bolao_apostador', 'twitter')

        # Adding field 'Apostador.facebook_id'
        db.add_column(u'bolao_apostador', 'facebook_id',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding M2M table for field boloes on 'Apostador'
        m2m_table_name = db.shorten_name(u'bolao_apostador_boloes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apostador', models.ForeignKey(orm[u'bolao.apostador'], null=False)),
            ('bolao', models.ForeignKey(orm[u'bolao.bolao'], null=False))
        ))
        db.create_unique(m2m_table_name, ['apostador_id', 'bolao_id'])


    def backwards(self, orm):
        # Deleting model 'Aposta'
        db.delete_table(u'bolao_aposta')

        # Deleting model 'Bolao'
        db.delete_table(u'bolao_bolao')

        # Adding field 'Apostador.twitter'
        db.add_column(u'bolao_apostador', 'twitter',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True),
                      keep_default=False)

        # Deleting field 'Apostador.facebook_id'
        db.delete_column(u'bolao_apostador', 'facebook_id')

        # Removing M2M table for field boloes on 'Apostador'
        db.delete_table(db.shorten_name(u'bolao_apostador_boloes'))


    models = {
        u'bolao.aposta': {
            'Meta': {'object_name': 'Aposta'},
            'bolao': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bolao.Bolao']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status_aposta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'valor_time_1': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'valor_time_2': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'bolao.apostador': {
            'Meta': {'object_name': 'Apostador'},
            'boloes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bolao.Bolao']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'facebook_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'bolao.bolao': {
            'Meta': {'object_name': 'Bolao'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bolao.Apostador']"}),
            'encerrado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resultado_time_1': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'resultado_time_2': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'time_1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'time_2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['bolao']