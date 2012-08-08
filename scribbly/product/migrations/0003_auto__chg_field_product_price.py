# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Product.price'
        db.alter_column('product_product', 'price', self.gf('django.db.models.fields.FloatField')())

    def backwards(self, orm):

        # Changing field 'Product.price'
        db.alter_column('product_product', 'price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2))

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
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['product']