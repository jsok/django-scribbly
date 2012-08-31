# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TaxCategory'
        db.create_table('pricing_taxcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('rate', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal('pricing', ['TaxCategory'])


    def backwards(self, orm):
        # Deleting model 'TaxCategory'
        db.delete_table('pricing_taxcategory')


    models = {
        'pricing.customerpricecategory': {
            'Meta': {'object_name': 'CustomerPriceCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'pricing.discountmatrixentry': {
            'Meta': {'object_name': 'DiscountMatrixEntry'},
            'customer_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pricing.CustomerPriceCategory']"}),
            'discount': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pricing.ProductPriceCategory']"})
        },
        'pricing.productpricecategory': {
            'Meta': {'object_name': 'ProductPriceCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'pricing.taxcategory': {
            'Meta': {'object_name': 'TaxCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'rate': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        }
    }

    complete_apps = ['pricing']