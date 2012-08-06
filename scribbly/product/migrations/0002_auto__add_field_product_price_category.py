# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.price_category'
        db.add_column('product_product', 'price_category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pricing.ProductPriceCategory'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.price_category'
        db.delete_column('product_product', 'price_category_id')


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
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'price_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pricing.ProductPriceCategory']", 'null': 'True'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['product']