# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'DiscountMatrixEntry.discount'
        db.alter_column('pricing_discountmatrixentry', 'discount', self.gf('django.db.models.fields.FloatField')())

    def backwards(self, orm):

        # Changing field 'DiscountMatrixEntry.discount'
        db.alter_column('pricing_discountmatrixentry', 'discount', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2))

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
        }
    }

    complete_apps = ['pricing']