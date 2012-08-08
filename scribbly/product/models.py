from decimal import Decimal
from django.db import models

from pricing.models import ProductPriceCategory
from customer.models import Customer
from taxon.models import Taxon

class Product(models.Model):
    """
    A product in the inventory which can be sold.
    """
    sku = models.CharField("SKU", max_length=50)
    name = models.CharField(max_length=100)

    # Inventory tracking
    # on_hand = models.IntegerField()

    price = models.FloatField("Retail Price", default=0.0)
    price_category = models.ForeignKey(ProductPriceCategory, null=True)

    taxons = models.ManyToManyField(Taxon)

    @property
    def customer_discount(self, user):
        customer = Customer.objects.filter(user=user)
        DiscountMatrixEntry.objects.filter(customer_category=customer.customer_category)
        return 0.3

    @property
    def customer_price(self):
        return (self.price * (1- self.customer_discount)) 

    def __unicode__(self):
        return self.name
