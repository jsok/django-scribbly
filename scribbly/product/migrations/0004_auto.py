# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field taxons on 'Product'
        db.create_table('product_product_taxons', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm['product.product'], null=False)),
            ('taxon', models.ForeignKey(orm['taxon.taxon'], null=False))
        ))
        db.create_unique('product_product_taxons', ['product_id', 'taxon_id'])


    def backwards(self, orm):
        # Removing M2M table for field taxons on 'Product'
        db.delete_table('product_product_taxons')


    models = {
        'pricing.productpricecategory': {
            'Meta': {'object_name': 'ProductPriceCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'product.product': {
            'Meta': {'object_name': 'Product'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'price_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pricing.ProductPriceCategory']", 'null': 'True'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'taxons': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['taxon.Taxon']", 'symmetrical': 'False'})
        },
        'taxon.taxon': {
            'Meta': {'object_name': 'Taxon'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['taxon.Taxon']", 'null': 'True', 'blank': 'True'}),
            'path': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['product']