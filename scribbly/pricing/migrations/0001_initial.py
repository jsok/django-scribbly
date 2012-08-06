# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductPriceCategory'
        db.create_table('pricing_productpricecategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('pricing', ['ProductPriceCategory'])

        # Adding model 'CustomerPriceCategory'
        db.create_table('pricing_customerpricecategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('pricing', ['CustomerPriceCategory'])

        # Adding model 'DiscountMatrixEntry'
        db.create_table('pricing_discountmatrixentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('discount', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('product_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pricing.ProductPriceCategory'])),
            ('customer_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pricing.CustomerPriceCategory'])),
        ))
        db.send_create_signal('pricing', ['DiscountMatrixEntry'])


    def backwards(self, orm):
        # Deleting model 'ProductPriceCategory'
        db.delete_table('pricing_productpricecategory')

        # Deleting model 'CustomerPriceCategory'
        db.delete_table('pricing_customerpricecategory')

        # Deleting model 'DiscountMatrixEntry'
        db.delete_table('pricing_discountmatrixentry')


    models = {
        'pricing.customerpricecategory': {
            'Meta': {'object_name': 'CustomerPriceCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'pricing.discountmatrixentry': {
            'Meta': {'object_name': 'DiscountMatrixEntry'},
            'customer_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pricing.CustomerPriceCategory']"}),
            'discount': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
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