# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Taxon'
        db.create_table('taxon_taxon', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('path', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['taxon.Taxon'], null=True, blank=True)),
        ))
        db.send_create_signal('taxon', ['Taxon'])


    def backwards(self, orm):
        # Deleting model 'Taxon'
        db.delete_table('taxon_taxon')


    models = {
        'taxon.taxon': {
            'Meta': {'object_name': 'Taxon'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['taxon.Taxon']", 'null': 'True', 'blank': 'True'}),
            'path': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['taxon']