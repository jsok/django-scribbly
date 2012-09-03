from decimal import Decimal
from django.db import models

from pricing.models import ProductPriceCategory
from taxon.models import Taxon

class Product(models.Model):
    """
    A product in the inventory which can be sold.
    """
    sku = models.CharField("SKU", max_length=50)
    slug = models.SlugField(unique=True, max_length=80)
    name = models.CharField(max_length=100)

    price = models.FloatField("Retail Price (excluding Tax)", default=0.0)
    price_category = models.ForeignKey(ProductPriceCategory, null=True)

    taxons = models.ManyToManyField(Taxon)

    def __unicode__(self):
        return self.name

